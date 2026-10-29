import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from careers.models import Career, CareerSkillRequirement
from opportunities.models import JobOpportunity, Internship, GovernmentExam, Course
from profiles.models import Degree, Skill

print("Starting 20,000 Massive Dataset Seeder Across All 8 Domain Clusters...")

# -------------------------------------------------------------
# Base Data Definitions
# -------------------------------------------------------------
CITIES = ["Bengaluru", "Mumbai", "Delhi NCR", "Hyderabad", "Chennai", "Pune", "Kolkata", "Mysuru", "Ahmedabad", "Chandigarh", "Jaipur", "Lucknow", "Kochi", "Coimbatore", "Bhopal", "Remote"]
JOB_TYPES = ["Full-time", "Remote", "Hybrid", "Contract"]
DIFFICULTIES = ["Beginner", "Intermediate", "Advanced"]
PROVIDERS = ["Udemy", "Coursera", "NPTEL", "GeeksforGeeks", "Simplilearn", "W3Schools"]

CLUSTER_DATA = {
    'medical': {
        'titles': ["Senior Dental Surgeon", "Cosmetic Dentist", "Orthodontist Specialist", "Oral & Maxillofacial Surgeon", "Endodontist & Root Canal Specialist", "Periodontist & Implantologist", "Pediatric Dentist", "Resident Medical Officer", "Consultant Cardiologist", "Consultant Neurologist", "Clinical Research Associate", "Pharmacovigilance Officer", "Head ICU Nurse", "Senior Physiotherapist", "Consultant Radiologist", "Clinical Psychologist", "Veterinary Medical Officer"],
        'companies': ["Apollo Dental Clinics", "Clove Dental Care", "Sabka Dentist Healthcare", "Fortis Healthcare", "Max Super Speciality Hospital", "Manipal Hospitals", "Syngene International", "IQVIA India", "Dr. Reddy's Laboratories", "Sun Pharma R&D", "Narayana Health", "Tata Memorial Hospital", "NIMHANS Care", "SRL Diagnostics"],
        'skills': ["Clinical Examination", "Dental Radiology", "Restorative Dentistry", "Endodontics", "Root Canal Therapy", "Oral Surgery", "Patient Care", "Clinical Diagnostics", "Pharmacovigilance", "Clinical Trials", "ICU Protocols", "Physiotherapy", "Medical Imaging", "Clinical Psychology", "Veterinary Surgery"],
        'exams': [("NEET-MDS 2027", "NBE"), ("INI-CET Medical & Dental", "AIIMS New Delhi"), ("NEET-PG 2027", "NBE"), ("GPAT Pharmacy 2027", "NTA"), ("FMGE 2027", "NBEMS"), ("USMLE Step 1/2", "ECFMG USA"), ("UPSC Medical Officer", "UPSC")],
        'degrees': ['BDS', 'MBBS', 'NURSING', 'BPHARM', 'DPHARM', 'PHYSIOTHERAPY', 'RADIOLOGY', 'PSYCHOLOGY', 'VETERINARY']
    },
    'tech': {
        'titles': ["Full Stack Web Developer", "AI & Machine Learning Engineer", "DevOps & Cloud Architect", "Data Scientist", "Cybersecurity Analyst", "Mobile App Developer (iOS/Android)", "Backend Software Engineer", "Frontend React Developer", "Data Engineer", "SRE & Systems Administrator", "QA Automation Engineer", "Embedded Systems Engineer", "Robotics Software Engineer"],
        'companies': ["Google India", "Microsoft India", "Amazon Web Services", "TCS Digital", "Infosys Technologies", "Wipro Digital", "Accenture Tech", "Flipkart Engineering", "Swiggy Tech", "Zomato Product", "Razorpay Engineering", "Freshworks Tech"],
        'skills': ["Python", "Java", "C++", "React.js", "Node.js", "SQL & Databases", "Data Structures & Algorithms", "AWS Cloud", "DevOps & Docker", "Machine Learning", "Cybersecurity", "Git & GitHub", "REST APIs"],
        'exams': [("GATE Computer Science 2027", "IIT / GATE Committee"), ("ISRO Scientist SC Tech", "ISRO"), ("DRDO Scientist B", "DRDO"), ("NIC Scientist B Exam", "NIC"), ("NIMCET MCA Entrance", "NIT Consortium"), ("C-DAC C-CAT Tech", "C-DAC")],
        'degrees': ['BTECH', 'MTECH', 'BE', 'ME', 'BCA', 'MCA', 'BSC_CS', 'DIPLOMA', 'ITI']
    },
    'commerce': {
        'titles': ["Investment Banking Analyst", "Chartered Accountant (CA)", "Statutory Audit Manager", "Equity Research Analyst", "Corporate Taxation Consultant", "Financial Controller & CFO", "Corporate Financial Analyst", "Internal Audit Senior", "Portfolio Wealth Manager", "Risk & Compliance Specialist"],
        'companies': ["Goldman Sachs India", "Morgan Stanley", "Deloitte India", "PwC India", "EY India", "KPMG India", "HDFC Bank Corporate", "ICICI Bank Finance", "Barclays Wealth", "Reliance Financials"],
        'skills': ["Financial Modeling & Excel", "Corporate Finance & Valuation", "Accounting Standards", "GST Compliance", "Statutory Audit", "Income Tax Filing", "Financial Markets", "Internal Audit", "Portfolio Management"],
        'exams': [("CA Final Exam 2027", "ICAI"), ("CFA Level 1 & 2", "CFA Institute"), ("CMA Final Exam", "ICMAI"), ("CS Professional Exam", "ICSI"), ("IBPS PO 2027", "IBPS"), ("RBI Grade B Officer", "RBI"), ("SEBI Grade A Officer", "SEBI")],
        'degrees': ['BCOM', 'MCOM', 'BBA', 'MBA', 'BMS', 'CA']
    },
    'legal': {
        'titles': ["Corporate Legal Counsel", "Cyber & IT Law Specialist", "Litigation Advocate", "Intellectual Property Attorney", "Judicial Magistrate", "Commercial Arbitrator & Mediator", "Environmental Law Legal Officer", "M&A Legal Associate"],
        'companies': ["Khaitan & Co", "Shardul Amarchand Mangaldas", "AZB & Partners", "Luthra and Luthra Law", "Trilegal India", "Cyril Amarchand Mangaldas", "Remfry & Sagar IP Law"],
        'skills': ["Corporate Law", "Contract Law", "Legal Drafting", "Court Litigation", "Cyber Law", "Intellectual Property Rights", "Commercial Arbitration", "Constitutional Law"],
        'exams': [("AIBE 2027 Bar Exam", "Bar Council of India"), ("Judicial Services Exam (PCS-J)", "State High Courts"), ("CLAT-PG 2027 LLM", "Consortium of NLUs"), ("SEBI Legal Officer Exam", "SEBI")],
        'degrees': ['LLB', 'BALLB', 'BBALLB', 'LLM']
    },
    'agriculture': {
        'titles': ["Senior Agronomist", "Horticulture Greenhouse Manager", "Sericulture Technology Specialist", "Agribusiness Supply Chain Manager", "Soil Health & Fertilizer Scientist", "Seed Tech Breeding Specialist", "Agri Drone Precision Specialist"],
        'companies': ["ITC Agri Business", "Mahindra Agri Solutions", "UPL Agro Solutions", "Nuziveedu Seeds", "Central Silk Board", "DeHaat Agri Tech", "Godrej Agrovet"],
        'skills': ["Agronomy", "Horticulture", "Sericulture", "Soil Science", "Plant Breeding", "Precision Farming", "Agribusiness", "Crop Protection"],
        'exams': [("ICAR AIEEA PG 2027", "ICAR / NTA"), ("NABARD Grade A Officer", "NABARD"), ("IBPS AFO (Agri Officer)", "IBPS"), ("State Agriculture Officer Exam", "State PSC")],
        'degrees': ['AGRI', 'SERICULTURE', 'HORTICULTURE', 'VETERINARY']
    },
    'architecture': {
        'titles': ["BIM Architect & Project Designer", "Senior Architectural Designer", "Urban Planner & GIS Specialist", "Landscape Architect", "Interior & Sustainable Design Specialist", "Building Construction Manager"],
        'companies': ["Hafeez Contractor Architects", "Morphogenesis Architects", "Atkins Realis Architecture", "Livspace Design Studios", "CPWD India Architecture Wing"],
        'skills': ["Architectural Design", "BIM", "AutoCAD", "Revit", "Urban Planning", "Landscape", "3D Rendering", "Sustainable Arch"],
        'exams': [("GATE Architecture & Planning", "IIT / GATE Committee"), ("NATA 2027 Architecture", "Council of Architecture"), ("CEPT MArch Entrance", "CEPT University")],
        'degrees': ['BARCH', 'MARCH']
    },
    'arts': {
        'titles': ["Lead UX/UI Designer", "Digital News Editor & Journalist", "Creative Art Director", "Motion Graphics Designer", "Brand Identity Specialist", "Copywriter & Content Strategist"],
        'companies': ["Flipkart Design Studios", "The Hindu Group", "Ogilvy Advertising", "Hotstar Visual Studios", "Swiggy Product Design", "Zomato Creative Lab"],
        'skills': ["UX/UI Design", "Figma", "Journalism", "Digital Media", "Graphic Design", "Adobe Creative Suite", "Branding", "User Research"],
        'exams': [("NID DAT PG 2027", "National Institute of Design"), ("UGC NET Journalism", "NTA"), ("NIFT Master of Design", "NIFT")],
        'degrees': ['BA', 'MA', 'BFA', 'BDES', 'BJMC']
    },
    'science': {
        'titles': ["Senior Research Scientist", "Biotechnologist R&D Specialist", "Bioinformatician & Computational Biologist", "Analytical Chemist", "Clinical Microbiologist R&D"],
        'companies': ["Biocon Research", "Syngene Biotech R&D", "Strand Life Sciences", "Indian Institute of Science (IISc)", "CSIR National Chemical Lab"],
        'skills': ["Research Methodology", "Laboratory Techniques", "Biotechnology", "Molecular Biology", "Scientific Writing", "Data Analysis"],
        'exams': [("CSIR NET Chemical Sciences", "CSIR / NTA"), ("CSIR NET Life Sciences", "CSIR / NTA"), ("GATE Biotechnology 2027", "IIT Committee")],
        'degrees': ['BSC', 'MSC']
    }
}

