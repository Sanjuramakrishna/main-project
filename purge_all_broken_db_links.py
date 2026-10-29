import os
import django
import requests
import urllib3
import concurrent.futures

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity, Internship, Course, Certification, GovernmentExam

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

print("=== STARTING FAST MULTI-THREADED LINK AUDIT AND PURGE ===")

all_urls = set()
for c in Certification.objects.all(): all_urls.add(c.url.strip())
for e in GovernmentExam.objects.all(): all_urls.add(e.website_url.strip())
for i in Internship.objects.all(): all_urls.add(i.application_url.strip())
for j in JobOpportunity.objects.all(): all_urls.add(j.application_url.strip())
for c in Course.objects.all(): all_urls.add(c.url.strip())

print(f"Checking {len(all_urls)} total unique URL endpoints across all models...")

endpoint_status = {}

def check_url(url):
    if not url.startswith('http'):
        return (url, False)
    try:
        r = requests.get(url, headers=HEADERS, timeout=3, stream=True, allow_redirects=True, verify=False)
        if r.status_code in [200, 201, 301, 302, 307, 308, 403, 405, 429]:
            return (url, True)
        elif r.status_code == 404:
            return (url, False)
        else:
            return (url, True)
    except Exception:
        return (url, False)

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(check_url, u) for u in all_urls]
    for f in concurrent.futures.as_completed(futures):
        u, is_valid = f.result()
        endpoint_status[u] = is_valid

dead_certs = 0
for cert in Certification.objects.all():
    if not endpoint_status.get(cert.url.strip(), True):
        cert.delete()
        dead_certs += 1

dead_exams = 0
for exam in GovernmentExam.objects.all():
    if not endpoint_status.get(exam.website_url.strip(), True):
        exam.delete()
        dead_exams += 1

dead_interns = 0
for intern in Internship.objects.all():
    if not endpoint_status.get(intern.application_url.strip(), True):
        intern.delete()
        dead_interns += 1

dead_jobs = 0
for job in JobOpportunity.objects.all():
    if not endpoint_status.get(job.application_url.strip(), True):
        job.delete()
        dead_jobs += 1

dead_courses = 0
for course in Course.objects.all():
    if not endpoint_status.get(course.url.strip(), True):
        course.delete()
        dead_courses += 1

print(f"\nPurge Complete!")
print(f"Certifications remaining: {Certification.objects.count()} (Purged {dead_certs})")
print(f"Government Exams remaining: {GovernmentExam.objects.count()} (Purged {dead_exams})")
print(f"Internships remaining: {Internship.objects.count()} (Purged {dead_interns})")
print(f"Job Opportunities remaining: {JobOpportunity.objects.count()} (Purged {dead_jobs})")
print(f"Courses remaining: {Course.objects.count()} (Purged {dead_courses})")
