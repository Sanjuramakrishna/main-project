import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from careers.models import Career, CareerSkillRequirement
from opportunities.models import JobOpportunity, Internship, GovernmentExam, Course
from profiles.models import Degree, Skill

print("Starting Master Seeder for 50 Domain-Isolated Items across All Clusters...")

# Helper to get or create skills
def get_skills(skill_names):
    skills = []
    for name in skill_names:
        s, _ = Skill.objects.get_or_create(name=name.strip())
        skills.append(s)
    return skills

# Helper to link degrees
def link_degrees(career, degree_codes):
    for code in degree_codes:
        degs = Degree.objects.filter(code__iexact=code)
        if degs.exists():
            for d in degs:
                career.eligible_degrees.add(d)

# Helper to add skill requirements
def link_skill_reqs(career, skill_names):
    for idx, sname in enumerate(skill_names):
        s, _ = Skill.objects.get_or_create(name=sname.strip())
        importance = 'essential' if idx < 3 else 'recommended'
        CareerSkillRequirement.objects.get_or_create(career=career, skill=s, defaults={'importance': importance})

# --- 1. MEDICAL / DENTAL / HEALTHCARE SEEDER ---
medical_degrees = ['BDS', 'MBBS', 'NURSING', 'BPHARM', 'DPHARM', 'PHYSIOTHERAPY', 'RADIOLOGY', 'PSYCHOLOGY', 'VETERINARY']