# Fetch degree objects mapping
degree_objs = {d.code.upper(): d for d in Degree.objects.all()}

# -------------------------------------------------------------
# 1. Bulk Generate Job Opportunities (Target: ~10,000)
# -------------------------------------------------------------
print("Generating ~10,000 Job Opportunities...")
jobs_to_create = []

for _ in range(10000):
    c_key = random.choice(list(CLUSTER_DATA.keys()))
    c_info = CLUSTER_DATA[c_key]
    title = f"{random.choice(c_info['titles'])} #{random.randint(100, 9999)}"
    comp = random.choice(c_info['companies'])
    loc = random.choice(CITIES)
    jtype = random.choice(JOB_TYPES)
    sal = f"₹{random.randint(5, 18)} - ₹{random.randint(19, 45)} LPA"
    exp = f"{random.randint(0, 3)} - {random.randint(4, 8)} Years"
    desc = f"Opportunity for {title} at {comp}. Role involves core tasks in {c_key.upper()} domain including {', '.join(c_info['skills'][:3])}. Competitive compensation and career growth."
    url = f"https://{comp.lower().replace(' ', '')}.com/careers/{random.randint(10000, 99999)}"
    
    jobs_to_create.append(JobOpportunity(
        title=title,
        company=comp,
        location=loc,
        job_type=jtype,
        salary_range=sal,
        experience_required=exp,
        description=desc,
        application_url=url,
        is_active=True
    ))

