import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import GovernmentExam

# Clear existing sample entries
GovernmentExam.objects.all().delete()

EXAMS_DATA = [
    # ----------------------------------------------------
    # GOVERNMENT & PSU COMPETITIVE EXAMS
    # ----------------------------------------------------
    {
        "exam_name": "UPSC Civil Services Examination (CSE - IAS/IPS/IFS)",
        "conducting_body": "Union Public Service Commission (UPSC)",
        "category": "govt",
        "domain": "Indian Administrative Service (IAS), Police (IPS), Foreign Service (IFS)",
        "eligibility": "Bachelor's Degree in any discipline from a recognized University. Age: 21 to 32 years (General).",
        "syllabus_summary": "Prelims GS-I (200M, 100 Qs) + CSAT GS-II (200M, 80 Qs, Qualifying 33%). Mains 9 Papers (Essay, GS I-IV, 2 Optional Papers) + Personality Interview Test.",
        "application_start_date": "February 04, 2027",
        "application_last_date": "February 24, 2027",
        "exam_date": "May 23, 2027 (Prelims) | September 17, 2027 (Mains)",
        "exam_timings": "Prelims Session 1: 09:30 AM – 11:30 AM | Session 2 (CSAT): 02:30 PM – 04:30 PM",
        "preparation_resources": "• Standard NCERT Textbooks (Classes 6-12)\n• Laxmikanth Indian Polity & Spectrum Modern India\n• The Hindu & Indian Express Daily Editorial Summaries\n• UPSC Previous 25 Years Solved Prelims Question Papers",
        "website_url": "https://upsc.gov.in",
        "exam_date_info": "Annual Exam (May/September)"
    },
    {
        "exam_name": "GATE 2027 (Graduate Aptitude Test in Engineering)",
        "conducting_body": "IIT Kharagpur / IISc Bangalore / GATE Committee",
        "category": "govt",
        "domain": "Computer Science, ECE, Mechanical, Electrical, Civil",
        "eligibility": "B.E / B.Tech / M.Sc / MCA completed or in pre-final/final year. No upper age limit.",
        "syllabus_summary": "Core CS/IT (33%), General Aptitude (15%), Engineering Mathematics (12%), Discrete Math, OS, DBMS, Algorithms, Computer Networks. 65 Questions (100 Marks).",
        "application_start_date": "August 30, 2026",
        "application_last_date": "October 12, 2026 (Extended)",
        "exam_date": "February 06, 07, 13 & 14, 2027",
        "exam_timings": "Forenoon Shift: 09:30 AM – 12:30 PM | Afternoon Shift: 02:30 PM – 05:30 PM",
        "preparation_resources": "• Official GATE Solved Question Papers (2015-2026)\n• NPTEL Video Lectures by IIT Faculty\n• Cormen (CLRS) Algorithms & Silberschatz OS Reference Textbooks\n• Free Virtual Calculator Practice Suite",
        "website_url": "https://gate2027.iitm.ac.in/",
        "exam_date_info": "Annual Exam (February)"
    },
    {
        "exam_name": "Karnataka PGCET / PG KCET 2026-2027",
        "conducting_body": "Karnataka Examinations Authority (KEA)",
        "category": "govt",
        "domain": "Post Graduate Admissions (M.Tech / M.E / MCA / MBA)",
        "eligibility": "B.E / B.Tech / B.Sc / BCA degree with minimum 50% aggregate (45% for SC/ST/OB-Karnataka).",
        "syllabus_summary": "100 MCQs (100 Marks, 150 Mins, No Negative Marking). Mathematics (25M), Computer Awareness (25M), Analytical Reasoning (25M), General English (25M).",
        "application_start_date": "May 25, 2026",
        "application_last_date": "June 20, 2026",
        "exam_date": "August 08 & 09, 2026",
        "exam_timings": "Single Shift: 02:30 PM – 05:00 PM (150 Minutes)",
        "preparation_resources": "• KEA PGCET Past 10 Years Solved Question Papers PDF\n• KEA Official Mock Examination Portal\n• Quantitative Aptitude & Reasoning Handbooks by R.S. Aggarwal",
        "website_url": "https://cetonline.karnataka.gov.in/kea",
        "exam_date_info": "Annual State Entrance (August)"
    },
    {
        "exam_name": "SSC CGL (Staff Selection Commission Combined Graduate Level)",
        "conducting_body": "Staff Selection Commission (SSC)",
        "category": "govt",
        "domain": "Assistant Section Officer (ASO), Income Tax Inspector, Central Excise, IT Officer",
        "eligibility": "Bachelor's Degree in any stream from a recognized university. Age: 18 to 32 years.",
        "syllabus_summary": "Tier I (100 Qs, 200M: General Intelligence 25Q, General Awareness 25Q, Quant 25Q, English 25Q). Tier II CBT (Math, Reasoning, English, General Awareness, Data Entry Speed Test).",
        "application_start_date": "June 24, 2026",
        "application_last_date": "July 24, 2026",
        "exam_date": "September 15 – October 05, 2026 (Tier I)",
        "exam_timings": "Shift 1: 09:00 AM – 10:00 AM | Shift 2: 12:30 PM – 01:30 PM | Shift 3: 04:00 PM – 05:00 PM",
        "preparation_resources": "• SSC CGL Previous Year Question Bank (50+ Shift Sets)\n• Lucent's General Knowledge & Kiran Reasoning Solved Papers\n• English Grammar & Vocab Rules Digest",
        "website_url": "https://ssc.gov.in",
        "exam_date_info": "Annual Exam (September)"
    },
    {
        "exam_name": "ISRO Scientist / Engineer 'SC' Cadre Exam",
        "conducting_body": "ISRO Centralized Recruitment Board (ICRB)",
        "category": "govt",
        "domain": "Space Research, Aerospace, CS & Electronics",
        "eligibility": "B.E / B.Tech in CS / ECE / Mechanical with minimum 65% aggregate or CGPA 6.84/10. Upper age limit: 28 years.",
        "syllabus_summary": "80 Technical Discipline MCQs (3 marks each, -1 negative mark). Covers Algorithms, Computer Architecture, Embedded Microcontrollers, Digital Logic, Signals & Systems.",
        "application_start_date": "September 15, 2026",
        "application_last_date": "October 20, 2026",
        "exam_date": "December 20, 2026",
        "exam_timings": "Single Shift: 10:00 AM – 12:00 PM (2 Hours)",
        "preparation_resources": "• ISRO Scientist Past 12 Years Solved Papers PDF\n• Advanced Digital Electronics & Computer Architecture Textbooks\n• ISRO Scientist Mock Practice Test Series",
        "website_url": "https://www.isro.gov.in/Careers.html",
        "exam_date_info": "Biannual Recruitment"
    },
    {
        "exam_name": "DRDO Scientist 'B' Recruitment Examination",
        "conducting_body": "Recruitment & Assessment Centre (RAC), DRDO",
        "category": "govt",
        "domain": "Defense Research & Development, Cyber Security, AI",
        "eligibility": "First Class Bachelor's Degree in Engineering (CS/IT/ECE) + Valid GATE Score. Max age: 28 years.",
        "syllabus_summary": "Descriptive Technical Paper I & II (300 Marks each). Advanced Cryptography, Embedded Systems, Radar Engineering, High-Performance Computing, AI/ML Principles.",
        "application_start_date": "October 01, 2026",
        "application_last_date": "November 10, 2026",
        "exam_date": "January 24, 2027",
        "exam_timings": "Paper I: 09:30 AM – 12:30 PM | Paper II: 02:00 PM – 05:00 PM",
        "preparation_resources": "• DRDO RAC Descriptive Model Question Papers\n• Applied Cryptography & Defense Technology Standard Notes\n• Technical Panel Interview Preparation Guide",
        "website_url": "https://rac.gov.in",
        "exam_date_info": "Annual Recruitment"
    },
    {
        "exam_name": "NIC Scientist 'B' & Technical Assistant A",
        "conducting_body": "National Informatics Centre (NIELIT / MeitY)",
        "category": "govt",
        "domain": "National e-Governance, Cloud & Cyber Infrastructure",
        "eligibility": "B.E / B.Tech / M.Sc / MCA in Computer Science / IT / ECE. No minimum percentage bar.",
        "syllabus_summary": "120 MCQs (78 Technical + 42 Generic Aptitude). Object-Oriented Programming, Web Technologies, Database Management, Network Security, Data Structures.",
        "application_start_date": "November 01, 2026",
        "application_last_date": "December 05, 2026",
        "exam_date": "March 14, 2027",
        "exam_timings": "Morning Shift: 10:00 AM – 01:00 PM (3 Hours)",
        "preparation_resources": "• NIELIT NIC Past Exam Solved Papers\n• Web & Database Fundamentals Question Bank\n• Online Mock Exam Portal",
        "website_url": "https://www.nielit.gov.in",
        "exam_date_info": "Annual Drive"
    },
    {
        "exam_name": "UPSC Engineering Services Examination (ESE / IES)",
        "conducting_body": "Union Public Service Commission (UPSC)",
        "category": "govt",
        "domain": "Indian Railway Service of Engineers, Central Power, Defense Quality Assurance",
        "eligibility": "B.E / B.Tech degree in Civil, Mechanical, Electrical, or ECE. Age: 21 to 30 years.",
        "syllabus_summary": "Stage I Prelims (500M: GS & Engineering Aptitude 200M + Discipline 300M). Stage II Mains (600M Conventional). Stage III Interview (200M).",
        "application_start_date": "September 16, 2026",
        "application_last_date": "October 06, 2026",
        "exam_date": "February 09, 2027",
        "exam_timings": "Paper I: 10:00 AM – 12:00 PM | Paper II: 02:00 PM – 05:00 PM",
        "preparation_resources": "• UPSC ESE Previous 20 Years Solved Objective & Conventional Papers\n• Made Easy / ACE Academy Postal Study Material\n• Standard Engineering Discipline Textbooks",
        "website_url": "https://upsc.gov.in",
        "exam_date_info": "Annual Exam (February)"
    },
    {
        "exam_name": "RRB Junior Engineer (JE) & IT Officers Drive",
        "conducting_body": "Railway Recruitment Control Board (RRCB)",
        "category": "govt",
        "domain": "Indian Railways Signal & Telecom, IT Systems, Maintenance",
        "eligibility": "Diploma / B.E / B.Tech in CS/IT/ECE/EE/ME or B.Sc CS. Age: 18 to 36 years.",
        "syllabus_summary": "CBT 1 (100M: Math 30M, Reasoning 25M, GA 15M, GS 30M). CBT 2 Technical (150M: Physics, Chemistry, Basics of Computers, Environment & Technical 100M).",
        "application_start_date": "July 30, 2026",
        "application_last_date": "August 29, 2026",
        "exam_date": "December 06 – 12, 2026",
        "exam_timings": "Shift 1: 09:00 AM – 10:30 AM | Shift 2: 12:30 PM – 02:00 PM | Shift 3: 04:00 PM – 05:30 PM",
        "preparation_resources": "• RRB JE Past Solved Technical Question Papers\n• General Science & Railway Awareness Notes\n• Online Timed CBT Practice Portal",
        "website_url": "https://indianrailways.gov.in",
        "exam_date_info": "Annual Recruitment"
    },
    {
        "exam_name": "SBI Specialist Cadre Officer (SCO) & IT Officer",
        "conducting_body": "State Bank of India (SBI Central Recruitment)",
        "category": "govt",
        "domain": "Banking Technology, Cyber Security, Cloud & FinTech",
        "eligibility": "B.E / B.Tech in CS/IT/ECE or MCA/M.Sc (IT). Age: 21 to 35 years.",
        "syllabus_summary": "Professional Knowledge Test (100 Marks), Reasoning (50 Marks), Quantitative Aptitude (50 Marks). Focus on Financial Cyber Security, Cloud Infrastructure, Core Banking API Systems.",
        "application_start_date": "September 10, 2026",
        "application_last_date": "October 05, 2026",
        "exam_date": "November 29, 2026",
        "exam_timings": "Online Test Shift 1: 09:00 AM – 11:15 AM",
        "preparation_resources": "• SBI SCO Professional Knowledge Question Bank\n• Banking IT Systems & Security Protocol Notes\n• Full Length Online Test Series",
        "website_url": "https://sbi.co.in/web/careers",
        "exam_date_info": "Biannual Drive"
    },

    # ----------------------------------------------------
    # PRIVATE & CORPORATE SECTOR CERTIFICATION EXAMS
    # ----------------------------------------------------
    {
        "exam_name": "TCS NQT (National Qualifier Test) & Digital/Prime Drive",
        "conducting_body": "Tata Consultancy Services (TCS iON)",
        "category": "private",
        "domain": "Software Engineering, Full Stack, Data Engineering, AI",
        "eligibility": "B.E / B.Tech / M.E / M.Tech / MCA / B.Sc / BCA freshers & candidates up to 2 years experience.",
        "syllabus_summary": "Part A Foundation (Numerical, Verbal, Reasoning). Part B Advanced (Advanced Quant + Hands-On Coding 2 Problems in C/C++/Java/Python).",
        "application_start_date": "Open Year-Round (Quarterly Drives)",
        "application_last_date": "March 10, 2027",
        "exam_date": "March 28, 2027",
        "exam_timings": "Morning Slot: 09:30 AM – 12:30 PM (TCS iON Digital Zones)",
        "preparation_resources": "• TCS NQT Previous Year Coding Questions & Solutions\n• PrepInsta TCS NQT Master Prep Material\n• LeetCode Easy-Medium Array & String Coding Practice",
        "website_url": "https://learning.tcsionhub.in/hub/national-qualifier-test",
        "exam_date_info": "Quarterly National Drive"
    },
    {
        "exam_name": "Wipro NLTH (Elite & Turbo National Hiring Drive)",
        "conducting_body": "Wipro Talent Transformation",
        "category": "private",
        "domain": "Full Stack Development, Cloud Engineering, QA Automation",
        "eligibility": "B.E / B.Tech / M.Tech (all branches) with minimum 60% in 10th, 12th & Graduation.",
        "syllabus_summary": "Aptitude Test (Logical, Quantitative, Verbal), Essay Writing (20 Mins), Hands-On Coding (2 Questions: Array Manipulation, String Parsing, Sorting).",
        "application_start_date": "August 15, 2026",
        "application_last_date": "September 25, 2026",
        "exam_date": "October 18, 2026",
        "exam_timings": "Online Proctored Assessment (Choose Flexible Preferred Slot)",
        "preparation_resources": "• Wipro Past Placement Question Papers\n• Array & String Coding Challenge Set\n• Business Essay Writing Tips Guide",
        "website_url": "https://careers.wipro.com/careers-home",
        "exam_date_info": "Annual Corporate Hiring"
    },
    {
        "exam_name": "AWS Certified Solutions Architect – Associate (SAA-C03)",
        "conducting_body": "Amazon Web Services (AWS Training & Certification)",
        "category": "private",
        "domain": "Cloud Computing, Infrastructure & Serverless",
        "eligibility": "Open to all students & professionals. Recommended 1+ year hands-on AWS experience.",
        "syllabus_summary": "65 Multiple Choice / Multiple Response Questions (130 Mins). Design Resilient Architectures (30%), High-Performing Architectures (26%), Secure Applications (24%), Cost-Optimized Architectures (20%).",
        "application_start_date": "Open Year-Round",
        "application_last_date": "Anytime (Flexible Scheduling)",
        "exam_date": "On-Demand (Online Proctored / Testing Center)",
        "exam_timings": "Flexible 24/7 Online Exam Slots Available",
        "preparation_resources": "• Official AWS SAA-C03 Exam Guide & Sample Questions\n• AWS Skill Builder Free Training Courses\n• Hands-On AWS Free Tier Architecture Practice\n• Stephane Maarek SAA-C03 Practice Exams",
        "website_url": "https://aws.amazon.com/certification/certified-solutions-architect-associate",
        "exam_date_info": "On-Demand 365 Days"
    },
    {
        "exam_name": "Google Associate Cloud Engineer (GCP Certification)",
        "conducting_body": "Google Cloud Training & Certification",
        "category": "private",
        "domain": "Google Cloud Infrastructure, Kubernetes & Big Data",
        "eligibility": "No strict prerequisites. Recommended 6+ months hands-on experience with GCP Console & gcloud CLI.",
        "syllabus_summary": "50 Multiple Choice Questions (120 Mins). Setting up Cloud Environment, Planning & Configuring Cloud Solution, Deploying Compute Engine / GKE / Cloud Run, Ensuring Successful Operation, Configuring Access & Security.",
        "application_start_date": "Open Year-Round",
        "application_last_date": "Anytime (Flexible Scheduling)",
        "exam_date": "On-Demand (Online Proctored / Kryterion Test Centers)",
        "exam_timings": "Choose preferred 2-hour slot (24/7 Availability)",
        "preparation_resources": "• Google Cloud Skills Boost Free Hands-On Labs\n• Official GCP Associate Cloud Engineer Study Guide\n• Google Cloud Interactive Architecture Diagrams",
        "website_url": "https://cloud.google.com/learn/certification/cloud-engineer",
        "exam_date_info": "On-Demand 365 Days"
    },
    {
        "exam_name": "Certified Kubernetes Administrator (CKA)",
        "conducting_body": "Linux Foundation & Cloud Native Computing Foundation (CNCF)",
        "category": "private",
        "domain": "Cloud Native, Container Orchestration, DevOps & Microservices",
        "eligibility": "Open to all DevOps engineers, SREs, and developers. Hands-on Linux CLI mastery recommended.",
        "syllabus_summary": "2-Hour Practical Performance-Based Exam (Hands-On Terminal Sandbox). Storage & Persistence (10%), Troubleshooting (30%), Workloads & Scheduling (15%), Cluster Architecture, Installation & Configuration (25%), Services & Networking (20%).",
        "application_start_date": "Open Year-Round",
        "application_last_date": "Anytime",
        "exam_date": "On-Demand (PSI Online Proctored)",
        "exam_timings": "24/7 Home/Office Online Slot",
        "preparation_resources": "• Killer.sh CKA Practice Simulator (Included with registration)\n• Mumshad Mannambeth CKA Udemy Course\n• Kubernetes.io Official Documentation & Cheatsheets",
        "website_url": "https://www.cncf.io/certification/cka/",
        "exam_date_info": "On-Demand 365 Days"
    },
    {
        "exam_name": "Cisco Certified Network Associate (CCNA 200-301)",
        "conducting_body": "Cisco Systems (Pearson VUE)",
        "category": "private",
        "domain": "Networking, Enterprise Routers, Switches & Cyber Ops",
        "eligibility": "Open to all engineering students & network technicians. No formal prerequisites.",
        "syllabus_summary": "100-120 Questions (120 Mins). Network Fundamentals (20%), Network Access (20%), IP Connectivity (25%), IP Services (10%), Security Fundamentals (15%), Automation & Programmability (10%).",
        "application_start_date": "Open Year-Round",
        "application_last_date": "Anytime",
        "exam_date": "On-Demand (Pearson VUE Center / Online)",
        "exam_timings": "Anytime via Pearson VUE Exam Scheduler",
        "preparation_resources": "• Cisco Packet Tracer Network Simulation Software\n• Official Cert Guide CCNA 200-301 by Wendell Odom\n• Jeremy's IT Lab Free CCNA Video Course & Anki Flashcards",
        "website_url": "https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html",
        "exam_date_info": "On-Demand 365 Days"
    },
    {
        "exam_name": "Microsoft Certified: Azure Solutions Architect Expert (AZ-305)",
        "conducting_body": "Microsoft Learn & Certification",
        "category": "private",
        "domain": "Enterprise Azure Infrastructure, Identity & Governance",
        "eligibility": "Prerequisite: Azure Administrator Associate (AZ-104) recommended.",
        "syllabus_summary": "40-60 Case Study & Technical Questions (120 Mins). Design Identity, Governance, and Monitoring Solutions (25-30%), Design Data Storage Solutions (25-30%), Design Business Continuity Solutions (10-15%), Design Infrastructure Solutions (25-30%).",
        "application_start_date": "Open Year-Round",
        "application_last_date": "Anytime",
        "exam_date": "On-Demand (Online Proctored via Pearson VUE)",
        "exam_timings": "Flexible 24/7 Scheduling",
        "preparation_resources": "• Microsoft Learn Free Learning Paths & Interactive Sandbox\n• Azure Architecture Center Reference Designs\n• AZ-305 Practice Assessment Exams",
        "website_url": "https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect",
        "exam_date_info": "On-Demand 365 Days"
    },
    {
        "exam_name": "Certified Information Systems Security Professional (CISSP)",
        "conducting_body": "ISC2 (International Information System Security Certification Consortium)",
        "category": "private",
        "domain": "Information Security, Chief Information Security Officer (CISO) Track",
        "eligibility": "5+ years of cumulative paid work experience in 2 or more of the 8 CISSP CBK domains.",
        "syllabus_summary": "Computerized Adaptive Testing (CAT) 100-150 Questions (3 Hours). Security & Risk Management, Asset Security, Security Architecture, Communication & Network Security, Identity & Access Management (IAM), Security Assessment & Testing.",
        "application_start_date": "Open Year-Round",
        "application_last_date": "Anytime",
        "exam_date": "On-Demand (Pearson VUE Testing Centers)",
        "exam_timings": "Flexible Slot Selection",
        "preparation_resources": "• Official ISC2 CISSP Study Guide (Sybex 9th Ed)\n• CISSP Practice Tests by Mike Chapple\n• Boson CISSP Exam Simulator",
        "website_url": "https://www.isc2.org/Certifications/CISSP",
        "exam_date_info": "On-Demand 365 Days"
    },
    {
        "exam_name": "HashiCorp Certified: Terraform Associate (003)",
        "conducting_body": "HashiCorp & PSI Online",
        "category": "private",
        "domain": "Infrastructure as Code (IaC), Multi-Cloud Automation",
        "eligibility": "Basic understanding of cloud concepts (AWS/Azure/GCP) and HCL syntax.",
        "syllabus_summary": "57 Multiple Choice & Multiple Select Questions (60 Mins). Understand IaC concepts, Terraform Basics, Terraform CLI, Terraform Modules, Terraform State, and HCL Syntax.",
        "application_start_date": "Open Year-Round",
        "application_last_date": "Anytime",
        "exam_date": "On-Demand (PSI Online Proctored)",
        "exam_timings": "Flexible 60-Minute Slots Available Daily",
        "preparation_resources": "• HashiCorp Official Developer Tutorials & Documentation\n• Terraform Associate Practice Exam Suite\n• Hands-On Local Terraform CLI Projects",
        "website_url": "https://developer.hashicorp.com/terraform/tutorials/certification-003",
        "exam_date_info": "On-Demand 365 Days"
    }
]

for item in EXAMS_DATA:
    GovernmentExam.objects.create(**item)

print(f"Successfully seeded {len(EXAMS_DATA)} real-world Government & Private Competitive Exams!")