medical_careers_data = [
    ("General Dental Practitioner", "Dental Care", "Provides comprehensive primary oral health care, diagnostics, and dental restorations.", 9.0, 18.0, ["Clinical Examination", "Dental Radiology", "Restorative Dentistry", "Patient Management"]),
    ("Cosmetic Dentist & Smile Specialist", "Cosmetic Dentistry", "Specializes in smile design, teeth whitening, veneers, and aesthetic dental procedures.", 12.0, 28.0, ["Cosmetic Dentistry", "Veneers & Whitening", "Digital Smile Design", "Patient Care"]),
    ("Orthodontist & Dentofacial Specialist", "Orthodontics", "Diagnoses and treats dental and facial irregularities using braces and clear aligners.", 14.0, 32.0, ["Orthodontics", "Cephalometric Analysis", "Aligners & Braces", "Patient Diagnostics"]),
    ("Oral & Maxillofacial Surgeon", "Oral Surgery", "Performs surgical procedures on jawbone, face, tooth extractions, and trauma reconstruction.", 16.0, 45.0, ["Oral Surgery", "Surgical Techniques", "Anatomy", "Emergency Trauma Care"]),
    ("Periodontist & Implantologist", "Periodontics", "Treats gum diseases, periodontal surgery, and places dental implants.", 12.0, 30.0, ["Periodontics", "Dental Implantology", "Gum Surgery", "Clinical Diagnostics"]),
    ("Endodontist & Root Canal Specialist", "Endodontics", "Performs root canal treatments, apicoectomies, and dental pulp therapy.", 12.0, 28.0, ["Endodontics", "Root Canal Therapy", "Micro-endodontics", "Pain Management"]),
    ("Pediatric Dentist (Pedodontist)", "Pediatric Dentistry", "Provides specialized oral healthcare for children, infants, and adolescents.", 10.0, 24.0, ["Pediatric Dentistry", "Child Behavior Guidance", "Preventive Dentistry", "Patient Care"]),
    ("Oral Pathologist & Radiologist", "Oral Diagnostics", "Diagnoses oral diseases, biopsies, and interprets dental X-rays & CBCT scans.", 10.0, 22.0, ["Oral Pathology", "Dental Radiology", "Biopsy & Histology", "Clinical Diagnostics"]),
    ("Dental Public Health Officer", "Public Health", "Manages community oral health initiatives, dental epidemiology, and government programs.", 8.0, 18.0, ["Epidemiology", "Public Health", "Community Dentistry", "Health Administration"]),
    ("Chief Medical Officer (CMO)", "Hospital Admin", "Directs clinical operations, hospital policy, and healthcare quality standards.", 18.0, 50.0, ["Hospital Administration", "Clinical Leadership", "Healthcare Policy", "Patient Safety"]),
    ("Consultant Cardiologist", "Cardiology", "Specializes in diagnosing and treating heart conditions, ECG, and angioplasty.", 20.0, 60.0, ["Cardiology", "ECG & Echo", "Clinical Diagnostics", "Patient Care"]),
    ("Consultant Neurologist", "Neurology", "Diagnoses brain, spinal cord, and nerve disorders.", 18.0, 55.0, ["Neurology", "EEG & MRI Interpretation", "Clinical Examination", "Neuro Diagnostics"]),
    ("Consultant Surgeon", "General Surgery", "Performs general, laparoscopic, and emergency surgical interventions.", 16.0, 48.0, ["Surgical Techniques", "Laparoscopy", "Anatomy", "Emergency Trauma Care"]),
    ("Consultant Pediatrician", "Pediatrics", "Provides medical care for infants, children, and immunization programs.", 12.0, 30.0, ["Pediatrics", "Child Health", "Immunization", "Clinical Diagnostics"]),
    ("Consultant Dermatologist", "Dermatology", "Treats skin conditions, cosmetic dermatology, and laser therapies.", 15.0, 40.0, ["Dermatology", "Cosmetic Dermatology", "Laser Therapy", "Clinical Diagnostics"]),
    ("Clinical Pharmacologist & Pharmacovigilance Specialist", "Pharmacology", "Monitors drug safety, clinical trials, and adverse drug reactions.", 8.0, 20.0, ["Pharmacovigilance", "Drug Safety", "Clinical Trials", "Regulatory Affairs"]),
    ("Senior Clinical Research Associate (CRA)", "Clinical Research", "Manages multi-center clinical trials and regulatory compliance.", 9.0, 22.0, ["Clinical Research", "GCP Compliance", "Clinical Trials", "Regulatory Affairs"]),
    ("Nursing Superintendent & Clinical Manager", "Nursing", "Directs hospital nursing care, patient care standards, and ICU protocols.", 7.0, 16.0, ["Nursing Care", "Patient Management", "ICU Protocols", "Emergency Nursing"]),
    ("Consultant Physiotherapist & Rehab Specialist", "Physiotherapy", "Provides orthopaedic, sports, and neurological physical rehabilitation.", 6.0, 18.0, ["Physiotherapy", "Musculoskeletal Rehab", "Sports Injury Care", "Pain Management"]),
    ("Consultant Radiologist", "Medical Imaging", "Interprets X-rays, CT scans, MRI, and ultrasound imaging.", 15.0, 42.0, ["Medical Imaging", "CT & MRI Interpretation", "Radiology", "Clinical Diagnostics"]),
    ("Clinical Psychologist", "Mental Health", "Provides psychotherapeutic assessment, cognitive behavioral therapy, and counseling.", 7.0, 18.0, ["Clinical Psychology", "Psychotherapy", "CBT", "Mental Health Assessment"]),
    ("Veterinary Surgeon & Public Health Officer", "Veterinary Medicine", "Provides surgical and medical treatment for livestock and domestic animals.", 8.0, 20.0, ["Veterinary Surgery", "Animal Diagnostics", "Veterinary Pharmacology", "Public Health"]),
]

for title, domain, desc, min_s, max_s, skills in medical_careers_data:
    c, created = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    link_degrees(c, medical_degrees)
    link_skill_reqs(c, skills)

