import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from careers.models import Career, CareerSkillRequirement
from opportunities.models import JobOpportunity, Internship, GovernmentExam, Course, Certification, ProjectIdea
from profiles.models import Degree, Skill

print("Starting Massive Dataset Expansion Across All 8 Domain Clusters...")

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

# ==========================================
# 1. MEDICAL / DENTAL / HEALTHCARE EXPANSION
# ==========================================
medical_degs = ['BDS', 'MBBS', 'NURSING', 'BPHARM', 'DPHARM', 'PHYSIOTHERAPY', 'RADIOLOGY', 'PSYCHOLOGY', 'VETERINARY']

medical_careers = [
    ("Consultant Anesthesiologist", "Anesthesiology", "Administers general, regional, and local anesthesia and manages perioperative patient care.", 18.0, 50.0, ["Anesthesiology", "Airway Management", "Clinical Diagnostics", "Patient Care"]),
    ("Consultant Nephrologist", "Nephrology", "Specializes in kidney diseases, dialysis management, and renal transplants.", 20.0, 55.0, ["Nephrology", "Dialysis Protocols", "Clinical Examination", "Patient Care"]),
    ("Consultant Gastroenterologist", "Gastroenterology", "Diagnoses digestive system diseases, endoscopy, and liver pathology.", 18.0, 52.0, ["Gastroenterology", "Endoscopy & Colonoscopy", "Clinical Diagnostics"]),
    ("Consultant Pulmonologist & Critical Care Specialist", "Pulmonology", "Treats respiratory diseases, lung trauma, and mechanical ventilation.", 16.0, 45.0, ["Pulmonology", "Ventilator Protocols", "ICU Protocols", "Patient Care"]),
    ("Consultant Medical Oncologist", "Oncology", "Specializes in cancer diagnostics, chemotherapy regimens, and immunotherapy.", 22.0, 65.0, ["Oncology", "Chemotherapy Protocols", "Clinical Diagnostics"]),
    ("Consultant Ophthalmologist", "Ophthalmology", "Performs eye surgeries, cataract extractions, LASIK, and treats retinal conditions.", 15.0, 42.0, ["Ophthalmology", "Cataract Surgery", "Clinical Examination"]),
    ("Consultant ENT Surgeon", "Otolaryngology", "Performs ear, nose, throat surgeries, sinus procedures, and head-neck surgeries.", 14.0, 40.0, ["ENT Surgery", "Surgical Techniques", "Clinical Diagnostics"]),
    ("Clinical Microbiologist & Infection Control Specialist", "Clinical Microbiology", "Diagnoses microbial infections, antibiotic sensitivity testing, and hospital infection control.", 9.0, 20.0, ["Clinical Microbiology", "Infection Control", "Laboratory Diagnostics"]),
]

