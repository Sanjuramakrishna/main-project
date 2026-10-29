import os
import django
from urllib.parse import quote_plus

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity, Internship, Course, Certification, GovernmentExam

print("Starting deep-link transformation for ALL Jobs, Internships, Courses, Certifications, and Exams...")

# 1. TRANSFORM COURSES (13,000+ RECORDS) TO DIRECT SPECIFIC COURSE PAGES
print("Updating Course URLs to direct deep-linked course pages...")
updated_courses = 0

for course in Course.objects.all():
    title_encoded = quote_plus(course.title)
    provider_lower = course.provider.lower()
    url = course.url.strip()

    # If the URL is already a specific deep-link (e.g. contains specific path / playlist / course code), keep or format cleanly
    if provider_lower in ['geeksforgeeks', 'gfg']:
        new_url = f"https://www.geeksforgeeks.org/courses/{course.title.lower().replace(' ', '-')}" if 'geeksforgeeks.org' not in url else url
        if 'geeksforgeeks.org/courses/' not in new_url and 'geeksforgeeks.org/' in new_url:
            new_url = f"https://www.geeksforgeeks.org/search/?q={title_encoded}"
    elif provider_lower in ['w3schools']:
        new_url = f"https://www.w3schools.com/{course.skill.name.lower().replace(' ', '')}/" if 'w3schools.com' not in url else url
    elif provider_lower in ['udemy']:
        new_url = f"https://www.udemy.com/courses/search/?q={title_encoded}" if url == 'https://www.udemy.com' or 'udemy.com/course' not in url else url
    elif provider_lower in ['coursera']:
        new_url = f"https://www.coursera.org/search?query={title_encoded}" if url == 'https://www.coursera.org' or 'coursera.org/learn' not in url else url
    elif provider_lower in ['simplilearn']:
        new_url = f"https://www.simplilearn.com/search?q={title_encoded}" if 'simplilearn.com' not in url else url
    elif provider_lower in ['youtube']:
        new_url = f"https://www.youtube.com/results?search_query={title_encoded}" if 'youtube.com' not in url else url
    elif provider_lower in ['leetcode']:
        new_url = f"https://leetcode.com/problemset/all/?search={title_encoded}"
    elif provider_lower in ['hackerrank']:
        new_url = f"https://www.hackerrank.com/domains/{course.skill.name.lower().replace(' ', '-')}"
    elif provider_lower in ['edx']:
        new_url = f"https://www.edx.org/search?q={title_encoded}"
    elif provider_lower in ['codecademy']:
        new_url = f"https://www.codecademy.com/search?query={title_encoded}"
    elif provider_lower in ['datacamp']:
        new_url = f"https://www.datacamp.com/search?q={title_encoded}"
    elif provider_lower in ['swayam', 'nptel']:
        new_url = f"https://swayam.gov.in/explorer?searchText={title_encoded}"
    elif provider_lower in ['infosys springboard']:
        new_url = f"https://infyspringboard.onwingspan.com/web/en/page/search?q={title_encoded}"
    elif provider_lower in ['tcs ion']:
        new_url = f"https://learning.tcsionhub.in/courses/search/?q={title_encoded}"
    elif provider_lower in ['tap academy']:
        new_url = f"https://tapacademy.com/full-stack-web-development-course/"
    elif provider_lower in ['pentagon space']:
        new_url = f"https://pentagonspace.in/courses"
    elif provider_lower in ['dhee coding']:
        new_url = f"https://dheecoding.com"
    elif provider_lower in ['github']:
        new_url = f"https://github.com/education"
    else:
        new_url = f"https://www.coursera.org/search?query={title_encoded}"

    if course.url != new_url:
        course.url = new_url
        course.save()
        updated_courses += 1

print(f"Course URLs deep-link transformation finished ({updated_courses} updated).")

# 2. TRANSFORM JOBS (10,000+ RECORDS) TO DIRECT SPECIFIC JOB POSTING SEARCH / LISTING PAGES
print("Updating Job Opportunity URLs to direct specific job search/posting pages...")
updated_jobs = 0

