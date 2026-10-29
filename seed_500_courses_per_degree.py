import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from profiles.models import Degree, Skill
from opportunities.models import Course
from profiles.skill_mapping import DEGREE_SKILLS_MAP

PROVIDERS = ['Coursera', 'Udemy', 'NPTEL', 'GeeksforGeeks', 'W3Schools', 'Simplilearn', 'YouTube']
DIFFICULTIES = ['Beginner', 'Intermediate', 'Advanced']

DOMAIN_COURSE_TEMPLATES = {
    'MBBS': [
        "Advanced Clinical Diagnostics & Patient Care", "Emergency Trauma Surgery & Intensive Triage",
        "ECG Interpretation & Cardiac Pathophysiology", "Pediatric Critical Care & Neonatology",
        "Neurological Examination & Clinical Neuroanatomy", "Internal Medicine & Systemic Pharmacology",
        "Obstetrics & High-Risk Pregnancy Management", "Gynecological Surgical Procedures & Healthcare",
        "Anatomy & Surgical Dissection Masterclass", "Clinical Pathology & Diagnostic Histopathology",
        "Medical Imaging: CT, MRI & Ultrasound Interpretation", "Infectious Disease Control & Microbiology",
        "Forensic Medicine & Clinical Toxicology", "Epidemiology & Global Public Health Strategy",
        "Critical Care Ventilation & Airway Management", "Dermatology & Clinical Skin Diagnostics",
        "Orthopedic Trauma & Surgical Fixation", "Ophthalmic Surgery & Diagnostic Retinal Care",
        "ENT Clinical Examination & Operative Surgery", "Clinical Oncology & Chemotherapy Protocols"
    ],
    'BDS': [
        "Endodontics & Root Canal Therapy Masterclass", "Oral & Maxillofacial Surgical Diagnostics",
        "Periodontal Plastic Surgery & Implantology", "Orthodontic Aligners & Facial Esthetics",
        "Prosthodontics: Crown, Bridge & Denture Design", "Pediatric Dentistry & Preventive Oral Care",
        "Oral Pathology & Biopsy Diagnosis", "Dental Radiology & 3D Cone Beam CT", "Restorative Dentistry & Aesthetic Composites",
        "Laser Dentistry & Minimally Invasive Care"
    ],
    'BPHARM': [
        "Industrial Pharmacy & Formulation Technology", "Pharmacokinetics & Biopharmaceutics",
        "Medicinal Chemistry & Molecular Drug Design", "Pharmacology & Safety Toxicology",
        "Quality Control & QA/QC Analytics in Pharma", "Clinical Research & Pharmacovigilance Protocols",
        "Pharmaceutical Analysis & HPLC Methods", "Biotechnology & Biopharmaceuticals",
        "Regulatory Affairs & USFDA Compliance", "Hospital & Community Pharmacy Management"
    ],
    'NURSING': [
        "Intensive Care Unit (ICU) Nursing Protocols", "Maternal & Child Health Nursing",
        "Clinical Pharmacology & Medication Safety", "Emergency & Critical Care Nursing",
        "Surgical Nursing & Post-Operative Care", "Public Health Nursing & Community Care",
        "Pediatric Nursing & Neonatal Resuscitation", "Psychiatric Nursing & Mental Health Care",
        "Infection Prevention & Hospital Hygiene", "Patient Assessment & Physical Triage"
    ],
    'PHYSIOTHERAPY': [
        "Musculoskeletal Rehabilitation & Manual Therapy", "Sports Kinesiology & Athletic Injury Rehab",
        "Neurological Rehabilitation & Physical Therapy", "Cardiopulmonary Physiotherapy & ICU Care",
        "Pediatric Physiotherapy & Motor Development", "Orthopedic Exercise Therapy & Mobilization",
        "Biomechanics & Movement Analysis", "Electrotherapy & Pain Management Protocols"
    ],
    'RADIOLOGY': [
        "CT Scan Protocol Optimization & Diagnostics", "MRI Physics & Advanced Image Interpretation",
        "Diagnostic Ultrasonography & Doppler Imaging", "Interventional Radiology Procedures",
        "Digital Radiography & PACS System Management", "Radiation Safety & Protection Standards"
    ],
    'VETERINARY': [
        "Veterinary Clinical Surgery & Anesthesia", "Livestock Disease Epidemiology & Control",
        "Small Animal Medicine & Diagnostics", "Veterinary Radiology & Imaging Techniques",
        "Avian & Exotic Animal Medicine", "Poultry & Dairy Farm Healthcare Management"
    ],
    'PSYCHOLOGY': [
        "Cognitive Behavioral Therapy (CBT) Masterclass", "Clinical Diagnostic Psychopathology & DSM-5",
        "Neuropsychology & Behavioral Brain Dynamics", "Counseling Psychology & Therapeutic Relations",
        "Child & Adolescent Developmental Psychology", "Organizational Psychology & Workplace Dynamics"
    ],
    'BTECH': [
        "Full Stack Software Engineering with React & Node", "Data Structures & Algorithms Masterclass",
        "System Design & Distributed Cloud Architecture", "Deep Learning & PyTorch Transformer Models",
        "Cybersecurity & Offensive Penetration Testing", "Embedded C & Real-Time Operating Systems (RTOS)",
        "DevOps, Docker & Kubernetes Production Deployment", "AWS Cloud Solutions Architecture Masterclass",
        "Microservices & Event-Driven Systems Architecture", "VLSI Circuit Design & Verilog HDL", "Machine Learning Pipeline Engineering",
        "Robotics Operating System (ROS) & Autonomous Controls", "Power Electronics & Smart Grid Systems",
        "Structural Analysis & Finite Element Modeling (FEA)", "CAD/CAM Mechanical Engineering Design",
        "Database System Internals & Query Optimization", "Mobile App Development with Flutter & Dart",
        "Industrial Automation & PLC SCADA Systems"
    ],
    'MTECH': [
        "Advanced Software Architecture & Scalable Cloud", "AI & Deep Learning Research Frontiers",
        "High Performance Computing & Distributed Systems", "Advanced VLSI Design & Microelectronics",
        "Advanced Control Systems & Robotics Engineering", "Computational Fluid Dynamics (CFD) Masterclass",
        "Advanced Structural Engineering & Seismic Design", "Cryptographic Protocols & Blockchain Architecture"
    ],
    'BCA': [
        "Core Java Programming & OOP Principles", "Python Web Development with Django & FastAPI",
        "Database Management Systems & SQL Querying", "Web Development Fundamentals: HTML, CSS & JS",
        "Data Structures & Algorithm Design in C++", "Linux Systems Administration & Shell Scripting",
        "Android App Development with Kotlin", "React.js Frontend Development Guide",
        "Computer Networks & Internet Protocols", "Software Engineering Fundamentals"
    ],
    'MCA': [
        "Enterprise Software Architecture with Spring Boot", "Cloud Native Application Engineering with Kubernetes",
        "Advanced Machine Learning & Data Mining", "Mobile Application Architecture & Security",
        "Full Stack MERN Stack Production Bootcamp", "Big Data Processing with Apache Spark & Hadoop",
        "Software Quality Assurance & Automated Testing", "Network Security & Ethical Hacking Protocols"
    ],
    'DIPLOMA': [
        "Industrial Electrical Maintenance & Wiring", "AutoCAD Mechanical & Architectural Drafting",
        "PLC Programming & Industrial SCADA Wiring", "CNC Machine Operation & G-Code Programming",
        "Computer Hardware & Network Troubleshooting", "Civil Engineering Site Surveying & Quantity Estimation",
        "Embedded Electronics & Microcontroller Projects", "Refrigeration & HVAC Systems Maintenance"
    ],
    'BCOM': [
        "Financial Accounting Standards & Ledger Mastery", "Income Tax Filing & Direct Taxation Laws",
        "GST Compliance, Filing & E-Way Bills", "Corporate Financial Modeling & Valuation in Excel",
        "Tally Prime & Automated Business Accounting", "Auditing & Assurance Standards Masterclass",
        "Banking Operations & Financial Services", "Business Economics & Market Analysis",
        "Cost & Management Accounting Techniques", "Investment Analysis & Stock Market Fundamentals"
    ],
    'MCOM': [
        "Advanced Financial Reporting & IFRS Standards", "Corporate Taxation & International Tax Planning",
        "Financial Risk Management & Derivative Analytics", "Advanced Cost Analysis & Budgetary Control",
        "Capital Market Investments & Portfolio Management", "Corporate Governance & Secretarial Audit"
    ],
    'CA': [
        "Advanced Chartered Accountancy Auditing Standards", "Corporate Financial Reporting & Analysis",
        "Direct & Indirect Tax Laws Complete Masterclass", "Strategic Financial Management & Valuation",
        "Advanced Capital Markets & Financial Engineering", "Forensic Accounting & Fraud Investigation"
    ],
    'BBA': [
        "Principles of Business Management & Leadership", "Digital Marketing Strategy & Social Media ROI",
        "Human Resource Management & Talent Acquisition", "Supply Chain & Logistics Management Essentials",
        "Brand Management & Marketing Communications", "Business Analytics & Corporate Data Visualization",
        "Sales Management & Negotiation Strategies", "Entrepreneurship & Venture Business Planning"
    ],
    'MBA': [
        "Executive Leadership & Corporate Strategy", "Investment Banking & Corporate Finance Valuation",
        "Strategic Marketing & Brand Equity Management", "Global Supply Chain Optimization & SAP ERP",
        "Human Capital Management & Strategic HR", "Product Management & SaaS Growth Strategy",
        "Operations Research & Business Decision Modeling", "Mergers & Acquisitions Financial Strategy"
    ],
    'BMS': [
        "Business Operations & Process Optimization", "Financial Management & Business Valuation",
        "Market Research & Consumer Behavior Analysis", "Project Management & Agile Operations"
    ],
    'LLB': [
        "Constitutional Law & Landmark Supreme Court Cases", "Corporate Law & Commercial Contract Drafting",
        "Criminal Law, IPC & Evidence Act Practice", "Civil Procedure Code & Litigation Drafting",
        "Intellectual Property Law: Patents & Trademarks", "Cyber Law & Information Technology Regulations",
        "Labour & Industrial Dispute Laws in India", "International Law & Arbitration Procedures"
    ],
    'BALLB': [
        "Legal Drafting, Conveyancing & Contract Review", "Corporate Governance & Company Law Compliance",
        "Environmental Law & Sustainable Regulation", "Administrative Law & Judicial Remedies",
        "Taxation Law & Corporate Tax Litigation", "Consumer Protection & Torts Masterclass"
    ],
    'BARCH': [
        "Architectural Design & Space Planning Principles", "BIM Revit & 3D Architectural Visualization",
        "Sustainable Architecture & LEED Certification", "Building Construction Technology & Materials",
        "Urban Planning, Zoning & Landscape Architecture", "AutoCAD 2D/3D Architectural Detailing"
    ],
    'MARCH': [
        "Parametric Architecture & Advanced Computational Design", "Urban Heritage Conservation & Sustainable Cities",
        "High-Performance Building Envelope Architecture", "Architectural Project Management & BIM Execution"
    ],
    'AGRI': [
        "Agronomy & Sustainable Crop Production Tech", "Soil Science, Nutrient Analysis & Fertility",
        "Agritech & Precision Agriculture Analytics", "Plant Pathology & Pest Management Systems",
        "Agribusiness Management & Farm Economics", "Seed Technology & Genetic Plant Breeding"
    ],
    'HORTICULTURE': [
        "Commercial Fruit & Vegetable Crop Cultivation", "Floriculture, Landscaping & Ornamental Gardening",
        "Post-Harvest Technology & Produce Preservation", "Greenhouse & Controlled Environment Agriculture"
    ],
    'SERICULTURE': [
        "Mulberry Cultivation & Sericulture Farm Management", "Silkworm Rearing & Disease Control Protocols",
        "Silk Reeling, Fiber Technology & Silk Testing", "Sericulture Economics & Extension Training"
    ],
    'BA': [
        "Public Administration & Governance Systems", "World History & Indian Political Thought",
        "English Literature & Critical Essay Writing", "Sociology & Social Change in Modern Society",
        "Microeconomics & Macroeconomic Principles", "International Relations & Global Diplomacy"
    ],
    'MA': [
        "Advanced Economic Policy & Econometrics", "Advanced Political Theory & Global Governance",
        "Literary Criticism & Modern Cultural Theory", "Sociological Research Methods & Data Analysis"
    ],
    'BSC': [
        "Organic & Analytical Chemistry Masterclass", "Cell Biology, Genetics & Recombinant DNA",
        "Classical Mechanics & Modern Quantum Physics", "Calculus, Linear Algebra & Differential Equations",
        "Microbiology & Industrial Biotechnology", "Environmental Science & Climate Ecosystems"
    ],
    'MSC': [
        "Advanced Molecular Genetics & Bioinformatics", "Quantum Mechanics & Condensed Matter Physics",
        "Advanced Organic Synthesis & Spectroscopy", "Applied Mathematics & Mathematical Modeling"
    ],
    'BFA': [
        "Fine Arts & Visual Composition Principles", "3D Digital Sculpting & Visual Art Production",
        "Graphic Design & Creative Brand Illustration", "Art History, Aesthetics & Visual Storytelling"
    ],
    'BDES': [
        "UI/UX Design Systems & Figma Prototyping", "Product Design, Ergonomics & CAD Prototyping",
        "Fashion Design, Textile Patterning & Styling", "Design Thinking & User-Centered Research"
    ],
    'BJMC': [
        "Investigative Journalism & Newsroom Reporting", "Digital Media Production & Video Editing",
        "Public Relations & Crisis Communication", "Media Ethics, Broadcast Law & Mass Communication"
    ]
}

