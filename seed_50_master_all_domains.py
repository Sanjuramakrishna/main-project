import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from careers.models import Career, CareerSkillRequirement
from opportunities.models import JobOpportunity, Internship, GovernmentExam, Course
from profiles.models import Degree, Skill

print("Seeding Additional 50 Master Items for All Domains...")

def get_skills(skill_names):
    skills = []
    for name in skill_names:
        s, _ = Skill.objects.get_or_create(name=name.strip())
        skills.append(s)
    return skills

def link_degrees(career, degree_codes):
    for code in degree_codes:
        degs = Degree.objects.filter(code__iexact=code)
        if degs.exists():
            for d in degs:
                career.eligible_degrees.add(d)

def link_skill_reqs(career, skill_names):
    for idx, sname in enumerate(skill_names):
        s, _ = Skill.objects.get_or_create(name=sname.strip())
        importance = 'essential' if idx < 3 else 'recommended'
        CareerSkillRequirement.objects.get_or_create(career=career, skill=s, defaults={'importance': importance})

# 1. MEDICAL / DENTAL / HEALTHCARE EXPANSION
medical_degs = ['BDS', 'MBBS', 'NURSING', 'BPHARM', 'DPHARM', 'PHYSIOTHERAPY', 'RADIOLOGY', 'PSYCHOLOGY', 'VETERINARY']