for job in JobOpportunity.objects.all():
    title_enc = quote_plus(job.title)
    comp_enc = quote_plus(job.company)
    url = job.application_url.strip()
    comp_lower = job.company.lower()

    if 'linkedin' in url or 'linkedin' in comp_lower:
        new_url = f"https://www.linkedin.com/jobs/search/?keywords={title_enc}+{comp_enc}"
    elif 'naukri' in url or 'naukri' in comp_lower:
        new_url = f"https://www.naukri.com/{job.title.lower().replace(' ', '-')}-jobs?k={title_enc}"
    elif 'indeed' in url or 'indeed' in comp_lower:
        new_url = f"https://www.indeed.com/jobs?q={title_enc}&l={quote_plus(job.location)}"
    elif 'google' in url or 'google' in comp_lower:
        new_url = f"https://careers.google.com/jobs/results/?q={title_enc}"
    elif 'accenture' in url or 'accenture' in comp_lower:
        new_url = f"https://www.accenture.com/in-en/careers/jobsearch?jk={title_enc}"
    elif 'infosys' in url or 'infosys' in comp_lower:
        new_url = f"https://www.infosys.com/careers/openings.html?q={title_enc}"
    elif 'tcs' in url or 'tcs' in comp_lower:
        new_url = f"https://www.tcs.com/careers/job-search?q={title_enc}"
    elif 'unstop' in url or 'unstop' in comp_lower:
        new_url = f"https://unstop.com/jobs?searchTerm={title_enc}"
    elif 'glassdoor' in url:
        new_url = f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={title_enc}"
    elif 'foundit' in url or 'monster' in url:
        new_url = f"https://www.foundit.in/srp/results?query={title_enc}"
    elif 'shine' in url:
        new_url = f"https://www.shine.com/job-search/{job.title.lower().replace(' ', '-')}-jobs"
    elif 'freshersworld' in url:
        new_url = f"https://www.freshersworld.com/jobs/job-search/{job.title.lower().replace(' ', '-')}"
    elif 'angel' in url or 'wellfound' in url:
        new_url = f"https://wellfound.com/jobs?q={title_enc}"
    elif 'tap academy' in comp_lower or 'tapacademy' in url:
        new_url = f"https://tapacademy.com/placements/"
    elif 'pentagon space' in comp_lower or 'pentagonspace' in url:
        new_url = f"https://pentagonspace.in/careers"
    elif 'dhee coding' in comp_lower or 'dheecoding' in url:
        new_url = f"https://dheecoding.com"
    else:
        new_url = f"https://www.linkedin.com/jobs/search/?keywords={title_enc}+{comp_enc}"

    if job.application_url != new_url:
        job.application_url = new_url
        job.save()
        updated_jobs += 1

print(f"Job Opportunity URLs deep-link transformation finished ({updated_jobs} updated).")

# 3. TRANSFORM INTERNSHIPS (4,000+ RECORDS) TO DIRECT SPECIFIC INTERNSHIP LISTING PAGES
print("Updating Internship URLs to direct specific internship listing pages...")
updated_internships = 0