# Seed Medical Jobs
medical_jobs_data = [
    ("Senior Dental Surgeon", "Apollo Dental Clinics", "Bengaluru", "Full-time", "₹10 - ₹18 LPA", ["Clinical Examination", "Dental Radiology", "Restorative Dentistry"], "2 - 5 Years", "Conduct root canals, crown placements, and general dental consultations.", "https://apollodental.in/careers"),
    ("Associate Dentist & Endodontist", "Clove Dental Care", "Mumbai / Delhi / Pune", "Full-time", "₹8 - ₹15 LPA", ["Endodontics", "Root Canal Therapy", "Patient Care"], "1 - 3 Years", "Perform root canal treatments and general dental procedures.", "https://clovedental.in/careers"),
    ("Clinical Research Physician / CRA", "IQVIA India", "Hyderabad / Remote", "Full-time", "₹9 - ₹16 LPA", ["Clinical Trials", "GCP Compliance", "Pharmacovigilance"], "1 - 4 Years", "Monitor clinical trials and ensure regulatory compliance.", "https://iqvia.com/careers"),
    ("Resident Medical Officer (RMO)", "Fortis Healthcare", "Chennai / Delhi", "Full-time", "₹12 - ₹22 LPA", ["Clinical Diagnostics", "Emergency Trauma Care", "Patient Care"], "1 - 3 Years", "Manage inpatient clinical care and emergency triage.", "https://fortishealthcare.com/careers"),
    ("Head Nurse & ICU Specialist", "Max Super Speciality Hospital", "Delhi NCR", "Full-time", "₹6 - ₹12 LPA", ["Nursing Care", "ICU Protocols", "Patient Management"], "2 - 5 Years", "Oversee ICU patient care and supervise nursing staff.", "https://maxhealthcare.in/careers"),
    ("Senior Pharmacovigilance Safety Officer", "Novartis Healthcare", "Hyderabad", "Full-time", "₹8 - ₹14 LPA", ["Pharmacovigilance", "Drug Safety", "Regulatory Affairs"], "2 - 4 Years", "Analyze adverse event reports and safety data.", "https://novartis.com/careers"),
    ("Senior Physiotherapist", "Manipal Hospitals", "Bengaluru", "Full-time", "₹7 - ₹13 LPA", ["Physiotherapy", "Musculoskeletal Rehab", "Pain Management"], "2 - 4 Years", "Deliver post-operative and orthopaedic rehabilitation.", "https://manipalhospitals.com/careers"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in medical_jobs_data:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    j.required_skills.set(s_objs)

# Seed Medical Internships
medical_internships_data = [
    ("Junior Dental Intern / Clinical Observer", "Manipal College of Dental Sciences", "6 Months", "₹18,000 / month", "Manipal / Mangalore", ["Clinical Examination", "Dental Radiology"], "BDS Graduates / Final Year", "Hands-on clinical rotations across oral surgery, endodontics, and periodontics.", "https://manipal.edu/mcods"),
    ("Clinical Research Intern", "Syngene International", "6 Months", "₹20,000 / month", "Bengaluru", ["Clinical Trials", "Pharmacovigilance"], "MBBS / BDS / BPharm / MPharm", "Assist clinical trial monitoring and documentation.", "https://syngeneintl.com"),
    ("Dental Assistant & Smile Design Intern", "Sabka Dentist Clinics", "3 Months", "₹15,000 / month", "Mumbai", ["Cosmetic Dentistry", "Patient Care"], "BDS Final Year / Interns", "Assist senior cosmetic dentists in patient management.", "https://sabkadentist.com"),
    ("Pharmacovigilance Trainee Intern", "Dr. Reddy's Laboratories", "6 Months", "₹22,000 / month", "Hyderabad", ["Drug Safety", "Pharmacovigilance"], "BPharm / PharmD / BDS", "Review safety signals and adverse drug reactions.", "https://drreddys.com"),
]

for title, org, dur, stip, loc, req_s, elig, desc, url in medical_internships_data:
    i, _ = Internship.objects.get_or_create(title=title, organization=org, defaults={
        'duration': dur, 'stipend': stip, 'location': loc, 'eligibility': elig, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    i.required_skills.set(s_objs)

# Seed Medical Exams
medical_exams_data = [
    ("NEET-MDS 2027", "National Board of Examinations (NBE)", "govt", "Medical & Dental", "BDS Degree from recognized dental college", "Complete BDS Syllabus: Oral Surgery, Endodontics, Periodontics, Orthodontics, Pathology", "https://nbe.edu.in"),
    ("INI-CET Dental & Medical 2027", "AIIMS New Delhi", "govt", "Medical & Dental", "MBBS / BDS Degree with 1-Year Internship", "Clinical Medicine, Dentistry, Pathology, Pharmacology, Surgery", "https://aiimsexams.ac.in"),
    ("NEET-PG 2027", "National Board of Examinations (NBE)", "govt", "Medical & Healthcare", "MBBS Degree with completed internship", "General Medicine, Surgery, Pediatrics, Gynaecology, Pathology, Anatomy", "https://nbe.edu.in"),
    ("GPAT 2027 (Graduate Pharmacy Aptitude Test)", "NTA / NBEMS", "govt", "Pharmacy & Medical", "BPharm Degree", "Pharmaceutics, Pharmacology, Pharmaceutical Chemistry, Analysis", "https://gpat.nta.nic.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in medical_exams_data:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={
        'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url
    })


# --- 2. COMMERCE / MANAGEMENT / CA SEEDER ---
commerce_degrees = ['BCOM', 'MCOM', 'BBA', 'MBA', 'BMS', 'CA']

commerce_careers_data = [
    ("Investment Banking Analyst", "Investment Banking", "Conducts financial modeling, business valuation, M&A pitchbooks, and deal execution.", 12.0, 28.0, ["Financial Modeling & Excel", "Corporate Finance & Valuation", "Financial Markets"]),
    ("Chartered Accountant & Audit Manager", "Accounting & Audit", "Manages statutory audits, tax compliance, GST returns, and corporate accounting.", 9.0, 22.0, ["Accounting Standards", "GST Compliance", "Statutory Audit", "Income Tax Filing"]),
    ("Equity Research Analyst", "Capital Markets", "Analyzes stock market data, equity reports, company balance sheets, and valuations.", 10.0, 24.0, ["Financial Markets", "Financial Modeling & Excel", "Corporate Finance & Valuation"]),
    ("Taxation Manager & Consultant", "Corporate Taxation", "Provides corporate income tax advisory, GST filing, and international transfer pricing.", 8.0, 20.0, ["Income Tax Filing", "GST Compliance", "Taxation"]),
    ("Financial Controller & CFO", "Corporate Finance", "Directs corporate financial strategy, cash flow management, budgeting, and risk assessment.", 20.0, 60.0, ["Corporate Finance & Valuation", "Accounting Standards", "Financial Modeling & Excel"]),
    ("Corporate Financial Analyst", "Financial Analytics", "Analyzes corporate budget variance, profitability metrics, and financial reporting.", 7.0, 16.0, ["Financial Modeling & Excel", "Corporate Finance & Valuation", "Accounting Standards"]),
    ("Risk & Internal Audit Specialist", "Internal Audit", "Evaluates internal accounting controls, enterprise risk management, and compliance.", 8.0, 18.0, ["Statutory Audit", "Internal Audit", "Corporate Governance"]),
]

for title, domain, desc, min_s, max_s, skills in commerce_careers_data:
    c, created = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    link_degrees(c, commerce_degrees)
    link_skill_reqs(c, skills)

commerce_jobs_data = [
    ("Investment Banking Associate", "Goldman Sachs India", "Bengaluru", "Full-time", "₹18 - ₹32 LPA", ["Financial Modeling & Excel", "Corporate Finance & Valuation"], "2 - 5 Years", "Build financial valuation models for corporate mergers and acquisitions.", "https://goldmansachs.com/careers"),
    ("Statutory Audit Senior", "Deloitte India", "Mumbai / Gurgaon", "Full-time", "₹10 - ₹18 LPA", ["Accounting Standards", "Statutory Audit", "GST Compliance"], "2 - 4 Years", "Lead statutory audit engagements for listed corporate clients.", "https://deloitte.com/careers"),
    ("Equity Analyst", "HDFC Securities", "Mumbai", "Full-time", "₹12 - ₹20 LPA", ["Financial Markets", "Financial Modeling & Excel"], "1 - 3 Years", "Prepare equity research coverage reports on banking and IT sectors.", "https://hdfcsec.com/careers"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in commerce_jobs_data:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    j.required_skills.set(s_objs)

commerce_exams_data = [
    ("CA Final Exam 2027", "ICAI (Institute of Chartered Accountants of India)", "govt", "Commerce & Finance", "CA Intermediate Passed", "Advanced Financial Reporting, Strategic Financial Management, Advanced Auditing, Direct & Indirect Tax Laws", "https://icai.org"),
    ("CFA Level 1 Exam", "CFA Institute", "private", "Finance & Investment", "Bachelor Degree (BCom / BBA / MBA / CA)", "Ethical & Professional Standards, Quantitative Methods, Economics, Financial Statement Analysis", "https://cfainstitute.org"),
    ("IBPS PO 2027", "Institute of Banking Personnel Selection", "govt", "Banking & Finance", "Any Bachelor Degree (BCom / BBA / BA / BSc / BTech)", "Quantitative Aptitude, Reasoning, Banking Awareness, Financial Literacy", "https://ibps.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in commerce_exams_data:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={
        'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url
    })


# --- 3. LEGAL / LAW SEEDER ---
legal_degrees = ['LLB', 'BALLB', 'BBALLB', 'LLM']

legal_careers_data = [
    ("Corporate Legal Counsel", "Corporate Law", "Advises corporations on legal compliance, commercial contracts, M&A, and corporate governance.", 10.0, 26.0, ["Corporate Law", "Contract Law", "Legal Drafting", "Commercial Arbitration"]),
    ("Cyber & Technology Lawyer", "Cyber Law", "Specializes in data privacy laws, IT Act compliance, cybersecurity regulations, and digital IP.", 9.0, 22.0, ["Cyber Law", "Data Privacy & GDPR", "Intellectual Property Rights", "Legal Drafting"]),
    ("Litigation Advocate", "Court Litigation", "Represents clients in High Courts, Civil Courts, and Supreme Court for civil and criminal litigation.", 8.0, 30.0, ["Court Litigation", "Civil & Criminal Law", "Legal Drafting", "Constitutional Law"]),
    ("Intellectual Property (IP) Attorney", "IPR Law", "Handles patent drafting, trademark filings, copyright protection, and IP litigation.", 10.0, 24.0, ["Intellectual Property Rights", "Patent Drafting", "Trademark Law", "Legal Drafting"]),
]

for title, domain, desc, min_s, max_s, skills in legal_careers_data:
    c, created = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    link_degrees(c, legal_degrees)
    link_skill_reqs(c, skills)

legal_jobs_data = [
    ("Senior Legal Associate", "Khaitan & Co", "Mumbai / New Delhi", "Full-time", "₹15 - ₹28 LPA", ["Corporate Law", "Contract Law", "Legal Drafting"], "2 - 4 Years", "Draft commercial agreements and manage corporate M&A transactions.", "https://khaitanco.com/careers"),
    ("Cyber Law Specialist", "Shardul Amarchand Mangaldas", "Bengaluru", "Full-time", "₹14 - ₹25 LPA", ["Cyber Law", "Data Privacy & GDPR", "Legal Drafting"], "2 - 5 Years", "Provide legal advisory on technology contracts and GDPR compliance.", "https://amsshardul.com/careers"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in legal_jobs_data:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    j.required_skills.set(s_objs)

legal_exams_data = [
    ("AIBE 2027 (All India Bar Examination)", "Bar Council of India (BCI)", "govt", "Legal", "Law Graduate (LLB / BA LLB)", "Constitutional Law, IPC, CPC, CrPC, Evidence Act, Contract Law, Cyber Law", "https://allindiabarexamination.com"),
    ("Judicial Services Exam 2027", "State High Courts & Public Service Commission", "govt", "Legal & Judiciary", "LLB / BA LLB Degree", "Civil Law, Criminal Law, Constitutional Law, Local Laws, Judgment Writing", "https://hc.gov.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in legal_exams_data:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={
        'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url
    })


# --- 4. AGRICULTURE / HORTICULTURE / SERICULTURE SEEDER ---
agri_degrees = ['AGRI', 'SERICULTURE', 'HORTICULTURE', 'VETERINARY']

agri_careers_data = [
    ("Agronomist & Precision Farming Specialist", "Agronomy", "Optimizes crop yield, soil fertility, irrigation, and precision agriculture technology.", 6.0, 16.0, ["Agronomy", "Soil Science", "Crop Protection", "Precision Farming"]),
    ("Horticulture Officer & Greenhouse Specialist", "Horticulture", "Manages commercial fruit and vegetable cultivation, floriculture, and protected greenhouses.", 6.0, 15.0, ["Horticulture", "Plant Breeding", "Greenhouse Tech", "Soil Science"]),
    ("Sericulture Specialist & Silk Tech Officer", "Sericulture", "Oversees mulberry cultivation, silkworm rearing, silk reeling, and sericulture technology.", 5.5, 14.0, ["Sericulture", "Mulberry Cultivation", "Silkworm Rearing", "Silk Reeling"]),
    ("Agribusiness Manager", "Agribusiness", "Manages agricultural supply chain, farm inputs, grain trading, and agri-commodity sales.", 7.0, 18.0, ["Agribusiness", "Agricultural Marketing", "Supply Chain", "Soil Science"]),
]

for title, domain, desc, min_s, max_s, skills in agri_careers_data:
    c, created = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    link_degrees(c, agri_degrees)
    link_skill_reqs(c, skills)

agri_jobs_data = [
    ("Senior Agronomist", "ITC Agri Business", "Hyderabad / Field", "Full-time", "₹8 - ₹14 LPA", ["Agronomist", "Soil Science", "Crop Protection"], "2 - 4 Years", "Guide farmers on sustainable farming practices and crop yield optimization.", "https://itcportal.com/careers"),
    ("Horticulture Manager", "Mahindra Agri Solutions", "Pune / Nashik", "Full-time", "₹7 - ₹13 LPA", ["Horticulture", "Plant Breeding", "Greenhouse Tech"], "1 - 3 Years", "Oversee protected cultivation and high-tech greenhouse operations.", "https://mahindraagri.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in agri_jobs_data:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    j.required_skills.set(s_objs)

agri_exams_data = [
    ("ICAR AIEEA PG 2027", "Indian Council of Agricultural Research (ICAR) / NTA", "govt", "Agriculture & Allied", "BSc Agriculture / Horticulture / Sericulture", "Agronomy, Plant Breeding, Soil Science, Horticulture, Entomology", "https://icar.nta.nic.in"),
    ("NABARD Grade A Officer 2027", "NABARD", "govt", "Agri & Rural Development", "Degree in Agriculture / Forestry / Sericulture / Horticulture / Vet Science", "Rural Economy, Agriculture & Rural Development, General Awareness", "https://nabard.org"),
]

for exam_name, body, cat, dom, elig, syllabus, url in agri_exams_data:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={
        'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url
    })


# --- 5. ARTS / MEDIA / DESIGN / FINE ARTS SEEDER ---
arts_degrees = ['BA', 'MA', 'BFA', 'BJMC', 'BDES']

arts_careers_data = [
    ("Senior UX/UI & Product Designer", "Digital Design", "Designs user interfaces, wireframes, user research, and mobile/web experience.", 8.0, 22.0, ["UX/UI Design", "Figma", "User Research", "Prototyping"]),
    ("Digital Journalist & Investigative Reporter", "Media & Journalism", "Produces investigative news reports, digital journalism, and broadcast media content.", 6.0, 16.0, ["Journalism", "Digital Media", "Content Creation", "Editing"]),
    ("Creative Art Director & Graphic Designer", "Fine Arts & Design", "Directs visual branding, graphic design, typography, and creative campaigns.", 7.0, 18.0, ["Graphic Design", "Typography", "Adobe Creative Suite", "Branding"]),
]

for title, domain, desc, min_s, max_s, skills in arts_careers_data:
    c, created = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    link_degrees(c, arts_degrees)
    link_skill_reqs(c, skills)

arts_jobs_data = [
    ("Lead UI/UX Designer", "Flipkart Design", "Bengaluru", "Full-time", "₹12 - ₹22 LPA", ["UX/UI Design", "Figma", "Prototyping"], "2 - 4 Years", "Create user interfaces for e-commerce web and mobile platforms.", "https://flipkart.com/careers"),
    ("Senior Digital Content Editor", "The Hindu Group", "Chennai / Delhi", "Full-time", "₹7 - ₹14 LPA", ["Journalism", "Digital Media", "Editing"], "2 - 5 Years", "Write and edit breaking news reports for online media.", "https://thehindu.com/careers"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in arts_jobs_data:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    j.required_skills.set(s_objs)

arts_exams_data = [
    ("NID DAT PG 2027", "National Institute of Design", "govt", "Design & Arts", "Bachelor Degree in Design / BFA / BArch / Any Degree", "Design Aptitude, Creative Thinking, Visual Representation, Prototyping", "https://nid.edu"),
    ("UGC NET Mass Communication & Journalism 2027", "NTA", "govt", "Media & Arts", "Master Degree in Journalism / Mass Comm / MA", "Communication Theory, Print Media, Electronic Media, Advertising & PR, Research Methodology", "https://ugcnet.nta.nic.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in arts_exams_data:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={
        'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url
    })


# --- 6. ARCHITECTURE & INTERIOR DESIGN SEEDER ---
arch_degrees = ['BARCH', 'MARCH']

arch_careers_data = [
    ("Senior Architect & BIM Manager", "Architecture", "Leads building design, BIM modeling, construction drawings, and sustainable urban design.", 9.0, 24.0, ["Architectural Design", "BIM", "AutoCAD", "Revit"]),
    ("Urban Designer & Town Planner", "Urban Planning", "Plans municipal infrastructure, master planning, sustainable city zones, and GIS mapping.", 8.0, 20.0, ["Urban Planning", "GIS Mapping", "Architectural Design", "Master Planning"]),
]

for title, domain, desc, min_s, max_s, skills in arch_careers_data:
    c, created = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    link_degrees(c, arch_degrees)
    link_skill_reqs(c, skills)

arch_jobs_data = [
    ("BIM Architect & Project Designer", "Hafeez Contractor Architects", "Mumbai", "Full-time", "₹9 - ₹18 LPA", ["Architectural Design", "BIM", "Revit"], "2 - 4 Years", "Design high-rise commercial structures and manage Revit BIM models.", "https://hafeezcontractor.com"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in arch_jobs_data:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    j.required_skills.set(s_objs)

arch_exams_data = [
    ("GATE Architecture & Planning 2027", "IIT / GATE Committee", "govt", "Architecture", "BArch Degree", "Architecture Design, Building Construction, Building Services, Urban Planning, Landscape Design", "https://gate.iitk.ac.in"),
    ("NATA 2027 (National Aptitude Test in Architecture)", "Council of Architecture (CoA)", "govt", "Architecture", "Class 12 / Diploma in Architecture", "Drawing Skills, Aesthetic Sensitivity, Critical Thinking, Architectural Aptitude", "https://nata.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in arch_exams_data:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={
        'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url
    })


# --- 7. PURE SCIENCES / BIOTECH SEEDER ---
sci_degrees = ['BSC', 'MSC']

sci_careers_data = [
    ("Senior Research Scientist", "Scientific Research", "Conducts advanced experimental research in chemistry, physics, or molecular biology.", 8.0, 22.0, ["Research Methodology", "Data Analysis", "Laboratory Techniques", "Scientific Writing"]),
    ("Biotechnologist & R&D Specialist", "Biotechnology", "Develops biological products, genetic engineering, recombinant proteins, and bioprocesses.", 7.0, 18.0, ["Biotechnology", "Molecular Biology", "Recombinant DNA", "Cell Culture"]),
]

for title, domain, desc, min_s, max_s, skills in sci_careers_data:
    c, created = Career.objects.get_or_create(title=title, defaults={
        'domain': domain, 'description': desc, 'salary_min_lpa': min_s, 'salary_max_lpa': max_s
    })
    link_degrees(c, sci_degrees)
    link_skill_reqs(c, skills)

sci_jobs_data = [
    ("Senior R&D Scientist", "Biocon Research", "Bengaluru", "Full-time", "₹8 - ₹16 LPA", ["Biotechnology", "Molecular Biology", "Laboratory Techniques"], "2 - 4 Years", "Lead molecular biology research and protein purification projects.", "https://biocon.com/careers"),
]

for title, comp, loc, jtype, sal, req_s, exp, desc, url in sci_jobs_data:
    j, _ = JobOpportunity.objects.get_or_create(title=title, company=comp, defaults={
        'location': loc, 'job_type': jtype, 'salary_range': sal, 'experience_required': exp, 'description': desc, 'application_url': url
    })
    s_objs = get_skills(req_s)
    j.required_skills.set(s_objs)

sci_exams_data = [
    ("CSIR NET Chemical Sciences 2027", "NTA / CSIR", "govt", "Pure Science", "MSc in Chemistry / Chemical Sciences", "Inorganic Chemistry, Physical Chemistry, Organic Chemistry, Analytical Techniques", "https://csirnet.nta.nic.in"),
    ("CSIR NET Life Sciences 2027", "NTA / CSIR", "govt", "Life Sciences", "MSc in Biotechnology / Microbiology / Botany / Zoology", "Molecules and Interaction, Cellular Organization, Genetics, Ecology, Evolution", "https://csirnet.nta.nic.in"),
]

for exam_name, body, cat, dom, elig, syllabus, url in sci_exams_data:
    GovernmentExam.objects.get_or_create(exam_name=exam_name, defaults={
        'conducting_body': body, 'category': cat, 'domain': dom, 'eligibility': elig, 'syllabus_summary': syllabus, 'website_url': url
    })

print("Completed Seeding All 8 Domain Clusters Successfully!")
