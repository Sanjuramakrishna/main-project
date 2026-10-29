import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from profiles.models import Degree, Skill
from careers.models import Career, CareerSkillRequirement
from opportunities.models import JobOpportunity, GovernmentExam, Course, Certification

def seed_master_50_data():
    print("Starting master seed for Careers, Jobs, and Exams covering ALL 15 Degrees...")

    # Ensure essential skills exist
    skills_to_create = [
        ("Python", "technical"),
        ("Java", "technical"),
        ("JavaScript", "technical"),
        ("React", "technical"),
        ("Node.js", "technical"),
        ("C++", "technical"),
        ("HTML & CSS", "technical"),
        ("SQL & Databases", "technical"),
        ("Data Structures & Algorithms", "technical"),
        ("Cybersecurity & Networking", "technical"),
        ("Machine Learning", "data_ai"),
        ("Deep Learning & PyTorch", "data_ai"),
        ("Pandas & NumPy", "data_ai"),
        ("Scikit-Learn", "data_ai"),
        ("Data Visualization (Tableau/PowerBI)", "data_ai"),
        ("Docker & Kubernetes", "tools"),
        ("AWS & Cloud Computing", "tools"),
        ("Git & GitHub", "tools"),
        ("UI/UX Design & Figma", "tools"),
        ("CAD & SolidWorks", "core_engineering"),
        ("Embedded C / Microcontrollers", "core_engineering"),
        ("MATLAB & Simulink", "core_engineering"),
        ("PLC & SCADA Automation", "core_engineering"),
        ("Structural Analysis & ETABS", "core_engineering"),
        ("Financial Modeling & Excel", "management"),
        ("Digital Marketing & SEO", "management"),
        ("Agile & Project Management", "management"),
        ("Business Analysis", "management"),
        ("Accounting & Taxation", "management"),
        ("Corporate Finance & Valuation", "management"),
        ("Human Resource Management", "management"),
        ("Supply Chain & Operations", "management"),
        ("Communication & Public Speaking", "soft_skills"),
        ("Problem Solving & Critical Thinking", "soft_skills"),
        ("Technical Writing & Documentation", "soft_skills"),
        ("Clinical Medicine & Diagnostics", "core_engineering"),
        ("Legal Drafting & Contract Review", "management"),
        ("Agritech & Crop Analytics", "data_ai"),
        ("3D Animation & Visual Art", "tools"),
        ("Industrial Maintenance & Machining", "core_engineering"),
    ]

    for sk_name, sk_cat in skills_to_create:
        Skill.objects.get_or_create(name=sk_name, defaults={'category': sk_cat})

    all_degrees = list(Degree.objects.all())
    deg_map = {d.code.upper(): d for d in all_degrees}

    # ----------------------------------------------------
    # 1. SEED CAREERS (COVERING ALL 15 DEGREES)
    # ----------------------------------------------------
    # Degree codes in DB: BTECH, BCA, MCA, BCOM, MCOM, BBA, MBA, BSC, BA, MTECH, MBBS, BDA, LLB, AGRI, DIPLOMA
    careers_master = [
        # Tech & Engineering Careers (BTECH, BCA, MCA, MTECH, BSC, DIPLOMA)
        ("AI & Machine Learning Engineer", "Artificial Intelligence", 8.5, 28.0, 26.0, "Very High", ["BTECH", "MTECH", "BSC", "BCA", "MCA"], ["Machine Learning", "Python", "Deep Learning & PyTorch", "Scikit-Learn"]),
        ("Full Stack Web Developer", "Software Engineering", 6.0, 22.0, 22.0, "Very High", ["BTECH", "BCA", "MCA", "BSC", "MTECH", "DIPLOMA"], ["React", "Node.js", "JavaScript", "HTML & CSS", "SQL & Databases"]),
        ("Cloud & DevOps Architect", "Cloud Infrastructure", 9.0, 30.0, 24.0, "Very High", ["BTECH", "BCA", "MCA", "MTECH"], ["AWS & Cloud Computing", "Docker & Kubernetes", "Git & GitHub", "SQL & Databases"]),
        ("Cybersecurity & Ethical Hacking Specialist", "Information Security", 7.5, 25.0, 25.0, "Very High", ["BTECH", "BCA", "MCA", "BSC", "MTECH", "DIPLOMA"], ["Cybersecurity & Networking", "Python", "SQL & Databases"]),
        ("Data Scientist & Predictive Analyst", "Data Science", 8.0, 26.0, 23.0, "Very High", ["BTECH", "BSC", "BCOM", "MCOM", "BBA", "MBA", "MCA", "MTECH", "AGRI"], ["Python", "Pandas & NumPy", "Machine Learning", "Data Visualization (Tableau/PowerBI)"]),
        ("Backend Systems Engineer", "Software Engineering", 6.5, 20.0, 20.0, "High", ["BTECH", "BCA", "MCA", "MTECH", "DIPLOMA"], ["Java", "Python", "SQL & Databases", "Data Structures & Algorithms"]),
        ("Front-End UI/UX Engineer", "Web Development", 5.5, 18.0, 18.0, "High", ["BTECH", "BCA", "MCA", "BSC", "BA", "BDA"], ["React", "JavaScript", "HTML & CSS", "UI/UX Design & Figma"]),
        ("Embedded Systems & Firmware Engineer", "Core Electronics", 6.0, 20.0, 19.0, "High", ["BTECH", "MTECH", "DIPLOMA"], ["Embedded C / Microcontrollers", "C++", "MATLAB & Simulink"]),
        ("Robotics & Mechatronics Automation Engineer", "Core Robotics", 7.0, 24.0, 21.0, "High", ["BTECH", "MTECH", "DIPLOMA"], ["Embedded C / Microcontrollers", "Python", "PLC & SCADA Automation", "CAD & SolidWorks"]),
        ("Mechanical CAD/CAM Design Engineer", "Mechanical Engineering", 5.0, 16.0, 15.0, "Moderate", ["BTECH", "MTECH", "DIPLOMA"], ["CAD & SolidWorks", "MATLAB & Simulink"]),
        ("Civil Structural & Infrastructure Engineer", "Civil Engineering", 5.0, 18.0, 16.0, "Moderate", ["BTECH", "MTECH", "DIPLOMA"], ["Structural Analysis & ETABS", "CAD & SolidWorks"]),
        ("Electrical Power & Smart Grid Engineer", "Electrical Engineering", 5.5, 17.0, 16.0, "Moderate", ["BTECH", "MTECH", "DIPLOMA"], ["MATLAB & Simulink", "PLC & SCADA Automation"]),
        ("Mobile App Developer (Flutter / React Native)", "Mobile Engineering", 6.0, 22.0, 22.0, "Very High", ["BTECH", "BCA", "MCA", "BSC", "DIPLOMA"], ["React", "JavaScript", "Python", "Git & GitHub"]),
        ("Database Administrator & Data Architect", "Data Infrastructure", 7.0, 23.0, 16.0, "High", ["BTECH", "BCA", "MCA", "BSC", "MTECH"], ["SQL & Databases", "AWS & Cloud Computing"]),
        ("Site Reliability Engineer (SRE)", "Cloud Reliability", 8.5, 28.0, 25.0, "Very High", ["BTECH", "MCA", "MTECH"], ["Docker & Kubernetes", "AWS & Cloud Computing", "Python"]),
        ("Software QA & Test Automation Engineer", "Quality Assurance", 5.0, 16.0, 15.0, "High", ["BTECH", "BCA", "MCA", "BSC", "DIPLOMA"], ["Python", "Java", "SQL & Databases"]),

        # Business, Finance & Commerce Careers (BCOM, MCOM, BBA, MBA)
        ("Financial Analyst & Investment Advisor", "Finance & Banking", 6.0, 22.0, 19.0, "Very High", ["BCOM", "MCOM", "BBA", "MBA", "BSC", "BA"], ["Financial Modeling & Excel", "Corporate Finance & Valuation", "Accounting & Taxation"]),
        ("Corporate Accountant & Tax Consultant", "Accounting", 4.5, 15.0, 14.0, "High", ["BCOM", "MCOM", "BBA", "MBA"], ["Accounting & Taxation", "Financial Modeling & Excel"]),
        ("Investment Banking Analyst", "Investment Banking", 10.0, 35.0, 20.0, "Very High", ["BCOM", "MCOM", "BBA", "MBA"], ["Corporate Finance & Valuation", "Financial Modeling & Excel", "Accounting & Taxation"]),
        ("Risk & Quantitative Compliance Analyst", "Financial Risk", 7.0, 24.0, 18.0, "High", ["BCOM", "MCOM", "BSC", "MBA", "LLB"], ["Financial Modeling & Excel", "SQL & Databases", "Pandas & NumPy"]),
        ("Digital Marketing & Growth Manager", "Marketing", 5.0, 18.0, 22.0, "Very High", ["BBA", "MBA", "BCOM", "MCOM", "BA", "BDA", "BCA"], ["Digital Marketing & SEO", "Data Visualization (Tableau/PowerBI)", "Communication & Public Speaking"]),
        ("Product Manager (Tech & SaaS)", "Product Management", 10.0, 32.0, 24.0, "Very High", ["BTECH", "BBA", "MBA", "MCA", "MTECH", "BDA"], ["Business Analysis", "Agile & Project Management", "UI/UX Design & Figma"]),
        ("Business Intelligence Analyst", "Data Analytics", 6.0, 20.0, 20.0, "High", ["BCOM", "MCOM", "BBA", "MBA", "BSC", "BTECH"], ["Data Visualization (Tableau/PowerBI)", "SQL & Databases", "Pandas & NumPy"]),
        ("Agile Scrum Master & Technical Delivery Lead", "Project Management", 8.0, 25.0, 17.0, "High", ["BTECH", "BBA", "MBA", "MCA"], ["Agile & Project Management", "Communication & Public Speaking"]),
        ("Human Resource Specialist & Talent Manager", "Human Resources", 4.8, 16.0, 15.0, "High", ["BBA", "MBA", "BA", "BCOM", "MCOM"], ["Human Resource Management", "Communication & Public Speaking"]),
        ("Supply Chain & Logistics Operations Manager", "Supply Chain", 5.5, 19.0, 17.0, "High", ["BBA", "MBA", "BTECH", "BCOM", "MCOM"], ["Supply Chain & Operations", "Financial Modeling & Excel"]),
        ("Enterprise Resource Planning (ERP) Consultant", "Enterprise Systems", 7.0, 24.0, 17.0, "High", ["BCOM", "MCOM", "BBA", "MBA", "BTECH", "MCA"], ["Accounting & Taxation", "SQL & Databases", "Business Analysis"]),
        ("Senior Tax & Audit Specialist", "Corporate Taxation", 6.5, 20.0, 18.0, "High", ["BCOM", "MCOM", "MBA"], ["Accounting & Taxation", "Financial Modeling & Excel"]),

        # Medical & Healthcare Careers (MBBS, BSC, MTECH)
        ("Resident Medical Officer & Clinical Specialist", "Healthcare & Medicine", 9.0, 30.0, 20.0, "Very High", ["MBBS"], ["Clinical Medicine & Diagnostics", "Communication & Public Speaking", "Problem Solving & Critical Thinking"]),
        ("Clinical Research Scientist", "Pharmaceutical & Clinical", 7.5, 24.0, 22.0, "High", ["MBBS", "BSC", "MTECH"], ["Clinical Medicine & Diagnostics", "Pandas & NumPy", "Technical Writing & Documentation"]),
        ("Healthcare & Hospital Administrator", "Healthcare Management", 6.5, 22.0, 18.0, "High", ["MBBS", "MBA", "BBA", "BSC"], ["Human Resource Management", "Financial Modeling & Excel", "Communication & Public Speaking"]),
        ("Telemedicine & HealthTech Specialist", "Digital Health", 8.0, 26.0, 25.0, "Very High", ["MBBS", "BTECH", "MCA"], ["Clinical Medicine & Diagnostics", "Digital Marketing & SEO", "Communication & Public Speaking"]),
        ("Medical Devices & Instrumentation Engineer", "Biomedical Engineering", 6.0, 20.0, 18.0, "High", ["BTECH", "MTECH", "MBBS", "BSC"], ["Embedded C / Microcontrollers", "MATLAB & Simulink"]),

        # Law & Legal Careers (LLB, BALLB, BA, BCOM, MBA)
        ("Corporate Legal Counsel", "Legal & Corporate Law", 8.0, 28.0, 20.0, "Very High", ["LLB", "BALLB", "BA", "BCOM", "MBA"], ["Legal Drafting & Contract Review", "Communication & Public Speaking", "Problem Solving & Critical Thinking"]),
        ("Legal Tech & Compliance Officer", "Legal Compliance", 7.5, 25.0, 22.0, "High", ["LLB", "BALLB", "BCOM", "MCOM", "MBA", "BTECH"], ["Legal Drafting & Contract Review", "Business Analysis", "Cybersecurity & Networking"]),
        ("Intellectual Property (IP) Attorney", "Patents & IP Law", 9.0, 32.0, 21.0, "Very High", ["LLB", "BALLB", "BTECH", "MTECH", "BSC"], ["Legal Drafting & Contract Review", "Technical Writing & Documentation"]),
        ("Cyber Law & Privacy Consultant", "Information Law", 8.5, 27.0, 24.0, "Very High", ["LLB", "BALLB", "BTECH", "BCA", "MCA"], ["Legal Drafting & Contract Review", "Cybersecurity & Networking"]),
        ("Judicial Services Officer / Magistrate", "Judicial Services", 10.0, 28.0, 15.0, "High", ["LLB", "BALLB"], ["Legal Drafting & Contract Review", "Communication & Public Speaking"]),

        # Agriculture & Agritech Careers (AGRI, SERICULTURE, HORTICULTURE, BSC, BTECH, DIPLOMA)
        ("Agritech & Smart Farming Specialist", "Agriculture Technology", 6.0, 22.0, 25.0, "Very High", ["AGRI", "HORTICULTURE", "SERICULTURE", "BTECH", "BSC", "DIPLOMA"], ["Agritech & Crop Analytics", "Python", "Data Visualization (Tableau/PowerBI)"]),
        ("Agriculture Extension Officer", "Government Agriculture", 5.5, 18.0, 16.0, "High", ["AGRI", "HORTICULTURE", "SERICULTURE", "BSC"], ["Agritech & Crop Analytics", "Communication & Public Speaking"]),
        ("Soil & Crop Data Analyst", "Precision Agriculture", 6.5, 20.0, 22.0, "High", ["AGRI", "HORTICULTURE", "BSC", "BTECH"], ["Agritech & Crop Analytics", "Pandas & NumPy", "Python"]),
        ("Organic Agribusiness Manager", "Agri Management", 6.0, 19.0, 20.0, "High", ["AGRI", "HORTICULTURE", "BBA", "MBA", "BCOM"], ["Supply Chain & Operations", "Digital Marketing & SEO"]),
        ("Food Safety & Quality Auditor", "Food Standards", 5.0, 16.0, 17.0, "Moderate", ["AGRI", "BSC", "BTECH"], ["Problem Solving & Critical Thinking", "Technical Writing & Documentation"]),

        # Design, Arts & Media Careers (BDA, BDES, BFA, BJMC, BA, BSC)
        ("UI/UX Design Specialist", "Design & User Experience", 6.0, 22.0, 24.0, "Very High", ["BDA", "BDES", "BFA", "BA", "BSC", "BCA", "BTECH"], ["UI/UX Design & Figma", "HTML & CSS", "Communication & Public Speaking"]),
        ("Game Art & 3D Animator", "Interactive Media", 6.5, 24.0, 22.0, "High", ["BDA", "BDES", "BFA", "BA", "BCA", "BTECH"], ["3D Animation & Visual Art", "UI/UX Design & Figma", "C++"]),
        ("Graphic & Visual Brand Strategist", "Brand Design", 5.0, 18.0, 19.0, "High", ["BDA", "BDES", "BFA", "BA", "BBA"], ["3D Animation & Visual Art", "UI/UX Design & Figma", "Digital Marketing & SEO"]),
        ("Motion Graphics & Video Editor", "Digital Media", 5.5, 19.0, 20.0, "High", ["BDA", "BDES", "BFA", "BJMC", "BA", "BSC"], ["3D Animation & Visual Art", "UI/UX Design & Figma"]),
        ("Journalism & Digital Media Specialist", "Media & Journalism", 5.0, 17.0, 18.0, "High", ["BJMC", "BA", "MA"], ["Communication & Public Speaking", "Digital Marketing & SEO"]),

        # Dentistry & Health Careers (BDS, MBBS, BPHARM, RADIOLOGY, NURSING, PHYSIOTHERAPY, VETERINARY)
        ("Dental Surgeon & Oral Specialist", "Dentistry", 8.0, 25.0, 18.0, "High", ["BDS"], ["Clinical Medicine & Diagnostics", "Communication & Public Speaking"]),
        ("Pharmacist & Drug Safety Specialist", "Pharmacy", 6.0, 20.0, 20.0, "High", ["BPHARM"], ["Technical Writing & Documentation", "Problem Solving & Critical Thinking"]),
        ("Radiology & Medical Imaging Specialist", "Radiology", 7.0, 22.0, 21.0, "High", ["RADIOLOGY", "MBBS"], ["Clinical Medicine & Diagnostics", "MATLAB & Simulink"]),
        ("Clinical Nurse Specialist", "Nursing", 5.5, 18.0, 19.0, "High", ["NURSING"], ["Clinical Medicine & Diagnostics", "Communication & Public Speaking"]),
        ("Orthopedic & Sports Physiotherapist", "Physiotherapy", 6.0, 20.0, 20.0, "High", ["PHYSIOTHERAPY"], ["Clinical Medicine & Diagnostics", "Communication & Public Speaking"]),
        ("Veterinary Medical Officer", "Veterinary Medicine", 7.0, 22.0, 18.0, "High", ["VETERINARY"], ["Clinical Medicine & Diagnostics", "Problem Solving & Critical Thinking"]),

        # Architecture, CA & Management Careers (BARCH, MARCH, CA, BMS)
        ("Architectural Designer & BIM Architect", "Architecture", 7.0, 24.0, 20.0, "High", ["BARCH", "MARCH"], ["CAD & SolidWorks", "UI/UX Design & Figma"]),
        ("Chartered Accountant & Financial Auditor", "Chartered Accountancy", 9.0, 30.0, 22.0, "Very High", ["CA", "MCOM", "BCOM"], ["Accounting & Taxation", "Financial Modeling & Excel", "Corporate Finance & Valuation"]),
        ("Business Operations Analyst", "Management Studies", 6.0, 20.0, 20.0, "High", ["BMS", "BBA", "MBA"], ["Business Analysis", "Financial Modeling & Excel"]),
        ("Clinical Psychologist & Counselor", "Psychology", 6.0, 20.0, 22.0, "High", ["PSYCHOLOGY", "BA", "MA"], ["Communication & Public Speaking", "Problem Solving & Critical Thinking"]),

        # Diploma & Vocational Careers (DIPLOMA, BTECH)
        ("Polytechnic Junior Engineer (JE)", "Engineering Services", 4.5, 14.0, 16.0, "High", ["DIPLOMA", "BTECH"], ["CAD & SolidWorks", "Industrial Maintenance & Machining", "PLC & SCADA Automation"]),
        ("Industrial Automation Technician", "Manufacturing Automation", 4.2, 13.5, 17.0, "High", ["DIPLOMA"], ["PLC & SCADA Automation", "Embedded C / Microcontrollers", "Industrial Maintenance & Machining"]),
        ("CAD Technical Drafter", "Engineering Design", 4.0, 12.0, 15.0, "Moderate", ["DIPLOMA"], ["CAD & SolidWorks", "Structural Analysis & ETABS"]),
        ("CNC Machine & Machining Programmer", "Manufacturing", 4.5, 13.0, 16.0, "Moderate", ["DIPLOMA"], ["Industrial Maintenance & Machining", "CAD & SolidWorks"]),
        ("Field Service Operations Specialist", "Technical Support", 4.0, 12.5, 15.0, "Moderate", ["DIPLOMA", "BCA"], ["Communication & Public Speaking", "Problem Solving & Critical Thinking"]),
    ]

    added_careers = 0
    for title, domain, min_s, max_s, growth, demand, deg_codes, sk_names in careers_master:
        car, created = Career.objects.get_or_create(
            title=title,
            defaults={
                'domain': domain,
                'description': f"Professional {title} role in {domain}. Dynamic career progression path with strong market demand.",
                'salary_min_lpa': min_s,
                'salary_max_lpa': max_s,
                'growth_rate_pct': growth,
                'industry_demand': demand
            }
        )
        if created:
            added_careers += 1

        # Attach degrees
        for code in deg_codes:
            if code in deg_map:
                car.eligible_degrees.add(deg_map[code])

        # Attach skills
        for idx, sk_n in enumerate(sk_names):
            sk_obj = Skill.objects.filter(name__iexact=sk_n).first()
            if sk_obj:
                imp = 'essential' if idx < 2 else 'recommended'
                CareerSkillRequirement.objects.get_or_create(career=car, skill=sk_obj, defaults={'importance': imp})

    print(f"Seeded {added_careers} new Careers (Total Careers in DB: {Career.objects.count()}).")

    # ----------------------------------------------------
    # 2. SEED JOB OPPORTUNITIES (COVERING ALL DOMAINS & DEGREES)
    # ----------------------------------------------------
    jobs_master = [
        # Tech & Engineering Jobs
        ("Scientist / Engineer 'SC' (Computer Science)", "ISRO - Indian Space Research Organisation", "Bengaluru / Sriharikota", "Full-time", "₹10.5 - ₹15.6 LPA", "0 - 2 Years", "Develop space mission software, telemetry algorithms, real-time satellite control systems.", "https://www.isro.gov.in/Careers.html", ["Python", "C++", "Data Structures & Algorithms"]),
        ("Scientist 'B' (Cyber Security & AI)", "DRDO - Defence Research & Dev Org", "New Delhi / Hyderabad", "Full-time", "₹10.8 - ₹16.0 LPA", "GATE Qualified", "Military-grade quantum encryption, defense AI systems, automated threat detection.", "https://rac.gov.in", ["Cybersecurity & Networking", "C++", "Python", "Machine Learning"]),
        ("Scientist 'B' (Cloud & e-Gov Gateway)", "NIC - National Informatics Centre", "New Delhi / State Capitals", "Full-time", "₹9.5 - ₹14.5 LPA", "0 - 3 Years", "National cloud infrastructure, citizen verification gateways, high-scale e-Gov portals.", "https://www.nic.in/recruitment", ["Java", "React", "SQL & Databases", "AWS & Cloud Computing"]),
        ("Graduate Engineer Officer (IT Systems)", "IOCL - Indian Oil Corporation Ltd", "Mumbai / New Delhi", "Full-time", "₹14.0 - ₹18.5 LPA", "0 - 1 Year", "Maharatna PSU enterprise ERP, cloud pipelines, refinery IoT analytics.", "https://www.iocl.com", ["Python", "SQL & Databases", "AWS & Cloud Computing"]),
        ("Executive Trainee (IT & Automation)", "NTPC Limited (Maharatna PSU)", "Noida / Hyderabad", "Full-time", "₹13.5 - ₹17.8 LPA", "0 - 2 Years", "Smart power grid monitoring software, industrial automation networks.", "https://careers.ntpc.co.in", ["Java", "SQL & Databases", "Data Structures & Algorithms"]),
        ("Probationary Engineer (Defense Software)", "BEL - Bharat Electronics Limited", "Bengaluru / Ghaziabad", "Full-time", "₹11.0 - ₹15.0 LPA", "0 - 2 Years", "Radar signal processing, naval defense communications, computer vision threat models.", "https://www.bel-india.in", ["C++", "Python", "Machine Learning"]),
        ("Specialist IT Manager (Cloud & Security)", "SBI - State Bank of India", "Mumbai / Navi Mumbai", "Full-time", "₹15.0 - ₹22.0 LPA", "1 - 4 Years", "Core banking cloud security, anti-money laundering AI, UPI transaction microservices.", "https://bank.sbi/careers", ["Java", "Cybersecurity & Networking", "SQL & Databases"]),
        ("Scientific Officer 'C' (Supercomputing)", "BARC - Bhabha Atomic Research Centre", "Trombay, Mumbai", "Full-time", "₹11.5 - ₹16.5 LPA", "0 - 2 Years", "High-performance supercomputing simulations, nuclear safety control systems.", "https://barc.gov.in", ["C++", "Python", "Data Structures & Algorithms"]),
        ("Associate Software Development Engineer", "Amazon India", "Bengaluru / Hyderabad", "Full-time", "₹18.0 - ₹28.0 LPA", "0 - 1 Year", "Build distributed cloud services, high-scale transaction backend APIs.", "https://amazon.jobs", ["Java", "Python", "Data Structures & Algorithms"]),
        ("Graduate Software Engineer", "Google Cloud India", "Bengaluru / Gurgaon", "Full-time", "₹22.0 - ₹32.0 LPA", "0 - 1 Year", "Cloud platform development, kubernetes container telemetry, AI APIs.", "https://careers.google.com", ["C++", "Python", "Docker & Kubernetes"]),
        ("Software Engineer - Core Products", "Microsoft India", "Hyderabad / Noida", "Full-time", "₹20.0 - ₹30.0 LPA", "0 - 2 Years", "Azure microservices, C# / .NET / C++ high performance computing.", "https://careers.microsoft.com", ["C++", "Java", "Data Structures & Algorithms"]),
        ("Data Analyst - Business Intelligence", "Flipkart", "Bengaluru", "Full-time", "₹10.0 - ₹16.0 LPA", "0 - 2 Years", "Supply chain analytics, customer funnel visualization, SQL pipelines.", "https://www.flipkartcareers.com", ["SQL & Databases", "Data Visualization (Tableau/PowerBI)", "Pandas & NumPy"]),
        ("Associate Machine Learning Engineer", "Swiggy AI Labs", "Bengaluru", "Full-time", "₹14.0 - ₹22.0 LPA", "0 - 2 Years", "Delivery route optimization, recommendation engines, food NLP models.", "https://careers.swiggy.com", ["Python", "Machine Learning", "Scikit-Learn"]),
        ("Front-End Developer (React)", "Razorpay", "Bengaluru / Remote", "Full-time", "₹12.0 - ₹18.0 LPA", "1 - 3 Years", "Payment gateway checkout UI, dashboard analytics, responsive web apps.", "https://razorpay.com/jobs", ["React", "JavaScript", "HTML & CSS"]),

        # Medical & Health Jobs (MBBS, BSC)
        ("Resident Medical Officer (RMO)", "Apollo Hospitals", "Bengaluru / Hyderabad", "Full-time", "₹12.0 - ₹18.0 LPA", "0 - 2 Years MBBS", "Inpatient clinical care, emergency triage, electronic health record management.", "https://www.apollohospitals.com/careers", ["Clinical Medicine & Diagnostics", "Communication & Public Speaking"]),
        ("Clinical Research Associate", "Pfizer India", "Mumbai", "Full-time", "₹6.5 - ₹10.5 LPA", "0 - 2 Years MBBS/BSc", "Clinical trial protocol monitoring, FDA safety data reporting, patient diagnostics.", "https://www.pfizer.co.in/careers", ["Clinical Medicine & Diagnostics", "Technical Writing & Documentation"]),
        ("Health Analytics Associate", "Practo Technologies", "Bengaluru / Remote", "Full-time", "₹7.0 - ₹12.0 LPA", "0 - 2 Years", "Telemedicine patient flow analytics, electronic prescription data pipelines.", "https://www.practo.com/careers", ["Pandas & NumPy", "SQL & Databases"]),

        # Law & Governance Jobs (LLB, BA, BCOM)
        ("Associate Corporate Legal Counsel", "AZB & Partners", "Mumbai / New Delhi", "Full-time", "₹14.0 - ₹20.0 LPA", "0 - 2 Years LLB", "Corporate M&A legal due diligence, commercial agreement drafting, regulatory compliance.", "https://www.azbpartners.com/careers", ["Legal Drafting & Contract Review", "Communication & Public Speaking"]),
        ("In-House Legal & Compliance Specialist", "Reliance Industries Ltd", "Mumbai", "Full-time", "₹9.0 - ₹15.0 LPA", "0 - 2 Years LLB/BCom", "Contract lifecycle management, IP trademark documentation, corporate compliance audit.", "https://www.ril.com/Careers.aspx", ["Legal Drafting & Contract Review", "Accounting & Taxation"]),
        ("Legal Tech & Cyber Law Associate", "Trilegal India", "Bengaluru / Delhi", "Full-time", "₹11.0 - ₹17.0 LPA", "0 - 2 Years LLB/BTech", "Cybersecurity legal compliance, data privacy framework audit (DPDP Act), legal automation.", "https://trilegal.com/careers", ["Legal Drafting & Contract Review", "Cybersecurity & Networking"]),

        # Agriculture & Agritech Jobs (AGRI, BSC, DIPLOMA)
        ("Agritech Operations & Data Associate", "DeHaat (Green Agrevolution)", "Gurugram / Patna", "Full-time", "₹6.0 - ₹10.0 LPA", "0 - 2 Years AGRI/BSc", "Crop yield prediction algorithms, farmer advisory portal operations, satellite imagery analysis.", "https://agribegri.com/careers", ["Agritech & Crop Analytics", "Pandas & NumPy"]),
        ("Agriculture Field Officer (AFO)", "State Bank of India (Agri Division)", "Statewide Branches", "Full-time", "₹8.5 - ₹14.0 LPA", "BSc Agri Graduate", "Agricultural loan credit processing, Kisan Credit Card evaluation, farm assets audit.", "https://bank.sbi/careers", ["Agritech & Crop Analytics", "Communication & Public Speaking"]),
        ("Precision Farming Specialist", "Ninjacart", "Bengaluru / Pune", "Full-time", "₹6.5 - ₹11.0 LPA", "0 - 2 Years AGRI/BTech", "Farm-to-fork supply chain analytics, quality scoring, cold chain logistics.", "https://ninjacart.in/careers", ["Supply Chain & Operations", "Agritech & Crop Analytics"]),

        # Design, Arts & Media Jobs (BDA, BA)
        ("Visual Experience Designer", "Canva India", "Remote / Mumbai", "Full-time", "₹8.0 - ₹14.0 LPA", "0 - 2 Years BDA/BA", "Digital visual templates, typography systems, vector illustrations, promotional assets.", "https://www.canva.com/careers", ["UI/UX Design & Figma", "3D Animation & Visual Art"]),
        ("UI/UX Product Designer", "Paytm", "Noida / Remote", "Full-time", "₹8.0 - ₹14.0 LPA", "1 - 3 Years BDA/BTech", "Mobile wallet interface design, wireframes, user testing prototypes.", "https://paytm.com/careers", ["UI/UX Design & Figma", "HTML & CSS"]),

        # Diploma & Vocational Jobs (DIPLOMA)
        ("Junior Engineer Trainee (JET - Mechanical)", "Tata Motors", "Pune / Jamshedpur", "Full-time", "₹4.5 - ₹7.0 LPA", "Diploma Engineering", "Assembly line quality control, CNC machining supervision, vehicle chassis inspection.", "https://www.tatamotors.com/careers", ["CAD & SolidWorks", "Industrial Maintenance & Machining"]),
        ("Junior Technical Supervisor", "Larsen & Toubro (L&T)", "Mumbai / Chennai", "Full-time", "₹4.2 - ₹6.8 LPA", "Diploma Civil/Electrical", "Construction site supervision, electrical wiring layout execution, CAD drafting.", "https://www.larsentoubro.com", ["CAD & SolidWorks", "PLC & SCADA Automation"]),
        ("Industrial Automation Specialist", "Siemens India", "Bengaluru / Pune", "Full-time", "₹4.8 - ₹7.5 LPA", "Diploma Electrical/ECE", "PLC programming, SCADA panel wiring, industrial motor drive maintenance.", "https://www.siemens.com/in/careers", ["PLC & SCADA Automation", "Embedded C / Microcontrollers"]),

        # Finance & Commerce Jobs
        ("Financial Analyst - Global Markets", "Goldman Sachs", "Bengaluru", "Full-time", "₹16.0 - ₹25.0 LPA", "0 - 2 Years BCom/MCom/MBA", "Equity valuation, quantitative risk modeling, financial forecasting.", "https://www.goldmansachs.com/careers", ["Financial Modeling & Excel", "Corporate Finance & Valuation"]),
        ("Corporate Finance Associate", "JPMorgan Chase", "Mumbai / Bengaluru", "Full-time", "₹15.0 - ₹22.0 LPA", "0 - 2 Years BCom/MCom/MBA", "DCF modeling, investment pitch decks, M&A due diligence.", "https://careers.jpmorgan.com", ["Financial Modeling & Excel", "Accounting & Taxation"]),
        ("Taxation & Audit Senior Analyst", "Deloitte India", "Hyderabad / Gurugram", "Full-time", "₹7.0 - ₹11.0 LPA", "0 - 2 Years BCom/MCom", "Statutory audit, GST compliance, international tax reporting.", "https://www2.deloitte.com/in/en/careers", ["Accounting & Taxation", "Financial Modeling & Excel"]),
    ]

    added_jobs = 0
    for title, company, loc, jtype, sal, exp, desc, url, sk_list in jobs_master:
        job, created = JobOpportunity.objects.get_or_create(
            title=title,
            company=company,
            defaults={
                'location': loc,
                'job_type': jtype,
                'salary_range': sal,
                'experience_required': exp,
                'description': desc,
                'application_url': url,
                'is_active': True
            }
        )
        if created:
            added_jobs += 1

        for sk_n in sk_list:
            sk_obj = Skill.objects.filter(name__iexact=sk_n).first()
            if sk_obj:
                job.required_skills.add(sk_obj)

    print(f"Seeded {added_jobs} new Job Opportunities (Total Jobs in DB: {JobOpportunity.objects.count()}).")

    # ----------------------------------------------------
    # 3. SEED COMPETITIVE & CERTIFICATION EXAMS (ALL 15 DEGREES)
    # ----------------------------------------------------
    GovernmentExam.objects.all().delete()
    exams_master = [
        # UPSC & Civil Services (All Degrees)
        ("UPSC Civil Services Examination (CSE - IAS/IPS/IFS)", "Union Public Service Commission (UPSC)", "govt", "Civil Services", "Bachelor's Degree in any discipline (BTech/BCom/BA/BSc/MBBS/LLB/AGRI/BDA).", "Prelims GS-I + CSAT GS-II. Mains 9 Papers + Interview.", "February 04, 2027", "February 24, 2027", "May 23, 2027", "Session 1: 09:30 AM | Session 2: 02:30 PM", "NCERTs, Laxmikanth, The Hindu", "https://upsc.gov.in"),

        # Medical Exams (MBBS)
        ("NEET-PG 2027 (National Eligibility cum Entrance Test - PG)", "National Board of Examinations (NBE)", "govt", "Medical PG Admissions (MD/MS)", "MBBS Degree with completed 1-year internship.", "200 Multiple Choice Questions (3 Hours 30 Mins) covering Clinical & Pre-Clinical Medicine.", "January 15, 2027", "February 10, 2027", "March 28, 2027", "09:00 AM – 12:30 PM", "First Aid for USMLE, Marrow Test Series", "https://nbe.edu.in"),
        ("NEXT (National Exit Test for MBBS / Medical Licensure)", "National Medical Commission (NMC)", "govt", "Medical Licensure & PG Entry", "Final Year MBBS Students.", "Step 1 (CBT Theory 540 Qs) + Step 2 (Practical Clinical Exam).", "February 01, 2027", "March 01, 2027", "May 10, 2027", "Shift 1: 09:00 AM | Shift 2: 02:00 PM", "NMC Official Clinical Practice Modules", "https://www.nmc.org.in"),

        # Law Exams (LLB)
        ("CLAT-PG 2027 (Common Law Admission Test for LLM)", "Consortium of National Law Universities", "govt", "Post-Graduate Law (LLM)", "3-Year or 5-Year LLB Degree with min 50% marks.", "120 Objective Questions testing Constitutional Law, Jurisprudence, Criminal Law, Contracts.", "August 01, 2026", "November 10, 2026", "December 06, 2026", "02:00 PM – 04:00 PM", "CLAT Post-Graduate Prep Guide", "https://consortiumofnlus.ac.in"),
        ("AIBE XXI 2027 (All India Bar Examination)", "Bar Council of India (BCI)", "govt", "Advocate Practice Licensure", "LLB Graduate enrolled with State Bar Council.", "100 Objective Questions covering Bar Council Syllabus & Judicial Precedents.", "September 10, 2026", "October 25, 2026", "November 22, 2026", "10:00 AM – 01:30 PM", "BCI Bare Acts & Official Manual", "https://allindiabarexamination.com"),
        ("State Judicial Services Examination (PCS-J)", "State Public Service Commissions / High Courts", "govt", "Civil Judge / Judicial Magistrate", "LLB Degree from recognized University.", "Prelims CBT + Mains Written (Civil & Criminal Law) + Viva-Voce.", "October 01, 2026", "November 15, 2026", "January 24, 2027", "10:00 AM – 01:00 PM", "State Bare Acts & Landmark Judgments", "https://upsc.gov.in"),

        # Agriculture Exams (AGRI)
        ("ICAR AIEEA PG 2027 (Indian Council of Agricultural Research)", "National Testing Agency (NTA)", "govt", "MSc Agriculture Admissions", "BSc Agriculture / Horticulture / Forestry degree.", "120 Objective MCQs (2 Hours) in Agricultural Sciences & Agronomy.", "March 01, 2027", "April 15, 2027", "May 25, 2027", "10:00 AM – 12:00 PM", "ICAR Agriculture Prep Guide by Nem Raj Sunda", "https://icar.nta.ac.in"),
        ("IBPS Agriculture Field Officer (IBPS AFO 2026)", "Institute of Banking Personnel Selection", "govt", "Agri Banking Specialist Officer", "4-Year BSc Agriculture / Agri Engineering.", "Prelims Aptitude + Professional Knowledge Test (Agri 60 Qs) + Interview.", "November 01, 2026", "November 21, 2026", "December 27, 2026", "Morning Shift: 09:30 AM", "IBPS AFO Agri Master Book", "https://www.ibps.in"),

        # Design Exams (BDA)
        ("CEED 2027 (Common Entrance Examination for Design)", "IIT Bombay / CEED Committee", "private", "Master of Design (M.Des) Admissions", "Degree in Design (BDA) / Engineering / Architecture / Fine Arts.", "Part A (CBT Visualization & Aptitude) + Part B (Drawing & Design Problem Solving).", "October 01, 2026", "November 15, 2026", "January 17, 2027", "09:00 AM – 12:00 PM", "CEED Past Question Papers & Sketchbook", "https://www.ceed.iitb.ac.in"),
        ("NID DAT 2027 (Design Aptitude Test)", "National Institute of Design", "govt", "B.Des / M.Des Admissions", "10+2 / BDA / Graduate in any stream.", "DAT Prelims (Design Aptitude & Creativity) + DAT Mains (Studio Test & Personal Interview).", "September 15, 2026", "December 01, 2026", "December 27, 2026", "10:00 AM – 01:00 PM", "NID Official Design Studio Workbook", "https://admissions.nid.edu"),

        # Diploma Exams (DIPLOMA)
        ("State Lateral Entry CET 2027 (Diploma to B.Tech)", "State Examinations Authority", "govt", "B.Tech 2nd Year Direct Admission", "3-Year Diploma in Engineering / Polytechnic.", "120 MCQs testing Engineering Mathematics, Physics, Chemistry, and Branch Fundamentals.", "March 15, 2027", "April 30, 2027", "June 06, 2027", "10:00 AM – 01:00 PM", "Lateral Entry CET Solved Question Papers", "https://cetonline.karnataka.gov.in"),
        ("RRB Junior Engineer (RRB JE 2026)", "Railway Recruitment Boards", "govt", "Railway Technical Services", "3-Year Diploma or BE/BTech in Civil/Mech/EEE/ECE.", "CBT-1 (General Science & Quant) + CBT-2 (Technical Abilities & Computer Apps).", "August 10, 2026", "September 15, 2026", "November 14, 2026", "Shift 1: 09:00 AM", "RRB JE Technical Master Guide", "https://www.rrbcdg.gov.in"),

        # Technical & GATE Exams (BTECH, BCA, MCA, MTECH, BSC)
        ("GATE 2027 (Computer Science & IT - CS)", "IIT Kharagpur / IISc / GATE Committee", "govt", "Computer Science & IT", "BE / B.Tech / MCA / MSc completed or final year.", "CS/IT Core (33%), Aptitude (15%), Engg Math (12%). 65 Qs.", "August 30, 2026", "October 12, 2026", "February 06, 2027", "09:30 AM – 12:30 PM", "GATE Previous Papers, NPTEL", "https://gate.iitk.ac.in"),
        ("GATE 2027 (Electronics & Communication - EC)", "GATE Committee", "govt", "Electronics & Comm", "BE / B.Tech in ECE/EEE.", "Networks, Signals & Systems, Analog/Digital Circuits, Electromagnetics.", "August 30, 2026", "October 12, 2026", "February 07, 2027", "02:30 PM – 05:30 PM", "GATE EC Solved Papers, NPTEL", "https://gate.iitk.ac.in"),
        ("GATE 2027 (Electrical Engineering - EE)", "GATE Committee", "govt", "Electrical Engineering", "BE / B.Tech in Electrical/EEE.", "Power Systems, Electrical Machines, Control Systems, Power Electronics.", "August 30, 2026", "October 12, 2026", "February 13, 2027", "09:30 AM – 12:30 PM", "GATE EE Solved Papers", "https://gate.iitk.ac.in"),
        ("GATE 2027 (Mechanical Engineering - ME)", "GATE Committee", "govt", "Mechanical Engineering", "BE / B.Tech in Mechanical/Automobile.", "Thermodynamics, Fluid Mechanics, CAD/CAM, Manufacturing Technology.", "August 30, 2026", "October 12, 2026", "February 14, 2027", "02:30 PM – 05:30 PM", "GATE ME Practice Sets", "https://gate.iitk.ac.in"),
        ("GATE 2027 (Civil Engineering - CE)", "GATE Committee", "govt", "Civil Engineering", "BE / B.Tech in Civil/Construction.", "Structural Engg, Geotechnical, Environmental, Transportation Engg.", "August 30, 2026", "October 12, 2026", "February 13, 2027", "02:30 PM – 05:30 PM", "NPTEL Civil Video Series", "https://gate.iitk.ac.in"),

        # PSU & Govt Exams
        ("ISRO Scientist/Engineer 'SC' Recruitment Exam", "ISRO Centralised Recruitment Board", "govt", "Space Science & Tech", "BE/B.Tech with minimum 65% aggregate.", "80 Objective Qs on core discipline + Interview.", "September 15, 2026", "October 10, 2026", "December 20, 2026", "10:00 AM – 12:00 PM", "ISRO Scientist Previous Papers", "https://www.isro.gov.in"),
        ("DRDO Scientist 'B' Entrance (RAC)", "DRDO Recruitment & Assessment Centre", "govt", "Defense R&D", "BE/BTech + Valid GATE Score.", "Descriptive Test (800 Marks) + Personal Interview.", "September 01, 2026", "October 20, 2026", "January 17, 2027", "09:30 AM – 12:30 PM", "RAC DRDO Official Syllabus Guide", "https://rac.gov.in"),
        ("NIC Scientist 'B' & Technical Assistant Exam", "National Informatics Centre (NIELIT)", "govt", "Govt IT & Cloud", "BE/BTech/MCA/MSc in CS/IT/ECE.", "120 Objective Qs (78 Technical + 42 Generic Aptitude).", "October 05, 2026", "November 15, 2026", "February 21, 2027", "10:00 AM – 01:00 PM", "NIELIT Official Question Bank", "https://www.nic.in"),

        # Banking & Commerce Exams (BCOM, MCOM, BBA, MBA, BA)
        ("IBPS Probationary Officer (IBPS PO XVI)", "Institute of Banking Personnel Selection", "govt", "Banking & Finance", "Degree in any discipline (BCom/BBA/BA/BSc/BTech).", "Prelims + Mains + Interview.", "August 01, 2026", "August 25, 2026", "October 18, 2026", "Multiple Shifts Daily", "Oliveboard Test Series", "https://www.ibps.in"),
        ("SBI Probationary Officer (SBI PO 2026)", "State Bank of India", "govt", "Bank Management", "Graduate in any discipline.", "Prelims (100M) + Mains (200M + 50M Descriptive) + Psychometric Test.", "September 07, 2026", "September 27, 2026", "November 29, 2026", "Shift 1: 09:00 AM", "SBI PO Master Mock Series", "https://bank.sbi/careers"),
        ("RBI Grade B Officer Examination 2026", "Reserve Bank of India Services Board", "govt", "Central Banking Policy", "Graduate with min 60% marks.", "Phase I CBT + Phase II (Economic & Social Issues, Finance & Mgmt).", "July 15, 2026", "August 05, 2026", "September 08, 2026", "Morning & Afternoon Sessions", "Edutap RBI Grade B Notes", "https://www.rbi.org.in"),
        ("NTA UGC NET (Commerce & Finance)", "National Testing Agency", "govt", "Academia & Research", "Master's Degree in Commerce (M.Com / MBA Finance).", "Paper 1 (100M) + Paper 2 Commerce & Financial Accounting (200M).", "May 10, 2026", "June 05, 2026", "July 14, 2026", "09:00 AM – 12:00 PM", "Trueman UGC NET Commerce Guide", "https://ugcnet.nta.ac.in"),

        # Management Admissions (CAT, MAT, XAT)
        ("CAT 2026 (Common Admission Test for IIMs)", "IIM Kozhikode / IIM Committee", "private", "Management Admissions (MBA/PGDM)", "Bachelor's Degree with minimum 50% aggregate.", "66 Questions (2 Hours): VARC, DILR, Quantitative Ability.", "August 02, 2026", "September 20, 2026", "November 29, 2026", "Slot 1: 08:30 AM | Slot 2: 12:30 PM", "Arun Sharma Quant & VARC", "https://iimcat.ac.in"),
        ("XAT 2027 (Xavier Aptitude Test)", "XLRI Jamshedpur", "private", "MBA / Business Management", "Bachelor's Degree in any stream.", "Verbal Ability, Decision Making, Quantitative Ability, General Knowledge.", "July 15, 2026", "December 10, 2026", "January 03, 2027", "02:00 PM – 05:30 PM", "XLRI Official Decision Making Series", "https://xatonline.in"),

        # Professional Certifications
        ("AWS Certified Solutions Architect - Associate (SAA-C03)", "Amazon Web Services", "private", "Cloud Architecture Certification", "Basic knowledge of AWS services and cloud concepts.", "65 Multiple Choice Questions (130 Mins).", "Open Year-Round", "Anytime", "On-Demand", "Flexible Daily Slots", "AWS Official Exam Simulator", "https://aws.amazon.com/certification"),
        ("Microsoft Certified: Azure Fundamentals (AZ-900)", "Microsoft", "private", "Cloud Foundation Certification", "No prerequisites. Open to all students.", "40-60 Questions (60 Mins) covering Azure Services.", "Open Year-Round", "Anytime", "On-Demand", "Flexible Daily Slots", "Microsoft Learn AZ-900", "https://learn.microsoft.com"),
        ("Chartered Financial Analyst (CFA Level 1)", "CFA Institute", "private", "Global Investment & Finance", "Final year Bachelor's degree or completed degree.", "180 Multiple Choice Questions (4.5 Hours).", "Quarterly Exams", "Window Based", "November 2026", "Shift 1: 08:00 AM", "Schweser Notes for CFA Level 1", "https://www.cfainstitute.org"),
        ("CompTIA Security+ (SY0-701)", "CompTIA", "private", "Global Cybersecurity Benchmark", "Networking fundamentals or IT experience.", "Max 90 Questions (90 Mins).", "Open Year-Round", "Anytime", "On-Demand", "Flexible Daily Slots", "CompTIA Security+ Guide", "https://www.comptia.org"),
    ]

    added_exams = 0
    for exam_name, body, cat, dom, elig, syl, s_date, l_date, e_date, timings, res, url in exams_master:
        exam, created = GovernmentExam.objects.get_or_create(
            exam_name=exam_name,
            defaults={
                'conducting_body': body,
                'category': cat,
                'domain': dom,
                'eligibility': elig,
                'syllabus_summary': syl,
                'application_start_date': s_date,
                'application_last_date': l_date,
                'exam_date': e_date,
                'exam_timings': timings,
                'preparation_resources': res,
                'website_url': url,
                'is_active': True
            }
        )
        if created:
            added_exams += 1

    print(f"Seeded {added_exams} new Competitive & Certification Exams (Total Exams in DB: {GovernmentExam.objects.count()}).")
    print("Master Seed Completed Successfully for ALL 15 Degrees!")

if __name__ == "__main__":
    seed_master_50_data()