add_med_jobs = [
    ("Associate Dental Surgeon", "Sabka Dentist Healthcare", "Mumbai / Pune", "Full-time", "₹8 - ₹14 LPA", ["Clinical Examination", "Dental Radiology", "Restorative Dentistry"], "1 - 3 Years", "Provide general and preventive dental procedures.", "https://sabkadentist.com"),
    ("Consultant Radiologist", "SRL Diagnostics", "Delhi NCR", "Full-time", "₹15 - ₹28 LPA", ["Medical Imaging", "CT & MRI Interpretation", "Radiology"], "2 - 5 Years", "Analyze diagnostic MRI, CT, and ultrasonography scans.", "https://srlworld.com"),
    ("Senior Staff Nurse - ICU", "Fortis Hospital", "Bengaluru", "Full-time", "₹5 - ₹10 LPA", ["Nursing Care", "ICU Protocols", "Patient Care"], "1 - 4 Years", "Deliver critical intensive care nursing.", "https://fortishealthcare.com"),
    ("Quality Control Chemist - Pharma", "Sun Pharma Laboratories", "Vadodara / Hyderabad", "Full-time", "₹6 - ₹12 LPA", ["Pharmaceutical Analysis", "QA/QC", "Pharmacology"], "1 - 3 Years", "Perform analytical testing of pharmaceutical formulations.", "https://sunpharma.com"),
    ("Clinical Psychologist", "NIMHANS Allied Care", "Bengaluru", "Full-time", "₹7 - ₹14 LPA", ["Clinical Psychology", "Psychotherapy", "CBT"], "1 - 3 Years", "Provide psychological counseling and mental health assessments.", "https://nimhans.ac.in"),
    ("Veterinary Surgeon", "State Animal Husbandry Dept", "Field Locations", "Full-time", "₹8 - ₹15 LPA", ["Veterinary Surgery", "Animal Diagnostics", "Public Health"], "1 - 3 Years", "Manage veterinary care and livestock disease control.", "https://animalhusbandry.gov.in"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in add_med_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    j.required_skills.set(get_skills(req_s))

add_med_internships = [
    ("Hospital Administration Trainee", "Max Healthcare", "6 Months", "₹18,000 / month", "Delhi NCR", ["Hospital Administration", "Healthcare Policy"], "MBBS / BDS / Nursing / MHA", "Learn clinical operations and hospital quality control.", "https://maxhealthcare.in"),
    ("Pharmacy Research Trainee", "Lupin Pharmaceuticals", "6 Months", "₹20,000 / month", "Pune", ["Pharmaceutics", "Pharmacology"], "BPharm / PharmD", "Assist pharmaceutical formulation and R&D research.", "https://lupin.com"),
    ("Physiotherapy Clinical Intern", "Manipal Rehab Center", "6 Months", "₹15,000 / month", "Bengaluru", ["Physiotherapy", "Musculoskeletal Rehab"], "BPT Graduates", "Hands-on orthopaedic physical therapy rotations.", "https://manipalhospitals.com"),
]

for title, org, dur, stip, loc, req_s, elig, desc, url in add_med_internships:
    i, _ = Internship.objects.get_or_create(title=title, organization=org, defaults={
        'duration': dur, 'stipend': stip, 'location': loc, 'eligibility': elig, 'description': desc, 'application_url': url
    })
    i.required_skills.set(get_skills(req_s))

# 2. COMMERCE EXPANSION
add_comm_jobs = [
    ("Taxation Senior Specialist", "KPMG India", "Bengaluru / Gurgaon", "Full-time", "₹9 - ₹17 LPA", ["Income Tax Filing", "GST Compliance", "Taxation"], "2 - 4 Years", "Direct GST compliance and corporate tax advisory.", "https://home.kpmg/in"),
    ("Risk Analyst - Financial Audit", "EY India", "Mumbai / Hyderabad", "Full-time", "₹10 - ₹18 LPA", ["Internal Audit", "Statutory Audit", "Corporate Governance"], "2 - 4 Years", "Conduct financial risk assessment for corporate clients.", "https://ey.com/in"),
    ("Corporate Accountant", "Reliance Industries", "Mumbai", "Full-time", "₹7 - ₹14 LPA", ["Accounting Standards", "Corporate Finance & Valuation", "GST Compliance"], "1 - 3 Years", "Manage ledger accounting, financial statements, and balance sheets.", "https://ril.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in add_comm_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    j.required_skills.set(get_skills(req_s))

# 3. LEGAL EXPANSION
add_legal_jobs = [
    ("Junior Legal Counsel", "Luthra and Luthra Law Offices", "New Delhi", "Full-time", "₹10 - ₹18 LPA", ["Corporate Law", "Contract Law", "Legal Drafting"], "1 - 3 Years", "Draft commercial legal contracts and regulatory filings.", "https://luthra.com"),
    ("Litigation Associate", "AZB & Partners", "Mumbai", "Full-time", "₹12 - ₹22 LPA", ["Court Litigation", "Civil & Criminal Law", "Legal Drafting"], "2 - 4 Years", "Represent corporate clients in court proceedings and arbitration.", "https://azbpartners.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in add_legal_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    j.required_skills.set(get_skills(req_s))

# 4. AGRICULTURE EXPANSION
add_agri_jobs = [
    ("Soil Health Specialist", "UPL Agro Solutions", "Ahmedabad / Field", "Full-time", "₹6 - ₹12 LPA", ["Soil Science", "Agronomy", "Crop Protection"], "1 - 3 Years", "Analyze soil nutrient profiles and advise crop nutrient management.", "https://upl-ltd.com"),
    ("Sericulture Field Inspector", "Central Silk Board", "Mysuru / Bengaluru", "Full-time", "₹7 - ₹13 LPA", ["Sericulture", "Mulberry Cultivation", "Silk Reeling"], "1 - 3 Years", "Inspect silkworm seed production and mulberry farms.", "https://csb.gov.in"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in add_agri_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    j.required_skills.set(get_skills(req_s))

# 5. ARTS & DESIGN EXPANSION
add_arts_jobs = [
    ("Visual & Graphic Designer", "Ogilvy India", "Mumbai", "Full-time", "₹7 - ₹14 LPA", ["Graphic Design", "Adobe Creative Suite", "Branding"], "1 - 3 Years", "Create digital advertising graphics and visual campaigns.", "https://ogilvy.com"),
    ("UX Researcher & Prototyper", "Swiggy Design", "Bengaluru", "Full-time", "₹11 - ₹20 LPA", ["UX/UI Design", "Figma", "User Research"], "2 - 4 Years", "Conduct user experience interviews and design prototypes.", "https://swiggy.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in add_arts_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    j.required_skills.set(get_skills(req_s))

# 6. ARCHITECTURE EXPANSION
add_arch_jobs = [
    ("Junior Architect", "Morphogenesis Architects", "New Delhi", "Full-time", "₹6 - ₹12 LPA", ["Architectural Design", "AutoCAD", "Revit"], "1 - 3 Years", "Prepare architectural elevation drawings and 3D Revit models.", "https://morphogenesis.org"),
    ("Interior & Sustainable Designer", "Livspace Design Studios", "Bengaluru", "Full-time", "₹7 - ₹13 LPA", ["Interior Arch", "3D Rendering", "Sustainable Arch"], "1 - 3 Years", "Design residential interior layouts and material specifications.", "https://livspace.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in add_arch_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    j.required_skills.set(get_skills(req_s))

# 7. SCIENCE EXPANSION
add_sci_jobs = [
    ("Junior Research Fellow (JRF)", "Indian Institute of Science (IISc)", "Bengaluru", "Full-time", "₹6 - ₹10 LPA", ["Laboratory Techniques", "Research Methodology", "Scientific Writing"], "0 - 2 Years", "Conduct laboratory synthesis and spectroscopic measurements.", "https://iisc.ac.in"),
    ("Bioprocess Analyst", "Syngene Biotech R&D", "Bengaluru", "Full-time", "₹7 - ₹13 LPA", ["Biotechnology", "Microbiology", "Bioprocess Engineering"], "1 - 3 Years", "Operate bioreactors and monitor cell culture growth.", "https://syngeneintl.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in add_sci_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    j.required_skills.set(get_skills(req_s))

print("Seeding Additional Master Items Completed!")