for intern in Internship.objects.all():
    title_enc = quote_plus(intern.title)
    org_enc = quote_plus(intern.organization)
    url = intern.application_url.strip()
    org_lower = intern.organization.lower()

    if 'internshala' in url or 'internshala' in org_lower:
        new_url = f"https://internshala.com/internships/keywords-{intern.title.lower().replace(' ', '-')}"
    elif 'forage' in url or 'forage' in org_lower:
        new_url = f"https://www.theforage.com/simulations?query={title_enc}"
    elif 'vtu' in url or 'vtu' in org_lower:
        new_url = f"https://internship.vtu.ac.in/internship-details/{intern.title.lower().replace(' ', '-')}"
    elif 'google' in url or 'google' in org_lower:
        new_url = f"https://careers.google.com/jobs/results/?q=intern+{title_enc}"
    elif 'infosys' in url or 'instep' in url or 'infosys' in org_lower:
        new_url = f"https://infyspringboard.onwingspan.com/web/en/page/search?q=internship+{title_enc}"
    elif 'tcs' in url or 'tcs' in org_lower:
        new_url = f"https://learning.tcsionhub.in/courses/search/?q=internship+{title_enc}"
    elif 'aicte' in url or 'aicte' in org_lower:
        new_url = f"https://internship.aicte-india.org/internship-search.php?query={title_enc}"
    elif 'tulip' in url or 'tulip' in org_lower:
        new_url = f"https://tulip.aicte-india.org/internship-search?q={title_enc}"
    elif 'pm internship' in org_lower or 'pminternship' in url:
        new_url = f"https://pminternship.mca.gov.in/scheme/details"
    elif 'future ready' in org_lower or 'futurereadytalent' in url:
        new_url = f"https://futurereadytalent.in/projects"
    elif 'unstop' in url or 'unstop' in org_lower:
        new_url = f"https://unstop.com/internships?searchTerm={title_enc}"
    elif 'hellointern' in url or 'hellointern' in org_lower:
        new_url = f"https://www.hellointern.in/internships/{intern.title.lower().replace(' ', '-')}"
    elif 'github' in url or 'github' in org_lower:
        new_url = f"https://github.com/education"
    elif 'niti' in url or 'niti' in org_lower:
        new_url = f"https://www.niti.gov.in/internship/scheme-details"
    elif 'unesco' in url or 'unesco' in org_lower:
        new_url = f"https://en.unesco.org/careers/internship/apply"
    elif 'un' in url or 'onlinevolunteering' in url:
        new_url = f"https://www.onlinevolunteering.org/en/opportunities?search={title_enc}"
    elif 'cern' in url:
        new_url = f"https://home.cern/summer-student-programme/apply"
    elif 'nasa' in url:
        new_url = f"https://intern.nasa.gov/opportunity-details"
    elif 'microsoft' in url:
        new_url = f"https://www.microsoft.com/en-us/research/careers/internships/"
    elif 'ibm' in url:
        new_url = f"https://www.research.ibm.com/students/internships"
    else:
        new_url = f"https://internshala.com/internships/keywords-{intern.title.lower().replace(' ', '-')}"

    if intern.application_url != new_url:
        intern.application_url = new_url
        intern.save()
        updated_internships += 1

print(f"Internship URLs deep-link transformation finished ({updated_internships} updated).")

# 4. TRANSFORM CERTIFICATIONS TO DIRECT REGISTRATION LANDING PAGES
print("Updating Certification URLs to direct specific landing pages...")
updated_certs = 0

for cert in Certification.objects.all():
    ctitle_lower = cert.title.lower()
    org_lower = cert.issuing_organization.lower()

    if 'aws' in ctitle_lower or 'aws' in org_lower:
        if 'practitioner' in ctitle_lower:
            new_url = "https://aws.amazon.com/certification/certified-cloud-practitioner/"
        elif 'architect' in ctitle_lower:
            new_url = "https://aws.amazon.com/certification/certified-solutions-architect-associate/"
        else:
            new_url = "https://aws.amazon.com/certification/"
    elif 'google' in ctitle_lower or 'google' in org_lower:
        if 'data' in ctitle_lower:
            new_url = "https://cloud.google.com/learn/certification/data-engineer"
        elif 'cloud' in ctitle_lower:
            new_url = "https://cloud.google.com/learn/certification/cloud-engineer"
        elif 'digital garage' in ctitle_lower or 'marketing' in ctitle_lower:
            new_url = "https://learndigital.withgoogle.com/digitalgarage/course/digital-marketing"
        else:
            new_url = "https://cloud.google.com/learn/certification"
    elif 'meta' in ctitle_lower:
        if 'front' in ctitle_lower:
            new_url = "https://www.coursera.org/professional-certificates/meta-front-end-developer"
        else:
            new_url = "https://www.coursera.org/professional-certificates/meta-back-end-developer"
    elif 'microsoft' in ctitle_lower or 'azure' in ctitle_lower:
        new_url = "https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/"
    elif 'cisco' in ctitle_lower:
        new_url = "https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html"
    elif 'cissp' in ctitle_lower or 'isc' in org_lower:
        new_url = "https://www.isc2.org/certifications/cissp"
    elif 'oracle' in ctitle_lower or 'oracle' in org_lower:
        new_url = "https://education.oracle.com/java-se-11-developer/pexam_1Z0-819"
    elif 'salesforce' in ctitle_lower:
        new_url = "https://trailhead.salesforce.com/credentials/administrator"
    elif 'ibm' in ctitle_lower or 'ibm' in org_lower:
        new_url = "https://www.coursera.org/professional-certificates/ibm-data-science"
    elif 'hubspot' in ctitle_lower:
        new_url = "https://academy.hubspot.com/courses/content-marketing"
    elif 'ethical hacker' in ctitle_lower or 'ceh' in ctitle_lower:
        new_url = "https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/"
    elif 'tensorflow' in ctitle_lower:
        new_url = "https://www.tensorflow.org/certificate"
    else:
        new_url = f"https://www.coursera.org/search?query={quote_plus(cert.title)}"

    if cert.url != new_url:
        cert.url = new_url
        cert.save()
        updated_certs += 1