for title, domain, desc, min_s, max_s, skills in medical_careers:
    c, _ = Career.objects.get_or_create(title=title, defaults={'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s})
    link_degrees(c, medical_degs)
    link_skill_reqs(c, skills)

medical_jobs = [
    ("Endodontic Specialist Dentist", "Signature Dental Clinics", "Bengaluru", "Full-time", "₹12 - ₹20 LPA", ["Endodontics", "Root Canal Therapy", "Patient Care"], "2 - 4 Years", "Manage micro-endodontics and complex root canal therapies.", "https://signaturedental.in"),
    ("Senior Clinical Research Physician", "Biocon Clinical R&D", "Bengaluru", "Full-time", "₹14 - ₹24 LPA", ["Clinical Trials", "GCP Compliance", "Pharmacovigilance"], "2 - 5 Years", "Lead Phase II/III oncology and biologic clinical trials.", "https://biocon.com"),
    ("Staff Anesthetist & ICU Specialist", "Narayana Health", "Kolkata / Mysuru", "Full-time", "₹15 - ₹28 LPA", ["Anesthesiology", "ICU Protocols", "Emergency Trauma Care"], "1 - 3 Years", "Manage cardiac surgical anesthesia and ICU monitoring.", "https://narayanahealth.org"),
    ("Senior Oncology Nurse", "Tata Memorial Hospital", "Mumbai", "Full-time", "₹6 - ₹12 LPA", ["Nursing Care", "Chemotherapy Protocols", "Patient Safety"], "2 - 4 Years", "Administer chemotherapy infusions and oncology patient management.", "https://tmc.gov.in"),
    ("Senior Veterinary Medical Officer", "Pet Care Hospitals Chain", "Delhi / Hyderabad", "Full-time", "₹8 - ₹16 LPA", ["Veterinary Surgery", "Animal Diagnostics", "Patient Care"], "1 - 3 Years", "Provide surgical and emergency care for domestic pets.", "https://petcarehospital.in"),
    ("Dialysis Technician & Supervisor", "NephroPlus Kidney Care", "Chennai", "Full-time", "₹5 - ₹10 LPA", ["Dialysis Protocols", "Patient Care", "Clinical Examination"], "1 - 3 Years", "Operate hemodialysis machines and monitor renal patients.", "https://nephroplus.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in medical_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url})
    j.required_skills.set(get_skills(req_s))

medical_internships = [
    ("Maxillofacial Surgery Trainee Intern", "Government Dental College & Hospital", "6 Months", "₹20,000 / month", "Mumbai", ["Oral Surgery", "Surgical Techniques"], "BDS Graduates", "Surgical rotation in facial trauma and oral pathology.", "https://gdchmumbai.org"),
    ("Ophthalmology Optometry Intern", "L V Prasad Eye Institute", "6 Months", "₹18,000 / month", "Hyderabad", ["Ophthalmology", "Clinical Examination"], "MBBS / Optometry Graduates", "Hands-on diagnostic eye examination and cataract screening.", "https://lvpei.org"),
    ("Pediatric Nursing Trainee", "Rainbow Children's Hospital", "6 Months", "₹16,000 / month", "Bengaluru", ["Nursing Care", "Pediatrics"], "Nursing Graduates / Post-Basic", "Clinical care rotations in pediatric and neonatal ICUs.", "https://rainbowhospitals.in"),
]

for title, org, dur, stip, loc, req_s, elig, desc, url in medical_internships:
    i, _ = Internship.objects.get_or_create(title=title, organization=org, defaults={'duration': dur, 'stipend': stip, 'location': loc, 'eligibility': elig, 'description': desc, 'application_url': url})
    i.required_skills.set(get_skills(req_s))

medical_exams = [
    ("USMLE Step 1 & Step 2 CK", "ECFMG / NBME USA", "private", "Medical & Clinical", "MBBS / BDS Graduates", "Anatomy, Physiology, Pathology, Clinical Knowledge, Internal Medicine", "https://ecfmg.org"),
    ("FMGE 2027 (Foreign Medical Graduate Exam)", "National Board of Examinations (NBE)", "govt", "Medical", "Primary Medical Degree from Outside India", "Anatomy, Pathology, Pharmacology, General Medicine, Surgery, Obstetrics", "https://nbe.edu.in"),
    ("AIIMS Super Speciality (INI-SS) 2027", "AIIMS New Delhi", "govt", "Medical & Surgical", "MD / MS / MDS Degree", "Advanced Cardiology, Neurology, Gastroenterology, Surgical Specialities", "https://aiimsexams.ac.in"),
    ("UPSC Combined Medical Services (CMS) 2027", "UPSC", "govt", "Government Medical Officer", "MBBS Degree", "General Medicine, Pediatrics, Surgery, Preventive & Social Medicine", "https://upsc.gov.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in medical_exams:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url})

medical_courses = [
    ("Masterclass in Endodontics & Microscopic Root Canal", "Udemy", "Advanced", "Endodontics", "Comprehensive video course covering rotary endodontics, rubber dam isolation, and warm vertical compaction.", "https://udemy.com"),
    ("Clinical Cardiology & ECG Interpretation", "Coursera", "Intermediate", "Cardiology", "Learn 12-lead ECG interpretation, arrhythmia diagnosis, and acute cardiac care.", "https://coursera.org"),
    ("Good Clinical Practice (GCP) & Clinical Trial Regulations", "NPTEL", "Beginner", "Clinical Research", "Official NPTEL certification on ethics, ICH-GCP guidelines, and regulatory filings.", "https://nptel.ac.in"),
]

for title, prov, diff, sname, desc, url in medical_courses:
    s, _ = Skill.objects.get_or_create(name=sname)
    Course.objects.get_or_create(title=title, defaults={'provider': prov, 'difficulty': diff, 'skill': s, 'description': desc, 'url': url})


# ==========================================
# 2. COMMERCE / FINANCE / CA EXPANSION
# ==========================================
commerce_degs = ['BCOM', 'MCOM', 'BBA', 'MBA', 'BMS', 'CA']

commerce_careers = [
    ("Corporate Treasurer & Liquidity Manager", "Corporate Treasury", "Manages corporate liquidity, FX hedging, cash forecasts, and bank relationships.", 14.0, 32.0, ["Corporate Finance & Valuation", "Financial Markets", "Financial Modeling & Excel"]),
    ("Wealth Management Consultant", "Private Wealth", "Advises high-net-worth clients on asset allocation, portfolio management, and estate planning.", 10.0, 25.0, ["Financial Markets", "Portfolio Management", "Financial Modeling & Excel"]),
    ("Cost Accountant (CMA)", "Cost & Management Accounting", "Conducts product cost analysis, budgetary control, operational auditing, and pricing strategies.", 8.0, 20.0, ["Cost Accounting", "Accounting Standards", "Statutory Audit"]),
    ("Risk & Compliance Officer", "Financial Compliance", "Ensures compliance with RBI, SEBI, AML regulations, and corporate financial ethics.", 9.0, 22.0, ["Corporate Governance", "Statutory Audit", "Financial Markets"]),
]

for title, domain, desc, min_s, max_s, skills in commerce_careers:
    c, _ = Career.objects.get_or_create(title=title, defaults={'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s})
    link_degrees(c, commerce_degs)
    link_skill_reqs(c, skills)

commerce_jobs = [
    ("Senior Portfolio Analyst", "Barclays Wealth India", "Mumbai", "Full-time", "₹14 - ₹24 LPA", ["Financial Markets", "Portfolio Management", "Financial Modeling & Excel"], "2 - 5 Years", "Analyze asset allocation and deliver private wealth solutions.", "https://barclays.com"),
    ("Corporate Tax Manager", "PwC India", "Bengaluru / Gurgaon", "Full-time", "₹12 - ₹22 LPA", ["Income Tax Filing", "GST Compliance", "Taxation"], "2 - 5 Years", "Advise international corporations on transfer pricing and tax litigation.", "https://pwc.in"),
    ("Credit Risk Analyst", "HDFC Bank Corporate", "Mumbai", "Full-time", "₹10 - ₹18 LPA", ["Financial Modeling & Excel", "Corporate Finance & Valuation", "Banking"], "1 - 4 Years", "Evaluate corporate credit underwriting and commercial loan proposals.", "https://hdfcbank.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in commerce_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url})
    j.required_skills.set(get_skills(req_s))

commerce_exams = [
    ("CMA Final Exam 2027", "ICMAI (Institute of Cost Accountants of India)", "govt", "Cost Accounting & Finance", "CMA Intermediate Passed", "Advanced Financial Management, Strategic Performance Management, Corporate Taxation, Cost Audit", "https://icmai.in"),
    ("CS Professional Exam 2027", "ICSI (Institute of Company Secretaries of India)", "govt", "Corporate Governance & Law", "CS Executive Passed", "Governance, Risk Management, Drafting, Secretarial Audit, Corporate Restructuring", "https://icsi.edu"),
    ("RBI Grade B Officer 2027", "Reserve Bank of India", "govt", "Central Banking & Finance", "Bachelor Degree (BCom / BBA / MBA / CA) with 60%+", "Economics & Social Issues, Financial Management, Quantitative Aptitude, General Awareness", "https://rbi.org.in"),
    ("SEBI Grade A Officer (General / Finance) 2027", "SEBI", "govt", "Financial Markets & Regulation", "Degree in Commerce / Finance / CA / MBA Finance", "Financial Capital Markets, Corporate Accounting, Costing, Companies Act, Economics", "https://sebi.gov.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in commerce_exams:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url})

commerce_courses = [
    ("Financial Modeling & Valuation Masterclass", "Coursera", "Advanced", "Financial Modeling & Excel", "Learn DCF valuation, LBO models, M&A pitchbooks, and Three-Statement financial modeling.", "https://coursera.org"),
    ("Complete Direct & Indirect GST Taxation", "Udemy", "Intermediate", "GST Compliance", "Practical GST return filing (GSTR-1, GSTR-3B, GSTR-9), TDS/TCS, and corporate tax advisory.", "https://udemy.com"),
]

for title, prov, diff, sname, desc, url in commerce_courses:
    s, _ = Skill.objects.get_or_create(name=sname)
    Course.objects.get_or_create(title=title, defaults={'provider': prov, 'difficulty': diff, 'skill': s, 'description': desc, 'url': url})


# ==========================================
# 3. LEGAL / LAW EXPANSION
# ==========================================
legal_degs = ['LLB', 'BALLB', 'BBALLB', 'LLM']

legal_careers = [
    ("Judicial Magistrate / District Judge", "Judiciary", "Presides over civil and criminal court trials, legal adjudications, and court judgments.", 12.0, 35.0, ["Court Litigation", "Civil & Criminal Law", "Constitutional Law", "Legal Drafting"]),
    ("Commercial Arbitrator & Mediator", "Arbitration", "Resolves corporate and commercial disputes out of court through binding arbitration.", 12.0, 30.0, ["Commercial Arbitration", "Contract Law", "Legal Drafting"]),
    ("Environmental Law Specialist", "Environmental Law", "Handles environmental compliance, NGT petitions, climate regulations, and ESG law.", 8.0, 20.0, ["Environmental Law", "Litigation", "Legal Drafting"]),
]

for title, domain, desc, min_s, max_s, skills in legal_careers:
    c, _ = Career.objects.get_or_create(title=title, defaults={'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s})
    link_degrees(c, legal_degs)
    link_skill_reqs(c, skills)

legal_jobs = [
    ("Corporate Contracts Counsel", "Tech Mahindra Legal", "Pune / Remote", "Full-time", "₹11 - ₹20 LPA", ["Corporate Law", "Contract Law", "Legal Drafting"], "2 - 4 Years", "Negotiate international software licenses and vendor contracts.", "https://techmahindra.com"),
    ("IP & Patent Associate", "Remfry & Sagar", "Gurgaon", "Full-time", "₹12 - ₹22 LPA", ["Intellectual Property Rights", "Patent Drafting", "Legal Drafting"], "2 - 4 Years", "Draft patent claims and represent clients in trademark oppositions.", "https://remfry.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in legal_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url})
    j.required_skills.set(get_skills(req_s))

legal_exams = [
    ("CLAT-PG 2027 (Common Law Admission Test for LLM)", "Consortium of NLUs", "govt", "Legal", "LLB / BA LLB Degree", "Constitutional Law, Jurisprudence, Criminal Law, Contract Law, Cyber Law, IPR", "https://consortiumofnlus.ac.in"),
    ("SEBI Officer Grade A (Legal)", "SEBI", "govt", "Legal & Regulatory", "Bachelor Degree in Law (LLB / BA LLB)", "Constitution of India, Law of Contracts, Companies Act, Criminal Law, Administrative Law", "https://sebi.gov.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in legal_exams:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url})


# ==========================================
# 4. AGRICULTURE & ALLIED EXPANSION
# ==========================================
agri_degs = ['AGRI', 'SERICULTURE', 'HORTICULTURE', 'VETERINARY']

agri_careers = [
    ("Plant Breeder & Geneticist", "Plant Genetics", "Develops disease-resistant, high-yield crop hybrids and seed genetic varieties.", 7.0, 18.0, ["Plant Breeding", "Seed Tech", "Agronomy"]),
    ("Farm Automation & Drone Specialist", "Agri Tech", "Deploys agricultural spraying drones, IoT soil sensors, and automated irrigation.", 7.0, 16.0, ["Precision Farming", "Agribusiness", "Soil Science"]),
]

for title, domain, desc, min_s, max_s, skills in agri_careers:
    c, _ = Career.objects.get_or_create(title=title, defaults={'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s})
    link_degrees(c, agri_degs)
    link_skill_reqs(c, skills)

agri_jobs = [
    ("Agri Drone & Precision Tech Manager", "DeHaat Agri Services", "Gurgaon / Field", "Full-time", "₹8 - ₹15 LPA", ["Precision Farming", "Agronomy", "Agribusiness"], "1 - 3 Years", "Manage IoT smart farming installations and field advisor networks.", "https://agridex.com"),
    ("Seed Breeding Manager", "Nuziveedu Seeds", "Hyderabad", "Full-time", "₹8 - ₹16 LPA", ["Plant Breeding", "Seed Tech", "Agronomy"], "2 - 4 Years", "Direct cotton and hybrid corn plant breeding projects.", "https://nuziveeduseeds.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in agri_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url})
    j.required_skills.set(get_skills(req_s))

agri_exams = [
    ("IBPS AFO (Agricultural Field Officer) 2027", "IBPS", "govt", "Agri Banking", "Degree in Agriculture / Horticulture / Sericulture / Vet Science / Forestry", "Agriculture Knowledge, Seed Tech, Agronomy, Soil Science, Animal Husbandry", "https://ibps.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in agri_exams:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url})


# ==========================================
# 5. ARTS, MEDIA & DESIGN EXPANSION
# ==========================================
arts_degs = ['BA', 'MA', 'BFA', 'BJMC', 'BDES']

arts_careers = [
    ("Creative Director & Brand Strategist", "Brand Advertising", "Leads integrated brand campaigns, art direction, and visual storytelling.", 10.0, 26.0, ["Branding", "Graphic Design", "Typography"]),
    ("Motion Graphics Artist & Animator", "Animation & VFX", "Creates 2D/3D motion graphics, visual effects, and animated digital media.", 7.0, 18.0, ["Adobe Creative Suite", "UX/UI Design", "Prototyping"]),
]

for title, domain, desc, min_s, max_s, skills in arts_careers:
    c, _ = Career.objects.get_or_create(title=title, defaults={'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s})
    link_degrees(c, arts_degs)
    link_skill_reqs(c, skills)

arts_jobs = [
    ("Senior Motion Designer", "Hotstar Visual Studios", "Mumbai", "Full-time", "₹10 - ₹18 LPA", ["Adobe Creative Suite", "Graphic Design", "UX/UI Design"], "2 - 4 Years", "Create broadcast graphics and promotional video animations.", "https://hotstar.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in arts_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url})
    j.required_skills.set(get_skills(req_s))

arts_exams = [
    ("NIFT PG Master of Design / Fashion 2027", "National Institute of Fashion Technology", "govt", "Design", "Bachelor Degree (BDES / BFA / BA / BArch)", "Creative Ability Test (CAT), General Ability Test (GAT), Portfolio & Interview", "https://nift.ac.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in arts_exams:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url})


# ==========================================
# 6. ARCHITECTURE & INTERIOR EXPANSION
# ==========================================
arch_degs = ['BARCH', 'MARCH']

arch_careers = [
    ("Landscape Architect & Environmental Planner", "Landscape Arch", "Designs outdoor urban spaces, ecological parks, and green infrastructure.", 8.0, 20.0, ["Architectural Design", "Landscape", "AutoCAD"]),
]

for title, domain, desc, min_s, max_s, skills in arch_careers:
    c, _ = Career.objects.get_or_create(title=title, defaults={'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s})
    link_degrees(c, arch_degs)
    link_skill_reqs(c, skills)

arch_jobs = [
    ("Senior Landscape Architect", "Atkins Realis India", "Bengaluru", "Full-time", "₹10 - ₹18 LPA", ["Architectural Design", "Landscape", "Revit"], "2 - 5 Years", "Design sustainable urban waterfronts and commercial landscape projects.", "https://atkinsrealis.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in arch_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url})
    j.required_skills.set(get_skills(req_s))

arch_exams = [
    ("CEPT Master of Architecture / Planning 2027", "CEPT University", "private", "Architecture & Planning", "BArch Degree", "Architectural Aptitude, Spatial Reasoning, Design Portfolio Review", "https://cept.ac.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in arch_exams:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url})


# ==========================================
# 7. PURE SCIENCES & BIOTECH EXPANSION
# ==========================================
sci_degs = ['BSC', 'MSC']

sci_careers = [
    ("Bioinformatician & Computational Biologist", "Bioinformatics", "Analyzes genomic sequencing data, protein structures, and biological pipelines.", 8.0, 22.0, ["Biotechnology", "Data Analysis", "Research Methodology"]),
]

for title, domain, desc, min_s, max_s, skills in sci_careers:
    c, _ = Career.objects.get_or_create(title=title, defaults={'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s})
    link_degrees(c, sci_degs)
    link_skill_reqs(c, skills)

sci_jobs = [
    ("Genomic Bioinformatician", "Strand Life Sciences", "Bengaluru", "Full-time", "₹9 - ₹17 LPA", ["Biotechnology", "Data Analysis", "Laboratory Techniques"], "1 - 3 Years", "Perform NGS genomic variant analysis and clinical reporting.", "https://strandls.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in sci_jobs:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url})
    j.required_skills.set(get_skills(req_s))

sci_exams = [
    ("GATE Biotechnology 2027", "IIT / GATE Committee", "govt", "Biotechnology & Science", "BSc / MSc Biotechnology / BTech Biotech", "Biochemistry, Microbiology, Cell Biology, Molecular Biology, Recombinant DNA", "https://gate.iitk.ac.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in sci_exams:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url})

print("Massive Expansion Completed Successfully!")
