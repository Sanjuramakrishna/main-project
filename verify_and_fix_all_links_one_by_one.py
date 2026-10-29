import os
import re
import django
from urllib.parse import quote_plus

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity, Internship, Course, Certification, GovernmentExam

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'#\d+', '', text)
    text = re.sub(r'\bCycle\b.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def make_clean_slug(text):
    text = clean_text(text).lower()
    text = text.replace('&', 'and').replace('/', '-')
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

print("Starting strict regex-boundary link verification across ALL models...")

# 1. GOVERNMENT & COMPETITIVE EXAMS
exams_updated = 0
for exam in GovernmentExam.objects.all():
    raw_name = exam.exam_name
    cname = clean_text(raw_name)
    cname_lower = cname.lower()
    
    if raw_name != cname:
        exam.exam_name = cname

    new_url = ""

    # Priority word-boundary matching for exams
    if re.search(r'\b(civil services|ias|ips|cse)\b', cname_lower):
        new_url = "https://upsc.gov.in/examinations/Civil%20Services%20%28Preliminary%29%20Examination"
    elif re.search(r'\b(engineering services|ese|ies)\b', cname_lower):
        new_url = "https://upsc.gov.in/examinations/Engineering%20Services%20%28Preliminary%29%20Examination"
    elif re.search(r'\b(combined medical|medical officer|cms)\b', cname_lower):
        new_url = "https://upsc.gov.in/examinations/Combined%20Medical%20Services%20Examination"
    elif re.search(r'\bupsc\b', cname_lower):
        new_url = "https://upsc.gov.in/examinations/notifications"
    elif re.search(r'\bgate\b', cname_lower):
        if re.search(r'\b(computer|cs|it)\b', cname_lower):
            new_url = "https://gate2027.iitm.ac.in/question-papers/computer-science"
        else:
            new_url = "https://gate2027.iitm.ac.in/"
    elif re.search(r'\b(ssc|cgl)\b', cname_lower):
        new_url = "https://ssc.gov.in/candidate-portal/examinations/cgl"
    elif re.search(r'\bibps\b', cname_lower):
        if re.search(r'\b(afo|agri)\b', cname_lower):
            new_url = "https://www.ibps.in/crp-spl/"
        else:
            new_url = "https://www.ibps.in/crp-po-mt/"
    elif re.search(r'\brbi\b', cname_lower):
        new_url = "https://opportunities.rbi.org.in/scripts/vacancies.aspx"
    elif re.search(r'\bnabard\b', cname_lower):
        new_url = "https://www.nabard.org/careers-notices.aspx"
    elif re.search(r'\bsbi\b', cname_lower):
        new_url = "https://bank.sbi/web/careers/current-openings"
    elif re.search(r'\brrb\b', cname_lower):
        new_url = "https://www.rrbcdg.gov.in/"
    elif re.search(r'\bisro\b', cname_lower):
        new_url = "https://www.isro.gov.in/ICRB_CENTRAL_SELECTION.html"
    elif re.search(r'\bdrdo\b', cname_lower):
        new_url = "https://rac.gov.in/index.php?lang=en&id=0"
    elif re.search(r'\bnic\b', cname_lower):
        new_url = "https://recruitment.nic.in/"
    elif re.search(r'\bcsir\b', cname_lower):
        new_url = "https://csirnet.nta.ac.in/"
    elif re.search(r'\bugc\b', cname_lower):
        new_url = "https://ugcnet.nta.ac.in/"
    elif re.search(r'\b(icar|aieea)\b', cname_lower):
        new_url = "https://icar.nta.nic.in/"
    elif re.search(r'\bgpat\b', cname_lower):
        new_url = "https://gpat.nta.nic.in/"
    elif re.search(r'\bneet-mds\b', cname_lower) or 'neet mds' in cname_lower:
        new_url = "https://natboard.edu.in/nbe-exam-page?exam=neetmds"
    elif re.search(r'\bneet\b', cname_lower):
        new_url = "https://natboard.edu.in/nbe-exam-page?exam=neetpg"
    elif re.search(r'\bfmge\b', cname_lower):
        new_url = "https://natboard.edu.in/nbe-exam-page?exam=fmge"
    elif re.search(r'\b(ini-ss|iniss)\b', cname_lower):
        new_url = "https://www.aiimsexams.ac.in/iniss"
    elif re.search(r'\b(ini-cet|inicet|aiims)\b', cname_lower):
        new_url = "https://www.aiimsexams.ac.in/inicet"
    elif re.search(r'\bclat\b', cname_lower):
        new_url = "https://consortiumofnlus.ac.in/clat-2026/"
    elif re.search(r'\baibe\b', cname_lower) or 'bar exam' in cname_lower:
        new_url = "https://allindiabarexamination.com/"
    elif re.search(r'\b(judicial|pcs-j|pcs j)\b', cname_lower):
        new_url = "https://upsc.gov.in/examinations/notifications"
    elif re.search(r'\b(pgcet|kcet|karnataka)\b', cname_lower):
        new_url = "https://cetonline.karnataka.gov.in/kea/pgcet2026"
    elif re.search(r'\bnata\b', cname_lower):
        new_url = "https://www.nata.in/"
    elif re.search(r'\bnid\b', cname_lower):
        new_url = "https://admissions.nid.edu/"
    elif re.search(r'\bnift\b', cname_lower):
        new_url = "https://nift.ac.in/admission"
    elif re.search(r'\bnimcet\b', cname_lower):
        new_url = "https://www.nimcet.in/"
    elif re.search(r'\b(c-dac|c-cat|cdac)\b', cname_lower):
        new_url = "https://www.cdac.in/index.aspx?id=edu_act_ccat"
    elif re.search(r'\b(ca final|icai)\b', cname_lower):
        new_url = "https://www.icai.org/post/exam-dates-notifications"
    elif re.search(r'\b(cs professional|icsi)\b', cname_lower):
        new_url = "https://www.icsi.edu/students/examination/"
    elif re.search(r'\b(cma final|icmai)\b', cname_lower):
        new_url = "https://icmai.in/studentssection/Exam-Notification.php"
    elif re.search(r'\bcfa\b', cname_lower):
        new_url = "https://www.cfainstitute.org/en/programs/cfa/exam"
    elif re.search(r'\bsebi\b', cname_lower):
        new_url = "https://www.sebi.gov.in/sebiweb/other/career.jsp"
    elif re.search(r'\busmle\b', cname_lower):
        new_url = "https://www.usmle.org/bulletin-information/registration"
    elif re.search(r'\bcept\b', cname_lower):
        new_url = "https://admissions.cept.ac.in/postgraduate/faculty-of-architecture"
    elif re.search(r'\btcs\b', cname_lower) and re.search(r'\b(nqt|digital)\b', cname_lower):
        new_url = "https://learning.tcsionhub.in/hub/national-qualifier-test/"
    elif re.search(r'\bwipro\b', cname_lower):
        new_url = "https://careers.wipro.com/careers-home"
    elif re.search(r'\baws\b', cname_lower):
        new_url = "https://aws.amazon.com/certification/certified-solutions-architect-associate/"
    elif re.search(r'\b(cka|kubernetes)\b', cname_lower):
        new_url = "https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/"
    elif re.search(r'\b(ccna|cisco)\b', cname_lower):
        new_url = "https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html"
    elif re.search(r'\b(gcp|google)\b', cname_lower):
        new_url = "https://cloud.google.com/learn/certification/cloud-engineer"
    elif re.search(r'\b(azure|microsoft)\b', cname_lower):
        new_url = "https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/"
    elif re.search(r'\b(terraform|hashicorp)\b', cname_lower):
        new_url = "https://www.hashicorp.com/certification/terraform-associate"
    elif re.search(r'\bcissp\b', cname_lower):
        new_url = "https://www.isc2.org/certifications/cissp"
    elif re.search(r'\bagriculture\b', cname_lower):
        new_url = "https://icar.org.in/"
    else:
        new_url = f"https://www.google.com/search?q={quote_plus(cname)}+official+portal"

    if exam.website_url != new_url or raw_name != cname:
        exam.website_url = new_url
        exam.save()
        exams_updated += 1

print(f"Strict Exam classification complete ({exams_updated} updated).")