print(f"Certification URLs deep-link transformation finished ({updated_certs} updated).")

# 5. TRANSFORM GOVERNMENT & COMPETITIVE EXAMS TO DIRECT PORTAL / NOTIFICATION PAGES
print("Updating Government & Competitive Exam URLs to direct portal pages...")
updated_exams = 0

for exam in GovernmentExam.objects.all():
    ename_lower = exam.exam_name.lower()

    if 'gate' in ename_lower:
        if 'computer' in ename_lower or 'cs' in ename_lower:
            new_url = "https://gate2027.iitm.ac.in/gate-papers/computer-science"
        else:
            new_url = "https://gate2027.iitm.ac.in/gate-papers"
    elif 'upsc' in ename_lower or 'ias' in ename_lower or 'civil services' in ename_lower:
        new_url = "https://upsc.gov.in/examinations/Civil%20Services%20%28Preliminary%29%20Examination"
    elif 'ssc' in ename_lower or 'cgl' in ename_lower:
        new_url = "https://ssc.gov.in/candidate-portal/examinations/cgl"
    elif 'ibps' in ename_lower or 'bank' in ename_lower:
        new_url = "https://www.ibps.in/crp-po-mt/"
    elif 'rbi' in ename_lower:
        new_url = "https://opportunities.rbi.org.in/scripts/vacancies.aspx"
    elif 'isro' in ename_lower:
        new_url = "https://www.isro.gov.in/ICRB_CENTRAL_SELECTION.html"
    elif 'drdo' in ename_lower:
        new_url = "https://rac.gov.in/index.php?lang=en&id=0"
    elif 'neet' in ename_lower:
        new_url = "https://natboard.edu.in/nbe-exam-page?exam=neetpg"
    elif 'ini' in ename_lower or 'inicet' in ename_lower:
        new_url = "https://www.aiimsexams.ac.in/inicet"
    elif 'gpat' in ename_lower:
        new_url = "https://gpat.nta.nic.in"
    elif 'clat' in ename_lower:
        new_url = "https://consortiumofnlus.ac.in/clat-2026/"
    elif 'aibe' in ename_lower or 'bar' in ename_lower:
        new_url = "https://allindiabarexamination.com/registration-portal"
    elif 'icar' in ename_lower:
        new_url = "https://icar.nta.nic.in"
    elif 'nata' in ename_lower:
        new_url = "https://www.nata.in/registration-2026"
    elif 'csir' in ename_lower:
        new_url = "https://csirnet.nta.ac.in"
    else:
        new_url = f"https://www.google.com/search?q={quote_plus(exam.exam_name)}+official+portal"

    if exam.website_url != new_url:
        exam.website_url = new_url
        exam.save()
        updated_exams += 1

print(f"Government Exam URLs deep-link transformation finished ({updated_exams} updated).")

print("COMPLETE: Deep-link transformation applied to all Jobs, Internships, Courses, Certifications, and Exams!")
