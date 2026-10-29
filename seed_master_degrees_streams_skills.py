import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from profiles.models import Degree, Stream, Skill

def seed_degrees_streams_and_skills():
    print("Starting master seed for all 32 Degrees, Streams, and Key Skills...")

    # Data mapping dictionary of 32 Degrees, Streams & Skills
    master_data = {
        ("BE / BTech — Engineering", "BTECH"): [
            ("Computer Science Engineering (CSE)", ["Python", "Java", "C++", "Data Structures & Algorithms", "SQL & Databases", "Operating Systems", "Computer Networks", "Git & GitHub"]),
            ("Information Science / Technology", ["Programming", "Web Development", "SQL & Databases", "AWS & Cloud Computing", "Cybersecurity & Networking"]),
            ("Artificial Intelligence", ["Python", "Machine Learning", "Deep Learning & PyTorch", "NLP", "Mathematics & Statistics"]),
            ("AI & Machine Learning", ["Python", "Scikit-Learn", "Deep Learning & PyTorch", "Machine Learning", "Statistics"]),
            ("Data Science", ["Python", "SQL & Databases", "Statistics", "Pandas & NumPy", "Machine Learning", "Data Visualization (Tableau/PowerBI)"]),
            ("Data Engineering", ["Python", "SQL & Databases", "ETL Pipelines", "Apache Spark", "AWS & Cloud Computing"]),
            ("Cyber Security", ["Cybersecurity & Networking", "Linux", "Ethical Hacking", "Cryptography", "SIEM"]),
            ("Cloud Computing", ["AWS & Cloud Computing", "Linux", "Docker & Kubernetes", "Cybersecurity & Networking"]),
            ("Software Engineering", ["Programming", "Software Development Lifecycle", "Git & GitHub", "Software Testing", "System Design"]),
            ("Computer Engineering", ["C/C++", "Embedded C / Microcontrollers", "Operating Systems", "Networks", "Hardware Design"]),
            ("Electronics & Communication (ECE)", ["Digital Electronics", "Communication Systems", "Embedded C / Microcontrollers", "MATLAB & Simulink"]),
            ("Electrical & Electronics (EEE)", ["Circuit Analysis", "Power Systems", "Control Systems", "MATLAB & Simulink"]),
            ("Electrical Engineering", ["Electrical Machines", "Power Systems", "PLC & SCADA Automation", "AutoCAD"]),
            ("Electronics Engineering", ["Electronics", "PCB Design", "Microcontrollers", "Embedded C / Microcontrollers"]),
            ("Instrumentation Engineering", ["Sensors & Transducers", "PLC & SCADA Automation", "Control Systems"]),
            ("Mechanical Engineering", ["CAD & SolidWorks", "CAM & CNC Machining", "Manufacturing Technology", "Thermodynamics"]),
            ("Mechatronics", ["Robotics & Automation", "PLC & SCADA Automation", "CAD & SolidWorks", "Embedded C / Microcontrollers"]),
            ("Automobile Engineering", ["Automotive Systems", "CAD & SolidWorks", "EV Battery Technology", "Mechanics"]),
            ("Civil Engineering", ["AutoCAD", "STAAD.Pro", "Structural Analysis & ETABS", "Land Surveying"]),
            ("Construction Engineering", ["Construction Project Management", "AutoCAD", "Cost Estimation", "Site Safety"]),
            ("Aerospace Engineering", ["Aerodynamics", "Propulsion Systems", "CAD & SolidWorks", "MATLAB & Simulink"]),
            ("Aeronautical Engineering", ["Aircraft Design", "Aerodynamics", "Propulsion Systems"]),
            ("Chemical Engineering", ["Chemical Process Design", "Thermodynamics", "MATLAB & Simulink", "Chemical Safety"]),
            ("Biotechnology", ["Molecular Biology", "Bioinformatics", "Laboratory Techniques"]),
            ("Biomedical Engineering", ["Medical Devices & Instrumentation", "Electronics", "Biomaterials", "MATLAB & Simulink"]),
            ("Environmental Engineering", ["Waste Management", "Water Treatment", "GIS Mapping"]),
            ("Industrial Engineering", ["Operations Research", "Lean Manufacturing", "Six Sigma", "Process Optimization"]),
            ("Production Engineering", ["Manufacturing Technology", "CNC Programming", "CAD & SolidWorks", "Quality Control"]),
            ("Metallurgical Engineering", ["Materials Science", "Metallurgy", "Materials Testing"]),
            ("Mining Engineering", ["Mine Planning", "Geology", "Industrial Safety", "Surveying"]),
            ("Petroleum Engineering", ["Drilling Technology", "Reservoir Engineering", "Geology"]),
            ("Textile Engineering", ["Textile Manufacturing", "CAD & SolidWorks", "Fabric Technology"]),
            ("Food Technology", ["Food Processing", "Quality Control", "Food Safety & Standards"]),
            ("Agricultural Engineering", ["Farm Machinery", "Irrigation Engineering", "Soil & Water Management"]),
            ("Marine Engineering", ["Marine Machinery", "Ship Systems", "Maritime Safety"]),
            ("Robotics Engineering", ["ROS (Robot OS)", "Python", "C++", "Sensors", "Computer Vision"]),
            ("IoT Engineering", ["Arduino", "Raspberry Pi", "Sensors", "MQTT Protocol", "AWS & Cloud Computing"]),
            ("VLSI", ["Verilog HDL", "VHDL", "Digital Logic Design", "FPGA", "ASIC Design"]),
            ("Embedded Systems", ["Embedded C / Microcontrollers", "C++", "RTOS", "IoT"]),
            ("Semiconductor Engineering", ["VLSI", "Semiconductor Physics", "Chip Fabrication"]),
            ("Nanotechnology", ["Nanomaterials", "Chemistry", "Materials Science"]),
            ("Renewable Energy", ["Solar PV Technology", "Wind Energy", "Energy Storage", "Power Electronics"])
        ],

        ("ME / MTech — Masters in Engineering", "MTECH"): [
            ("CSE (Advanced)", ["Advanced Programming", "Algorithms", "AI & Machine Learning", "Cloud Infrastructure"]),
            ("AI & ML (Advanced)", ["Deep Learning & PyTorch", "NLP", "Computer Vision", "Python"]),
            ("Data Science (Advanced)", ["Statistics", "Machine Learning", "Big Data Analytics", "Python", "SQL & Databases"]),
            ("Cyber Security (Advanced)", ["Cryptography", "Network Security", "Digital Forensics"]),
            ("Software Engineering (Advanced)", ["Software Architecture", "DevOps & CI/CD", "Software Testing", "System Design"]),
            ("VLSI (Advanced)", ["Verilog HDL", "FPGA", "ASIC Design", "Digital Logic Design"]),
            ("Embedded Systems (Advanced)", ["Embedded C / Microcontrollers", "RTOS", "IoT"]),
            ("Communication Engineering", ["RF Engineering", "Wireless Communication", "Signal Processing"]),
            ("Power Systems", ["Smart Grid", "Power Electronics", "Power System Protection"]),
            ("Control Systems", ["MATLAB & Simulink", "PLC & SCADA Automation"]),
            ("Structural Engineering", ["Structural Analysis & ETABS", "STAAD.Pro"]),
            ("Thermal Engineering", ["Thermodynamics", "Heat Transfer", "CFD Simulations"]),
            ("Manufacturing Engineering", ["CNC Programming", "CAD & SolidWorks", "Industrial Automation"]),
            ("Machine Design", ["CAD & SolidWorks", "FEA Analysis"]),
            ("Biotechnology (Advanced)", ["Bioinformatics", "Molecular Biology", "Advanced Research"]),
            ("Biomedical Engineering (Advanced)", ["Medical Imaging", "Biomedical Devices"])
        ],

        ("MBBS — Medical & Surgery", "MBBS"): [
            ("General Medicine", ["Clinical Diagnostics", "Patient Management", "Clinical Examination"]),
            ("General Surgery", ["Surgical Techniques", "Anatomy", "Emergency Trauma Care"]),
            ("Cardiology", ["ECG Interpretation", "Cardiac Diagnosis", "Patient Care"]),
            ("Neurology", ["Neurological Examination", "Clinical Diagnosis"]),
            ("Neurosurgery", ["Neurosurgery", "Neuroanatomy", "Critical Care"]),
            ("Paediatrics", ["Child Healthcare", "Pediatric Diagnostics", "Patient Communication"]),
            ("Dermatology", ["Skin Diagnosis", "Dermatological Procedures"]),
            ("Psychiatry", ["Mental Health Assessment", "Counseling & Psychotherapy"]),
            ("Orthopaedics", ["Musculoskeletal Diagnosis", "Orthopedic Surgery"]),
            ("Obstetrics & Gynaecology", ["Pregnancy Care", "Gynecological Surgery", "Women's Health"]),
            ("Anaesthesiology", ["Anaesthesia Administration", "Airway Management", "Critical Care"]),
            ("Radiology & Imaging", ["Medical Imaging (CT/MRI/Ultrasound)", "X-Ray Diagnostics"]),
            ("Pathology", ["Histopathology", "Laboratory Diagnosis"]),
            ("Microbiology", ["Microbial Testing", "Infection Control"]),
            ("Pharmacology", ["Drug Therapy", "Clinical Research & Pharmacology"]),
            ("Forensic Medicine", ["Forensic Examination", "Medical Jurisprudence"]),
            ("Community Medicine", ["Epidemiology", "Public Health Management"]),
            ("Emergency Medicine", ["Emergency Trauma Care", "Critical Care"]),
            ("Oncology", ["Cancer Diagnosis", "Treatment Planning"]),
            ("Nephrology", ["Kidney Disease Management", "Dialysis Operations"]),
            ("Gastroenterology", ["GI Diagnosis", "Endoscopy"]),
            ("Endocrinology", ["Hormonal Disorders", "Diabetes Management"]),
            ("Pulmonology", ["Respiratory Diagnostics", "Critical Care"]),
            ("Ophthalmology", ["Eye Examination", "Ophthalmic Surgery"]),
            ("ENT (Otorhinolaryngology)", ["ENT Diagnostics", "ENT Surgery"]),
            ("Family Medicine", ["Primary Care Diagnostics", "Preventive Medicine"])
        ],

        ("BDS — Dentistry", "BDS"): [
            ("Oral Medicine", ["Oral Examination & Diagnosis", "Patient Care"]),
            ("Oral Surgery", ["Dental Surgery", "Tooth Extraction"]),
            ("Orthodontics", ["Braces & Aligners", "Dental Correction"]),
            ("Prosthodontics", ["Dentures & Crowns", "Dental Implants"]),
            ("Periodontics", ["Gum Disease Treatment", "Periodontal Surgery"]),
            ("Conservative Dentistry & Endodontics", ["Restorative Dentistry", "Root Canal Treatment"]),
            ("Pedodontics", ["Pediatric Dentistry", "Child Care"]),
            ("Oral Pathology", ["Biopsy Analysis", "Histopathology"]),
            ("Public Health Dentistry", ["Community Dental Health", "Preventive Care"]),
            ("Dental Radiology", ["Dental X-Ray Imaging", "Oral Diagnostics"]),
            ("Cosmetic Dentistry", ["Smile Design", "Dental Veneers"])
        ],

        ("BCom — Bachelor of Commerce", "BCOM"): [
            ("General Commerce", ["Accounting & Taxation", "Business Economics", "Business Law"]),
            ("Accounting & Finance", ["Tally Prime & GST", "Financial Modeling & Excel", "Corporate Finance & Valuation"]),
            ("Banking & Finance", ["Banking Operations", "Financial Services", "Financial Modeling & Excel"]),
            ("Corporate Accounting", ["Accounting Standards", "Financial Statement Preparation"]),
            ("Taxation", ["GST Compliance", "Income Tax Filing", "Tax Planning"]),
            ("Computer Applications (BCom CA)", ["Financial Modeling & Excel", "Tally Prime & GST", "SQL & Databases", "Business Software"]),
            ("International Business", ["Global Trade", "Export-Import Procedures", "Economics"]),
            ("E-Commerce", ["Digital Marketing & SEO", "E-Commerce Management"]),
            ("Business Analytics", ["Financial Modeling & Excel", "SQL & Databases", "Data Visualization (Tableau/PowerBI)", "Statistics"]),
            ("Financial Markets", ["Investment Analysis", "Stock Markets", "Corporate Finance & Valuation"]),
            ("Auditing", ["Statutory Audit", "Accounting & Taxation", "Regulatory Compliance"]),
            ("Cost Accounting", ["Cost Accounting", "Budgeting", "Financial Analysis"])
        ],

        ("MCom — Master of Commerce", "MCOM"): [
            ("Advanced Accounting", ["Advanced Financial Reporting", "Accounting Standards"]),
            ("Corporate Finance", ["Corporate Finance & Valuation", "Investment Analysis", "Financial Modeling & Excel"]),
            ("Banking Operations", ["Central Banking", "Financial Risk Management"]),
            ("Taxation (Advanced)", ["GST Compliance", "Income Tax Planning", "International Tax"]),
            ("Marketing & Analytics", ["Digital Marketing & SEO", "Market Research"]),
            ("Business Analytics (Advanced)", ["Financial Modeling & Excel", "SQL & Databases", "Data Visualization (Tableau/PowerBI)"]),
            ("Economics & Econometrics", ["Econometrics", "Statistical Analysis", "Economic Policy"]),
            ("Corporate Secretaryship", ["Corporate Law", "Board Compliance"])
        ],

        ("BCA — Bachelor of Computer Applications", "BCA"): [
            ("General Computer Applications", ["Programming", "SQL & Databases", "Operating Systems"]),
            ("Software Development", ["Java", "Python", "C++", "Git & GitHub"]),
            ("Web Development", ["HTML & CSS", "JavaScript", "React", "Node.js"]),
            ("Mobile App Development", ["Java", "Flutter", "Android SDK"]),
            ("Data Science & Analytics", ["Python", "SQL & Databases", "Statistics", "Machine Learning"]),
            ("AI & ML", ["Python", "Machine Learning", "Deep Learning & PyTorch"]),
            ("Cyber Security", ["Linux", "Cybersecurity & Networking", "Ethical Hacking"]),
            ("Cloud Computing", ["AWS & Cloud Computing", "Linux", "Docker & Kubernetes"]),
            ("Data Analytics", ["Financial Modeling & Excel", "SQL & Databases", "Data Visualization (Tableau/PowerBI)", "Python"]),
            ("Computer Networking", ["TCP/IP", "Linux", "Cybersecurity & Networking"]),
            ("Database Management", ["SQL & Databases", "MySQL", "PostgreSQL"]),
            ("Game Development", ["Unity 3D", "C++", "UI/UX Design & Figma"]),
            ("IoT Applications", ["Arduino", "Raspberry Pi", "Sensors"])
        ],

        ("MCA — Master of Computer Applications", "MCA"): [
            ("Software Engineering", ["Software Development Lifecycle", "Java", "Python", "Software Testing"]),
            ("AI & Machine Learning", ["Python", "Deep Learning & PyTorch", "Machine Learning"]),
            ("Data Science & Big Data", ["Python", "SQL & Databases", "Statistics", "Machine Learning"]),
            ("Cyber Security & Cryptography", ["Ethical Hacking", "Linux", "Cryptography"]),
            ("Cloud & DevOps", ["AWS & Cloud Computing", "Docker & Kubernetes", "CI/CD Pipelines"]),
            ("Web Technologies", ["React", "Node.js", "REST APIs", "SQL & Databases"]),
            ("Mobile Computing", ["Android SDK", "Flutter", "Mobile Architecture"]),
            ("Database Architecture", ["SQL & Databases", "PostgreSQL", "MongoDB"]),
            ("Networking & Security", ["TCP/IP", "Linux", "Cybersecurity & Networking"]),
            ("Big Data Systems", ["Hadoop", "Apache Spark", "Python", "Data Engineering"]),
            ("Blockchain Tech", ["Solidity", "Smart Contracts", "Web3", "Cybersecurity & Networking"]),
            ("DevOps Systems", ["Git & GitHub", "Docker & Kubernetes", "Jenkins CI/CD"])
        ],

        ("BBA — Bachelor of Business Administration", "BBA"): [
            ("General Management", ["Business Leadership", "Communication & Public Speaking", "Business Strategy"]),
            ("Finance", ["Financial Modeling & Excel", "Corporate Finance & Valuation", "Accounting & Taxation"]),
            ("Marketing", ["Digital Marketing & SEO", "Sales Strategy", "Brand Management"]),
            ("Human Resource (HR)", ["Talent Acquisition", "Human Resource Management", "Communication & Public Speaking"]),
            ("International Business", ["Global Trade", "Export Import Strategy"]),
            ("Business Analytics", ["Financial Modeling & Excel", "SQL & Databases", "Data Visualization (Tableau/PowerBI)"]),
            ("Entrepreneurship", ["Business Planning", "Innovation Management", "Venture Pitching"]),
            ("Logistics & Supply Chain", ["Supply Chain & Operations", "Inventory Management", "SAP ERP"]),
            ("E-Commerce Management", ["Digital Marketing & SEO", "E-Commerce Operations"]),
            ("Retail Management", ["Retail Sales", "Inventory Control", "Customer Service"])
        ],

        ("MBA — Master of Business Administration", "MBA"): [
            ("Finance (Advanced)", ["Financial Modeling & Excel", "Corporate Finance & Valuation", "Investment Banking"]),
            ("Marketing (Advanced)", ["Digital Marketing & SEO", "Brand Strategy", "Consumer Psychology"]),
            ("HR & Talent Management", ["Human Resource Management", "HR Analytics", "Talent Management"]),
            ("Operations & Supply Chain", ["Supply Chain & Operations", "Lean Manufacturing", "Six Sigma"]),
            ("Business Analytics (MBA)", ["SQL & Databases", "Python", "Data Visualization (Tableau/PowerBI)"]),
            ("IT & Systems Management", ["IT Project Management", "AWS & Cloud Computing", "ERP Systems"]),
            ("International Business (MBA)", ["Global Business Strategy", "International Trade"]),
            ("Product Management", ["Product Strategy", "Agile & Project Management", "UI/UX Design & Figma"]),
            ("Digital Marketing & Growth", ["Digital Marketing & SEO", "SEM & Social Ads", "Growth Analytics"]),
            ("Project Management", ["Agile & Project Management", "Scrum Framework", "JIRA"]),
            ("Business Intelligence", ["Data Visualization (Tableau/PowerBI)", "SQL & Databases", "Business Analysis"])
        ],

        ("BMS — Bachelor of Management Studies", "BMS"): [
            ("Finance Management", ["Accounting & Taxation", "Financial Modeling & Excel", "Financial Analysis"]),
            ("Marketing Management", ["Digital Marketing & SEO", "Sales Management"]),
            ("HR Management", ["Human Resource Management", "Communication & Public Speaking"]),
            ("Operations Management", ["Supply Chain & Operations", "Business Process Optimization"]),
            ("Business Analytics", ["Financial Modeling & Excel", "SQL & Databases", "Data Visualization (Tableau/PowerBI)"])
        ],

        ("BA — Bachelor of Arts", "BA"): [
            ("English Literature & Writing", ["Creative Writing", "Communication & Public Speaking", "Content Editing"]),
            ("Economics", ["Statistical Analysis", "Economic Policy", "Data Analysis"]),
            ("History & Archival Research", ["Historical Research", "Archival Analysis"]),
            ("Political Science", ["Political Analysis", "Policy Research", "Public Administration"]),
            ("Sociology", ["Social Research", "Survey Design", "Data Analysis"]),
            ("Psychology", ["Psychological Counseling", "Behavioral Assessment", "Research Methods"]),
            ("Geography & GIS", ["GIS Mapping", "Spatial Analysis", "Geographic Research"]),
            ("Journalism & Mass Comm", ["Journalism & News Reporting", "Media Production", "Video Editing"]),
            ("Public Administration", ["Public Policy", "Administrative Governance"]),
            ("Fine Arts & Visual Media", ["Drawing & Painting", "UI/UX Design & Figma", "Visual Art"]),
            ("Social Work (BSW)", ["Community Counseling", "Social Welfare Work"]),
            ("Economics & Mathematics", ["Statistics", "Econometrics", "Data Analysis"])
        ],

        ("MA — Master of Arts", "MA"): [
            ("English (Advanced)", ["Academic Writing", "Content Editing", "Literary Analysis"]),
            ("Economics (Advanced)", ["Econometrics", "Advanced Statistics", "Data Analysis"]),
            ("Political Science (Advanced)", ["Policy Analysis", "International Relations", "Political Research"]),
            ("Psychology (Advanced)", ["Clinical Counseling", "Psychological Assessment", "Research Methods"]),
            ("Journalism & Digital Media", ["Digital Journalism", "Media Ethics", "Video Editing"]),
            ("International Relations", ["Diplomacy", "Global Policy Analysis", "Strategic Research"])
        ],

        ("BSc — Bachelor of Science", "BSC"): [
            ("Physics", ["Physics Laboratory", "Mathematics", "MATLAB & Simulink"]),
            ("Chemistry", ["Analytical Chemistry", "Laboratory Techniques", "Chemical Safety"]),
            ("Mathematics", ["Calculus", "Statistics", "Python Programming"]),
            ("Computer Science", ["Programming", "SQL & Databases", "Data Structures & Algorithms"]),
            ("Information Technology", ["Web Development", "Networks", "SQL & Databases"]),
            ("Data Science", ["Python", "SQL & Databases", "Statistics", "Machine Learning"]),
            ("AI & Machine Learning", ["Python", "Machine Learning", "Mathematics"]),
            ("Biotechnology", ["Molecular Biology", "Laboratory Techniques", "Bioinformatics"]),
            ("Microbiology", ["Microbiology Testing", "Laboratory Diagnostics"]),
            ("Biochemistry", ["Biochemistry Assays", "Laboratory Research"]),
            ("Zoology", ["Animal Biology", "Biological Research"]),
            ("Botany", ["Plant Science", "Biological Research"]),
            ("Environmental Science", ["Environmental Impact Analysis", "GIS Mapping"]),
            ("Forensic Science", ["Forensic Laboratory Analysis", "Evidence Testing"]),
            ("Food Science & Nutrition", ["Food Quality Testing", "Nutrition Planning"]),
            ("Agriculture", ["Agronomy", "Soil Science", "Farm Management"])
        ],

        ("MSc — Master of Science", "MSC"): [
            ("Computer Science (MSc)", ["Advanced Algorithms", "Python", "System Architecture"]),
            ("Data Science (MSc)", ["Python", "Machine Learning", "Statistics", "Big Data"]),
            ("AI & Machine Learning (MSc)", ["Deep Learning & PyTorch", "NLP", "Computer Vision"]),
            ("Physics (MSc)", ["Quantum Physics", "MATLAB & Simulink", "Simulations"]),
            ("Chemistry (MSc)", ["Organic Chemistry", "Analytical Instrumentation"]),
            ("Biotechnology (MSc)", ["Genomics", "Bioinformatics", "Molecular Research"]),
            ("Microbiology (MSc)", ["Microbial Research", "Laboratory Diagnostics"]),
            ("Environmental Science (MSc)", ["Environmental Monitoring", "GIS Mapping"]),
            ("Forensic Science (MSc)", ["Forensic Crime Analysis", "Lab Diagnostics"])
        ],

        ("B.Pharm / D.Pharm — Pharmacy", "BPHARM"): [
            ("Pharmaceutics", ["Drug Formulation", "Pharmaceutical Manufacturing"]),
            ("Pharmacology", ["Pharmacology & Drug Action", "Clinical Trial Operations"]),
            ("Pharmaceutical Chemistry", ["Drug Synthesis", "Laboratory Instrumentation"]),
            ("Pharmaceutical Analysis", ["HPLC Testing", "Spectroscopy", "Quality Assurance"]),
            ("Clinical Pharmacy", ["Patient Care", "Medication Advisory"]),
            ("Regulatory Affairs", ["Drug Regulation Documentation", "FDA Compliance"]),
            ("Pharmacovigilance", ["Drug Safety Monitoring", "Adverse Event Reporting"]),
            ("Quality Control & Assurance", ["GMP Compliance", "Quality Control Testing"]),
            ("Medical Writing", ["Technical Writing & Documentation", "Scientific Reporting"])
        ],

        ("ITI / Diploma — Vocational & Polytechnic", "DIPLOMA"): [
            ("Electrician Trade", ["Electrical Wiring", "Circuit Troubleshooting", "Safety Protocols"]),
            ("Fitter Trade", ["Machine Fitting", "Bench Tool Operations", "Assembly"]),
            ("Welder Trade", ["Arc Welding", "Metal Fabrication"]),
            ("Plumber Trade", ["Plumbing Systems", "Piping Installation"]),
            ("Turner / Machinist Trade", ["Lathe Operation", "CNC Machining", "Industrial Maintenance & Machining"]),
            ("COPA (Computer Operator)", ["Computer Fundamentals", "MS Office & Tally", "Basic Web Design"]),
            ("Electronics Mechanic Trade", ["Electronics Circuit Repair", "PCB Soldering"]),
            ("Mechanic Motor Vehicle", ["Automobile Repair", "Engine Maintenance"]),
            ("Draughtsman Civil", ["AutoCAD", "Technical Engineering Drawing"]),
            ("Draughtsman Mechanical", ["CAD & SolidWorks", "Engineering Drawing"]),
            ("Refrigeration & AC", ["HVAC Systems", "Refrigeration Repair"]),
            ("Solar Technician", ["Solar Panel Installation", "Electrical Connections"]),
            ("Diploma Civil Engineering", ["AutoCAD", "Site Supervision", "Structural Detailing"]),
            ("Diploma Mechanical Engineering", ["CAD & SolidWorks", "CNC Programming", "Machine Maintenance"]),
            ("Diploma Electrical Engineering", ["Electrical Systems", "PLC & SCADA Automation"]),
            ("Diploma Electronics Engineering", ["Electronics", "Embedded C / Microcontrollers"]),
            ("Diploma Automobile Engineering", ["Automobile Repair", "CAD Drafting"])
        ],

        ("B.Arch — Bachelor of Architecture", "BARCH"): [
            ("Architectural Design", ["AutoCAD", "SketchUp", "Revit BIM"]),
            ("Urban Design & Planning", ["GIS Mapping", "Urban Infrastructure Planning"]),
            ("Interior Architecture", ["3D Modeling & Rendering", "Interior Layout Design"]),
            ("Sustainable Architecture", ["Green Building Design", "Energy Efficiency"]),
            ("Construction Management", ["Building Project Management", "Cost Estimation"])
        ],

        ("M.Arch — Master of Architecture", "MARCH"): [
            ("Advanced Architectural Design", ["BIM Architecture", "Parametric Design (Rhino/Grasshopper)"]),
            ("Urban Planning & Design", ["Urban Planning", "GIS Mapping"]),
            ("Sustainable & Environmental Arch", ["Building Energy Modeling", "Sustainability Audit"])
        ],

        ("CA — Chartered Accountancy", "CA"): [
            ("Statutory Financial Audit", ["Statutory Audit", "Accounting Standards", "Financial Reporting"]),
            ("Direct & Indirect Taxation", ["Income Tax Planning", "GST Compliance", "Tax Filing"]),
            ("Corporate Financial Management", ["Corporate Finance & Valuation", "Financial Modeling & Excel"]),
            ("Management Accounting & Costing", ["Cost Accounting", "Budgetary Control"]),
            ("Forensic Accounting & Investigation", ["Forensic Audit", "Financial Fraud Investigation"]),
            ("Internal Audit & Controls", ["Internal Risk Controls", "Audit Compliance"])
        ],

        ("BFA — Fine Arts & Visual Arts", "BFA"): [
            ("Painting & Visual Art", ["Drawing & Painting", "Art Composition"]),
            ("Applied Arts & Graphic Design", ["UI/UX Design & Figma", "Graphic Illustration", "Advertising Design"]),
            ("Digital Art & Animation", ["Digital Painting", "2D/3D Animation", "UI/UX Design & Figma"]),
            ("Photography", ["Commercial Photography", "Photo Editing (Photoshop/Lightroom)"]),
            ("Sculpture & 3D Design", ["3D Art Sculpture", "Material Design"])
        ],

        ("BJMC / BMM — Journalism & Mass Comm", "BJMC"): [
            ("Journalism & News Reporting", ["Journalism & News Reporting", "News Writing", "Fact Checking"]),
            ("Digital Journalism & SEO", ["Digital Content Creation", "Digital Marketing & SEO", "Social Media"]),
            ("Broadcast & TV Journalism", ["Video Editing", "Camera Operation", "TV News Reporting"]),
            ("Advertising & PR", ["Public Relations", "Brand Campaign Copywriting"]),
            ("Film Making & Video Editing", ["Scriptwriting", "Video Editing", "Cinematography"])
        ],

        ("BA LLB / BBA LLB / Law", "BALLB"): [
            ("Corporate Law", ["Legal Drafting & Contract Review", "Company Law Compliance", "M&A Due Diligence"]),
            ("Criminal Law", ["Criminal Procedure Code", "Legal Research", "Court Advocacy"]),
            ("Civil Law", ["Civil Procedure Code", "Legal Drafting & Contract Review"]),
            ("Constitutional Law", ["Constitutional Law", "Legal Research & Precedents"]),
            ("Intellectual Property Rights (IPR)", ["Patent Registration", "Trademark & Copyright Law"]),
            ("Cyber Law & Privacy", ["Cybersecurity & Networking", "Data Privacy Laws (DPDP)"]),
            ("Taxation Law", ["GST Compliance", "Income Tax Regulations"]),
            ("Labor & Employment Law", ["Labor Law Compliance", "Employee Relations"]),
            ("Commercial Arbitration", ["Legal Dispute Negotiation", "Arbitration Proceedings"])
        ],

        ("B.Des / BFD — Fashion & Product Design", "BDES"): [
            ("Fashion Design", ["Fashion Illustration", "Pattern Making & Garment Construction"]),
            ("Textile Design", ["Textile Weaving", "Fabric Pattern Design"]),
            ("Product & Industrial Design", ["CAD & SolidWorks", "3D Product Modeling"]),
            ("Graphic & Brand Design", ["Graphic Design", "UI/UX Design & Figma", "Typography"]),
            ("UX/UI Design", ["UI/UX Design & Figma", "User Research", "Wireframing & Prototyping"]),
            ("Interior Design", ["AutoCAD", "SketchUp", "Interior Space Planning"]),
            ("Animation & Game Design", ["2D/3D Animation", "Unity 3D", "Character Design"])
        ],

        ("Psychology (BA/BSc)", "PSYCHOLOGY"): [
            ("Clinical Psychology", ["Psychological Assessment", "Counseling & Psychotherapy", "Behavioral Diagnosis"]),
            ("Counseling Psychology", ["Psychological Counseling", "Active Listening & Empathy"]),
            ("Organizational / HR Psychology", ["Organizational Behavior", "HR Talent Assessment"]),
            ("Educational & Child Psychology", ["Child Development", "Learning Disability Assessment"]),
            ("Research Psychology", ["Statistical Analysis", "Psychometric Test Design"])
        ],

        ("Radiology & Medical Imaging", "RADIOLOGY"): [
            ("X-Ray & Radiography Tech", ["X-Ray Equipment Operation", "Patient Radiographic Positioning"]),
            ("CT Scan Technology", ["CT Scanner Operation", "Medical Cross-Sectional Imaging"]),
            ("MRI Technology", ["MRI Scanner Operation", "Magnetic Resonance Safety"]),
            ("Ultrasound Technology", ["Ultrasound Sonography", "Diagnostic Imaging"]),
            ("Nuclear Medicine & Radiotherapy", ["Radiation Safety", "Nuclear Imaging Equipment"])
        ],

        ("Agriculture — BSc Agriculture", "AGRI"): [
            ("Agronomy & Crop Production", ["Agritech & Crop Analytics", "Soil Fertility Management", "Crop Production"]),
            ("Horticulture Science", ["Fruit & Vegetable Cultivation", "Floriculture"]),
            ("Soil Science & Agricultural Chemistry", ["Soil NPK Testing", "Soil Health Management"]),
            ("Agricultural Economics & Agribusiness", ["Agribusiness Management", "Farm Supply Chain", "Agricultural Economics"]),
            ("Plant Pathology & Entomology", ["Pest Management", "Crop Disease Identification"]),
            ("Genetics & Plant Breeding", ["Crop Genetics", "Hybrid Seed Breeding"]),
            ("Precision Agriculture & Drones", ["Agritech & Crop Analytics", "GIS Mapping", "Drone Crop Monitoring"])
        ],

        ("Sericulture Science", "SERICULTURE"): [
            ("Mulberry Cultivation", ["Mulberry Agronomy", "Soil Management"]),
            ("Silkworm Rearing & Pathology", ["Silkworm Rearing", "Pest & Disease Control"]),
            ("Silk Reeling & Weaving", ["Silk Reeling Machinery", "Silk Fabric Weaving"]),
            ("Sericulture Economics & Extension", ["Sericulture Business", "Farmer Training & Extension"])
        ],

        ("Horticulture Science", "HORTICULTURE"): [
            ("Fruit Science (Pomology)", ["Fruit Crop Cultivation", "Orchard Management"]),
            ("Vegetable Science (Olericulture)", ["Vegetable Production", "Greenhouse Cultivation"]),
            ("Floriculture & Landscaping", ["Flower Cultivation", "Landscape Garden Design"]),
            ("Post-Harvest Technology", ["Fruit & Vegetable Storage", "Food Packaging Technology"]),
            ("Nursery Management", ["Plant Propagation", "Nursery Operations"])
        ],

        ("Veterinary Sciences — BVSc & AH", "VETERINARY"): [
            ("Veterinary Clinical Medicine", ["Animal Diagnosis", "Veterinary Treatment", "Clinical Care"]),
            ("Veterinary Surgery & Radiology", ["Animal Surgery", "Veterinary X-Ray Diagnostics"]),
            ("Animal Nutrition & Feed Tech", ["Livestock Nutrition", "Feed Formulation"]),
            ("Animal Genetics & Breeding", ["Livestock Breeding", "Animal Genetics"]),
            ("Veterinary Public Health", ["Zoonotic Disease Control", "Meat & Milk Quality Control"]),
            ("Poultry & Dairy Science", ["Poultry Farm Management", "Dairy Herd Operations"])
        ],

        ("BSc Nursing", "NURSING"): [
            ("General Clinical Nursing", ["Patient Care", "Vital Signs Monitoring", "Clinical Examination"]),
            ("Medical-Surgical Nursing", ["Post-Operative Care", "Clinical Patient Monitoring"]),
            ("Paediatric Nursing", ["Child Healthcare", "Pediatric Diagnostics"]),
            ("Obstetric & Gynecological Nursing", ["Maternal Care", "Neonatal Delivery Care"]),
            ("Critical Care & ICU Nursing", ["ICU Patient Monitoring", "Emergency Trauma Care"]),
            ("Operation Theatre Nursing", ["Surgical Assistance", "Sterilization Protocols"]),
            ("Community Health Nursing", ["Public Health Care", "Immunization & Hygiene"])
        ],

        ("Physiotherapy — BPT", "PHYSIOTHERAPY"): [
            ("Orthopaedic Physiotherapy", ["Musculoskeletal Rehabilitation", "Physical Therapy Exercises"]),
            ("Neurological Physiotherapy", ["Neuro Rehabilitation", "Stroke & Paralysis Mobility Therapy"]),
            ("Cardiopulmonary Physiotherapy", ["Respiratory Rehabilitation", "Cardiac Fitness Therapy"]),
            ("Sports Physiotherapy", ["Sports Injury Management", "Kinesiology & Taping"]),
            ("Pediatric & Geriatric Physiotherapy", ["Child Mobility Rehabilitation", "Elderly Mobility Care"]),
            ("Ergonomics & Pain Management", ["Postural Ergonomics", "Manual Pain Relief Therapy"])
        ]
    }

    # Step 1: Ensure Skills exist
    added_skills = 0
    for (deg_name, deg_code), streams in master_data.items():
        for stream_name, skills_list in streams:
            for sk_name in skills_list:
                sk_obj, created = Skill.objects.get_or_create(
                    name=sk_name,
                    defaults={'category': 'technical' if 'Python' in sk_name or 'Java' in sk_name else 'management' if 'Management' in sk_name or 'Finance' in sk_name else 'soft_skills'}
                )
                if created:
                    added_skills += 1

    print(f"Added {added_skills} new Skills to DB. Total Skills: {Skill.objects.count()}.")

    # Step 2: Seed Degrees & Streams
    added_degrees = 0
    added_streams = 0

    for (deg_name, deg_code), streams in master_data.items():
        degree_obj, created = Degree.objects.get_or_create(
            code=deg_code,
            defaults={
                'name': deg_name,
                'description': f"Official curriculum program for {deg_name}."
            }
        )
        if created:
            added_degrees += 1
        else:
            # Update name if needed
            degree_obj.name = deg_name
            degree_obj.save()

        for stream_name, skills_list in streams:
            stream_obj, s_created = Stream.objects.get_or_create(
                degree=degree_obj,
                name=stream_name,
                defaults={'code': f"{deg_code}_{stream_name[:10].upper().replace(' ', '_')}"}
            )
            if s_created:
                added_streams += 1

    print(f"Master Seed Complete! Degrees in DB: {Degree.objects.count()} | Streams in DB: {Stream.objects.count()}.")

if __name__ == '__main__':
    seed_degrees_streams_and_skills()