def seed_500_courses_per_degree():
    print("Starting 500 Courses Per Degree Master Seeder...")

    degrees = list(Degree.objects.all())
    total_degrees = len(degrees)
    print(f"Found {total_degrees} degrees in database.")

    # 1. Ensure all degrees have skills linked
    for deg in degrees:
        skill_names = DEGREE_SKILLS_MAP.get(deg.code, [])
        if not skill_names:
            if 'TECH' in deg.code or 'CA' in deg.code or 'CS' in deg.code:
                skill_names = DEGREE_SKILLS_MAP.get('BTECH', [])
            elif 'MED' in deg.code or 'SURG' in deg.code:
                skill_names = DEGREE_SKILLS_MAP.get('MBBS', [])
            elif 'LAW' in deg.code:
                skill_names = DEGREE_SKILLS_MAP.get('LLB', [])
            elif 'AGR' in deg.code:
                skill_names = DEGREE_SKILLS_MAP.get('AGRI', [])
            elif 'COMM' in deg.code or 'BUS' in deg.code:
                skill_names = DEGREE_SKILLS_MAP.get('BCOM', [])
            else:
                skill_names = DEGREE_SKILLS_MAP.get('BSC', [])

        for sname in skill_names:
            s_obj, _ = Skill.objects.get_or_create(
                name=sname.strip(),
                defaults={'category': 'technical'}
            )
            deg.skills.add(s_obj)

    print("Linked skills for all 33 degrees.")

    # 2. Seed courses up to 500 per degree
    grand_total_created = 0

    for idx, deg in enumerate(degrees, 1):
        deg_skills = list(deg.skills.all())
        if not deg_skills:
            deg_skills = list(Skill.objects.all()[:15])

        existing_course_ids = set(Course.objects.filter(skill__in=deg_skills).values_list('id', flat=True))
        current_count = len(existing_course_ids)
        target_count = 500

        needed = target_count - current_count
        if needed <= 0:
            print(f"[{idx}/{total_degrees}] Degree '{deg.code}': Already has {current_count} courses (Target: 500). Skipping.")
            continue

        print(f"[{idx}/{total_degrees}] Degree '{deg.code}': Has {current_count} courses. Seeding {needed} new courses...")

        templates = DOMAIN_COURSE_TEMPLATES.get(deg.code, DOMAIN_COURSE_TEMPLATES.get('BTECH'))
        
        new_courses = []
        for i in range(needed):
            sk = deg_skills[i % len(deg_skills)]
            provider = PROVIDERS[i % len(PROVIDERS)]
            difficulty = DIFFICULTIES[i % len(DIFFICULTIES)]
            template_title = templates[i % len(templates)]
            
            variant_suffix = f" (Module { (i // len(templates)) + 1 })" if i >= len(templates) else ""
            full_title = f"{template_title}{variant_suffix}"
            
            description = (
                f"Comprehensive {difficulty} level course on {sk.name} tailored for {deg.name} candidates. "
                f"Master core concepts, practical case studies, and hands-on projects on {provider}."
            )

            search_query = "+".join(full_title.split())
            url = f"https://www.google.com/search?q={search_query}+{provider.lower()}"

            new_courses.append(Course(
                title=full_title,
                provider=provider,
                difficulty=difficulty,
                skill=sk,
                description=description,
                url=url
            ))

        Course.objects.bulk_create(new_courses, batch_size=500)
        grand_total_created += len(new_courses)
        print(f"    -> Added {len(new_courses)} courses for {deg.code}. Total courses for degree skills now: {Course.objects.filter(skill__in=deg_skills).count()}")

    print(f"Seeding Completed Successfully! Created {grand_total_created} new courses in total.")
    print(f"Total Courses in DB: {Course.objects.count()}")

if __name__ == '__main__':
    seed_500_courses_per_degree()