JobOpportunity.objects.bulk_create(jobs_to_create, batch_size=2500)
print("Saved 10,000 Job Opportunities!")

# -------------------------------------------------------------
# 2. Bulk Generate Internships (Target: ~4,000)
# -------------------------------------------------------------
print("Generating ~4,000 Internships...")
internships_to_create = []

for _ in range(4000):
    c_key = random.choice(list(CLUSTER_DATA.keys()))
    c_info = CLUSTER_DATA[c_key]
    title = f"{c_key.title()} Intern - {random.choice(c_info['titles'])} #{random.randint(100, 9999)}"
    org = random.choice(c_info['companies'])
    dur = random.choice(["3 Months", "6 Months", "9 Months"])
    stip = f"₹{random.randint(12, 35)},000 / month"
    loc = random.choice(CITIES)
    elig = f"Students or Graduates in {', '.join(c_info['degrees'][:2])}"
    desc = f"Hands-on internship for {title} at {org}. Gain practical exposure in {c_key.upper()} workflows, mentorship by senior specialists, and Certificate of Completion."
    url = f"https://{org.lower().replace(' ', '')}.com/internships/{random.randint(10000, 99999)}"

    internships_to_create.append(Internship(
        title=title,
        organization=org,
        duration=dur,
        stipend=stip,
        location=loc,
        eligibility=elig,
        description=desc,
        application_url=url
    ))

