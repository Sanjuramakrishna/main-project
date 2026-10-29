import os
import django
import requests
import urllib3
import concurrent.futures

# Suppress insecure HTTPS warnings for testing SSL-mismatched government sites
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity, Internship, Course, Certification, GovernmentExam

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

def test_url(url):
    url = url.strip()
    if not url.startswith('http://') and not url.startswith('https://'):
        return (url, ('INVALID_SCHEMA', 0))
    try:
        # Try GET with stream=True and verify=False to catch 404s while ignoring self-signed SSL quirks
        response = requests.get(url, headers=HEADERS, timeout=8, stream=True, allow_redirects=True, verify=False)
        status = response.status_code
        if status in [200, 301, 302, 307, 308]:
            return (url, ('OK', status))
        elif status in [403, 405, 429]:
            # Bot protection (LinkedIn, Cloudflare) - valid browser URL
            return (url, ('BOT_PROTECTED', status))
        elif status == 404:
            return (url, ('NOT_FOUND_404', status))
        else:
            return (url, (f'HTTP_{status}', status))
    except requests.exceptions.SSLError:
        return (url, ('SSL_ERROR', 0))
    except requests.exceptions.ConnectionError:
        return (url, ('CONNECTION_ERROR', 0))
    except requests.exceptions.Timeout:
        return (url, ('TIMEOUT', 0))
    except Exception as e:
        return (url, (f'ERROR', 0))

print("=== STARTING COMPREHENSIVE LINK VALIDATION ACROSS ALL 5 MODELS ===")

# 1. CERTS
cert_urls = list(set(c.url for c in Certification.objects.all()))
print(f"\nTesting {len(cert_urls)} Certification URLs...")
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results_cert = dict(executor.map(test_url, cert_urls))

bad_cert_urls = set()
for u, (res_type, status) in results_cert.items():
    if res_type in ['NOT_FOUND_404', 'CONNECTION_ERROR', 'INVALID_SCHEMA']:
        print(f"FAILED Cert URL: [{res_type}] ({status}) {u}")
        bad_cert_urls.add(u)
    else:
        print(f"PASSED Cert URL: [{res_type}] ({status}) {u}")

# 2. EXAMS
exam_urls = list(set(e.website_url for e in GovernmentExam.objects.all()))
print(f"\nTesting {len(exam_urls)} Government Exam URLs...")
with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    results_exam = dict(executor.map(test_url, exam_urls))

bad_exam_urls = set()
for u, (res_type, status) in results_exam.items():
    if res_type in ['NOT_FOUND_404', 'CONNECTION_ERROR', 'INVALID_SCHEMA']:
        print(f"FAILED Exam URL: [{res_type}] ({status}) {u}")
        bad_exam_urls.add(u)
    else:
        print(f"PASSED Exam URL: [{res_type}] ({status}) {u}")

print(f"\nSummary: Found {len(bad_exam_urls)} broken Exam URLs out of {len(exam_urls)} total.")

# 3. INTERNSHIPS
intern_urls = list(set(i.application_url for i in Internship.objects.all()))
print(f"\nTesting {len(intern_urls)} Internship unique URLs...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results_intern = dict(executor.map(test_url, intern_urls))

bad_intern_urls = set()
for u, (res_type, status) in results_intern.items():
    if res_type in ['NOT_FOUND_404', 'CONNECTION_ERROR', 'INVALID_SCHEMA']:
        print(f"FAILED Internship URL: [{res_type}] ({status}) {u}")
        bad_intern_urls.add(u)

print(f"\nSummary: Found {len(bad_intern_urls)} broken Internship URLs out of {len(intern_urls)} total.")

# 4. JOBS
job_urls = list(set(j.application_url for j in JobOpportunity.objects.all()))
print(f"\nTesting {len(job_urls)} Job Opportunity unique URLs...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results_job = dict(executor.map(test_url, job_urls))

bad_job_urls = set()
for u, (res_type, status) in results_job.items():
    if res_type in ['NOT_FOUND_404', 'CONNECTION_ERROR', 'INVALID_SCHEMA']:
        print(f"FAILED Job URL: [{res_type}] ({status}) {u}")
        bad_job_urls.add(u)

print(f"\nSummary: Found {len(bad_job_urls)} broken Job URLs out of {len(job_urls)} total.")

# 5. COURSES
course_urls = list(set(c.url for c in Course.objects.all()))
print(f"\nTesting {len(course_urls)} Course unique URLs...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results_course = dict(executor.map(test_url, course_urls))

bad_course_urls = set()
for u, (res_type, status) in results_course.items():
    if res_type in ['NOT_FOUND_404', 'CONNECTION_ERROR', 'INVALID_SCHEMA']:
        print(f"FAILED Course URL: [{res_type}] ({status}) {u}")
        bad_course_urls.add(u)

print(f"\nSummary: Found {len(bad_course_urls)} broken Course URLs out of {len(course_urls)} total.")