Internship.objects.bulk_create(internships_to_create, batch_size=2000)
print("Saved 4,000 Internships!")

# -------------------------------------------------------------
# 3. Bulk Generate Online Courses (Target: ~3,000)
# -------------------------------------------------------------
print("Generating ~3,000 Online Courses...")
# Fetch existing skills or get one
all_skills = list(Skill.objects.all())
if not all_skills:
    all_skills = [Skill.objects.create(name="Core Professional Skill")]

courses_to_create = []
for _ in range(3000):
    c_key = random.choice(list(CLUSTER_DATA.keys()))
    c_info = CLUSTER_DATA[c_key]
    s_name = random.choice(c_info['skills'])
    sk, _ = Skill.objects.get_or_create(name=s_name)
    prov = random.choice(PROVIDERS)
    diff = random.choice(DIFFICULTIES)
    title = f"Mastering {s_name} in {c_key.title()} #{random.randint(100, 9999)}"
    desc = f"Comprehensive {diff} level online course on {s_name}. Includes hands-on projects, expert lectures, downloadable resources, and industry certification."
    url = f"https://{prov.lower()}.com/course/{s_name.lower().replace(' ', '-')}-{random.randint(1000, 9999)}"

    courses_to_create.append(Course(
        title=title,
        provider=prov,
        difficulty=diff,
        skill=sk,
        description=desc,
        url=url
    ))

Course.objects.bulk_create(courses_to_create, batch_size=1500)
print("Saved 3,000 Online Courses!")

# -------------------------------------------------------------
# 4. Bulk Generate Government & Competitive Exams (Target: ~1,000)
# -------------------------------------------------------------
print("Generating ~1,000 Competitive Exams...")
exams_to_create = []

for _ in range(1000):
    c_key = random.choice(list(CLUSTER_DATA.keys()))
    c_info = CLUSTER_DATA[c_key]
    base_name, body = random.choice(c_info['exams'])
    exam_name = f"{base_name} Cycle #{random.randint(100, 9999)}"
    cat = "govt" if "UPSC" in body or "NTA" in body or "NBE" in body or "IIT" in body or "ICAI" in body else "private"
    dom = f"{c_key.title()} & Professional"
    elig = f"Graduates with Degree in {', '.join(c_info['degrees'][:3])}"
    syllabus = f"Comprehensive {c_key.title()} syllabus covering {', '.join(c_info['skills'][:4])} and analytical aptitude."
    url = f"https://{body.lower().replace(' ', '')}.org/exams/{random.randint(1000, 9999)}"

    exams_to_create.append(GovernmentExam(
        exam_name=exam_name,
        conducting_body=body,
        category=cat,
        domain=dom,
        eligibility=elig,
        syllabus_summary=syllabus,
        website_url=url,
        is_active=True
    ))

GovernmentExam.objects.bulk_create(exams_to_create, batch_size=1000)
print("Saved 1,000 Competitive Exams!")

# -------------------------------------------------------------
# 5. Bulk Generate Careers (Target: ~2,000)
# -------------------------------------------------------------
print("Generating ~2,000 Careers...")

for i in range(2000):
    c_key = random.choice(list(CLUSTER_DATA.keys()))
    c_info = CLUSTER_DATA[c_key]
    base_title = random.choice(c_info['titles'])
    title = f"{base_title} Specialist #{i+1000}"
    domain = c_key.title()
    desc = f"Professional career path as {title} in {c_key.title()}. Responsible for advanced domain execution, strategy, and innovation."
    min_s = float(random.randint(5, 15))
    max_s = float(random.randint(16, 45))

    c, _ = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    
    # Link degrees
    for code in c_info['degrees']:
        if code in degree_objs:
            c.eligible_degrees.add(degree_objs[code])
    
    # Link skills
    for s_idx, sname in enumerate(c_info['skills'][:4]):
        sk, _ = Skill.objects.get_or_create(name=sname)
        importance = 'essential' if s_idx < 2 else 'recommended'
        CareerSkillRequirement.objects.get_or_create(career=c, skill=sk, defaults={'importance': importance})

print("\nSUCCESS! Successfully Generated 20,000 Total Datasets Across All Domains!")
