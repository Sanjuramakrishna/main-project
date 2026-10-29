import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity
from profiles.models import Skill, Degree

def seed_unstop_github_naukri_jobs():
    print("[INFO] Seeding Jobs from Unstop, GitHub, and Naukri across all degree domains...")

    # Define domain jobs dataset for Unstop, GitHub, and Naukri
    jobs_dataset = [
        # =========================================================================
        # 1. TECH DOMAIN (B.Tech, M.Tech, BE, ME, BCA, MCA, B.Sc CS, ITI / Diploma Tech)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Software Development Engineer (SDE-1)',
            'company': 'Infosys / Cognizant (via Unstop)',
            'domain': 'tech',
            'location': 'Bengaluru / Remote',
            'job_type': 'Full-time',
            'salary_range': '₹8 - ₹16 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Apply via Unstop for SDE-1 software development positions. Develop high-scale web APIs, data structures, and cloud microservices. Great growth opportunity for Engineering, BCA, and MCA freshers.',
            'application_url': 'https://unstop.com/jobs/software-development-engineer-sde-1-100234',
            'skills': ['Python', 'Java', 'Data Structures', 'Web Development', 'SQL']
        },
        {
            'title': 'GitHub Careers: Open Source Cloud & DevOps Engineer',
            'company': 'GitHub Engineering Network',
            'domain': 'tech',
            'location': 'Remote (India)',
            'job_type': 'Remote',
            'salary_range': '₹14 - ₹28 LPA',
            'experience_required': '1 - 3 Years',
            'description': 'Direct hiring via GitHub Careers for Open Source Cloud & DevOps Engineers. Build Kubernetes infrastructure, automated CI/CD pipelines, and cloud security frameworks.',
            'application_url': 'https://github.com/careers/positions/cloud-devops-engineer-4091',
            'skills': ['Docker', 'Kubernetes', 'Cloud Computing', 'Linux', 'Python']
        },
        {
            'title': 'Naukri Hiring: Full Stack Web & Systems Developer',
            'company': 'TCS / Wipro Digital (via Naukri.com)',
            'domain': 'tech',
            'location': 'Hyderabad / Pune',
            'job_type': 'Hybrid',
            'salary_range': '₹7 - ₹15 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'Featured on Naukri.com: Hiring Full Stack Developers proficient in React, Node.js, Python, and PostgreSQL. Design responsive UI components and backend database schemas.',
            'application_url': 'https://www.naukri.com/job-listings-full-stack-web-developer-tcs-bengaluru-509182',
            'skills': ['React', 'Node.js', 'Web Development', 'SQL', 'JavaScript']
        },

        # =========================================================================
        # 2. MEDICAL DOMAIN (MBBS, BDS, B.Pharm, D.Pharm, Nursing, Physiotherapy, Psychology, Radiology, Veterinary)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Clinical Research Associate & Medical Data Specialist',
            'company': 'Apollo Healthcare / Biocon (via Unstop)',
            'domain': 'medical',
            'location': 'Mumbai / Bengaluru',
            'job_type': 'Full-time',
            'salary_range': '₹7 - ₹14 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Unstop National Hiring Drive: Clinical Research Associate role for MBBS, BDS, B.Pharm, and Nursing graduates. Conduct clinical trials, analyze patient medical data, and verify FDA regulatory documentation.',
            'application_url': 'https://unstop.com/jobs/clinical-research-associate-medical-data-analyst-100567',
            'skills': ['Clinical Research', 'Pharmacology', 'Medical Terminology', 'Healthcare Data']
        },
        {
            'title': 'GitHub Careers: Bio-Informatics & Healthcare Data Software Specialist',
            'company': "Dr. Reddy's Labs / Genomics Institute (via GitHub Careers)",
            'domain': 'medical',
            'location': 'Remote / Hyderabad',
            'job_type': 'Remote',
            'salary_range': '₹10 - ₹20 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'GitHub Careers Open Position: Bio-Informatics Specialist analyzing genomic sequencing, biomedical data algorithms, and clinical software pipelines for pharmacy and medical researchers.',
            'application_url': 'https://github.com/careers/positions/bioinformatics-software-specialist-6012',
            'skills': ['Bioinformatics', 'Genomics', 'Python', 'Data Analysis']
        },
        {
            'title': 'Naukri Hiring: Hospital Clinical Specialist & Resident Medical Officer',
            'company': 'Fortis Hospitals / Max Healthcare (via Naukri.com)',
            'domain': 'medical',
            'location': 'New Delhi / Chennai',
            'job_type': 'Full-time',
            'salary_range': '₹9 - ₹18 LPA',
            'experience_required': '1 - 4 Years',
            'description': 'Featured on Naukri.com: Resident Medical Officers and Clinical Specialists for leading multi-specialty hospitals. Patient diagnosis, emergency care, clinical administration, and diagnostic imaging.',
            'application_url': 'https://www.naukri.com/job-listings-resident-medical-officer-fortis-delhi-702319',
            'skills': ['Patient Care', 'Clinical Diagnosis', 'Emergency Care', 'Pharmacology']
        },

        # =========================================================================
        # 3. COMMERCE DOMAIN (B.Com, M.Com, BBA, MBA, BMS, CA)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Corporate Financial Analyst & Risk Associate',
            'company': 'Deloitte / KPMG (via Unstop)',
            'domain': 'commerce',
            'location': 'Mumbai / Gurugram',
            'job_type': 'Full-time',
            'salary_range': '₹8 - ₹15 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Unstop Business Hiring Challenge: Corporate Financial Analyst role for B.Com, M.Com, BBA, MBA, and CA candidates. Financial modeling, GST auditing, equity research, and corporate tax planning.',
            'application_url': 'https://unstop.com/jobs/corporate-financial-analyst-deloitte-100891',
            'skills': ['Financial Analysis', 'Accounting', 'Taxation', 'Tally Prime', 'Excel']
        },
        {
            'title': 'GitHub Careers: FinTech Data Analyst & Quantitative Auditor',
            'company': 'Razorpay / Paytm Financial (via GitHub Careers)',
            'domain': 'commerce',
            'location': 'Remote / Bengaluru',
            'job_type': 'Remote',
            'salary_range': '₹12 - ₹22 LPA',
            'experience_required': '1 - 3 Years',
            'description': 'GitHub Careers FinTech Track: Quantitative Data Analyst analyzing digital transaction metrics, fraud detection algorithms, banking APIs, and financial reporting dashboards.',
            'application_url': 'https://github.com/careers/positions/fintech-data-analyst-8012',
            'skills': ['Financial Modeling', 'SQL', 'Data Analysis', 'Python', 'Excel']
        },
        {
            'title': 'Naukri Hiring: Senior Accounts Manager & Investment Analyst',
            'company': 'HDFC Bank / ICICI Securities (via Naukri.com)',
            'domain': 'commerce',
            'location': 'Mumbai / Pune',
            'job_type': 'Hybrid',
            'salary_range': '₹7 - ₹16 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'Naukri.com Verified Hiring: Investment & Accounts Analyst managing corporate wealth portfolios, banking reconciliation, balance sheet audit, and SAP financial management.',
            'application_url': 'https://www.naukri.com/job-listings-investment-analyst-hdfc-mumbai-901234',
            'skills': ['Banking', 'Investment Management', 'Accounting', 'Portfolio Management']
        },

        # =========================================================================
        # 4. LEGAL DOMAIN (Law LLB, BA LLB, BBA LLB, LLM)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Corporate Legal Associate & Compliance Specialist',
            'company': 'Shardul Amarchand Mangaldas (via Unstop)',
            'domain': 'legal',
            'location': 'New Delhi / Mumbai',
            'job_type': 'Full-time',
            'salary_range': '₹9 - ₹18 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Unstop Legal Excellence Drive: Corporate Counsel role for LLB and LLM graduates. Draft commercial contracts, handle intellectual property compliance, corporate governance, and arbitration.',
            'application_url': 'https://unstop.com/jobs/corporate-legal-associate-101123',
            'skills': ['Corporate Law', 'Legal Drafting', 'Contract Law', 'Intellectual Property']
        },
        {
            'title': 'GitHub Careers: Tech Policy & Legal Counsel Advisor',
            'company': 'LegalTech Innovation Labs (via GitHub Careers)',
            'domain': 'legal',
            'location': 'Remote (India)',
            'job_type': 'Remote',
            'salary_range': '₹11 - ₹22 LPA',
            'experience_required': '1 - 3 Years',
            'description': 'GitHub Careers Legal Tech Position: Legal Policy Advisor evaluating digital privacy laws, GDPR data governance, open source licensing contracts, and software copyright law.',
            'application_url': 'https://github.com/careers/positions/tech-policy-legal-counsel-9045',
            'skills': ['Cyber Law', 'Data Privacy', 'Legal Drafting', 'Compliance']
        },
        {
            'title': 'Naukri Hiring: High Court Legal Advocate & Regulatory Counsel',
            'company': 'AZB & Partners / Trilegal (via Naukri.com)',
            'domain': 'legal',
            'location': 'Bengaluru / Delhi NCR',
            'job_type': 'Full-time',
            'salary_range': '₹8 - ₹16 LPA',
            'experience_required': '1 - 4 Years',
            'description': 'Featured on Naukri.com: Litigation Advocate & Regulatory Counsel for leading law firms. Handle civil litigation, court case research, contract review, and Bar Council advocacy.',
            'application_url': 'https://www.naukri.com/job-listings-corporate-legal-counsel-azb-delhi-802341',
            'skills': ['Litigation', 'Legal Research', 'Constitutional Law', 'Contract Law']
        },

        # =========================================================================
        # 5. AGRICULTURE DOMAIN (BSc Agriculture, Sericulture, Horticulture)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Agribusiness Operations Manager & Agronomist',
            'company': 'UPL Ltd / Coromandel International (via Unstop)',
            'domain': 'agriculture',
            'location': 'Hyderabad / Pune',
            'job_type': 'Full-time',
            'salary_range': '₹6 - ₹13 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Unstop Agri-Innovators Hiring: Agronomist & Agribusiness Operations Manager. Soil fertility analysis, crop yield optimization, organic farming protocols, and seed research.',
            'application_url': 'https://unstop.com/jobs/agribusiness-operations-manager-101456',
            'skills': ['Agronomy', 'Soil Science', 'Agribusiness', 'Crop Protection']
        },
        {
            'title': 'GitHub Careers: AgriTech Smart Data & Precision Farming Engineer',
            'company': 'DeHaat / CropIn AgriTech (via GitHub Careers)',
            'domain': 'agriculture',
            'location': 'Remote / Bengaluru',
            'job_type': 'Remote',
            'salary_range': '₹9 - ₹18 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'GitHub Careers AgriTech Division: Smart Farming Data Specialist. Build GIS crop mapping algorithms, weather pattern data pipelines, and automated irrigation software.',
            'application_url': 'https://github.com/careers/positions/agritech-precision-farming-7034',
            'skills': ['AgriTech', 'Data Analysis', 'Remote Sensing', 'Soil Science']
        },
        {
            'title': 'Naukri Hiring: Soil Science Researcher & Crop Quality Inspector',
            'company': 'Bayer CropScience / NITI Aayog Agri (via Naukri.com)',
            'domain': 'agriculture',
            'location': 'Nagpur / Anand / Chandigarh',
            'job_type': 'Full-time',
            'salary_range': '₹6 - ₹12 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'Featured on Naukri.com: Quality Inspector & Soil Science Specialist. Hybrid seed quality testing, sericulture silkworm cultivation techniques, and horticulture crop advisory.',
            'application_url': 'https://www.naukri.com/job-listings-soil-science-researcher-bayer-pune-709123',
            'skills': ['Horticulture', 'Sericulture', 'Soil Science', 'Plant Breeding']
        },

        # =========================================================================
        # 6. ARCHITECTURE DOMAIN (B.Arch, M.Arch)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Architectural Consultant & BIM Specialist',
            'company': 'Hafeez Contractor / L&T Construction (via Unstop)',
            'domain': 'architecture',
            'location': 'Mumbai / Bengaluru',
            'job_type': 'Full-time',
            'salary_range': '₹7 - ₹15 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Unstop Design Challenge Hiring: Architectural Consultant for B.Arch and M.Arch graduates. Building Information Modeling (BIM), AutoCAD drafting, Revit 3D modeling, and structural blueprint review.',
            'application_url': 'https://unstop.com/jobs/architectural-consultant-bim-specialist-101789',
            'skills': ['AutoCAD', 'Revit BIM', '3D Modeling', 'Urban Planning']
        },
        {
            'title': 'GitHub Careers: 3D Parametric Architect & Computational Designer',
            'company': 'Spatial3D Design Studio (via GitHub Careers)',
            'domain': 'architecture',
            'location': 'Remote / New Delhi',
            'job_type': 'Remote',
            'salary_range': '₹10 - ₹20 LPA',
            'experience_required': '1 - 3 Years',
            'description': 'GitHub Careers Computational Architecture Track: Parametric Design Engineer using Rhino, Grasshopper, Python scripting, and generative structural building design.',
            'application_url': 'https://github.com/careers/positions/3d-computational-architect-5023',
            'skills': ['Parametric Design', 'Rhino 3D', 'Grasshopper', 'Python']
        },
        {
            'title': 'Naukri Hiring: Urban Planning Architect & Interior Designer',
            'company': 'Shapoorji Pallonji / DLF Urban (via Naukri.com)',
            'domain': 'architecture',
            'location': 'Gurugram / Pune',
            'job_type': 'Hybrid',
            'salary_range': '₹8 - ₹16 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'Naukri.com Prime Job: Urban Planner & Commercial Interior Architect. Green building certifications (LEED), master planning, 3ds Max rendering, and site construction supervision.',
            'application_url': 'https://www.naukri.com/job-listings-urban-planning-architect-dlf-gurugram-604512',
            'skills': ['Urban Planning', 'Interior Design', 'AutoCAD', 'Structural Engineering']
        },

        # =========================================================================
        # 7. ARTS DOMAIN (BA, MA, BFA, BJMC / BMM Journalism, B.Des Fashion & Product)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Digital Media Specialist & Content Strategist',
            'company': 'Times Internet / NDTV Media (via Unstop)',
            'domain': 'arts',
            'location': 'New Delhi / Mumbai',
            'job_type': 'Full-time',
            'salary_range': '₹6 - ₹12 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Unstop Creative Talent Hiring: Media Specialist & Journalist. Digital news publishing, brand storytelling, video editing, public relations, and social media analytics.',
            'application_url': 'https://unstop.com/jobs/digital-media-specialist-content-strategist-102012',
            'skills': ['Journalism', 'Content Writing', 'Digital Media', 'Public Relations']
        },
        {
            'title': 'GitHub Careers: Senior UI/UX Designer & Product Illustrator',
            'company': 'Canva / GitHub Design Guild (via GitHub Careers)',
            'domain': 'arts',
            'location': 'Remote (India)',
            'job_type': 'Remote',
            'salary_range': '₹11 - ₹22 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'GitHub Careers Design Guild: Product Designer & UI/UX Specialist for B.Des and BFA graduates. User research, wireframing, Figma design systems, motion graphics, and accessibility.',
            'application_url': 'https://github.com/careers/positions/ui-ux-product-designer-3089',
            'skills': ['UI/UX Design', 'Figma', 'Graphic Design', 'Visual Arts']
        },
        {
            'title': 'Naukri Hiring: Corporate Communications Manager & Graphic Designer',
            'company': 'Ogilvy & Mather / Dentsu Aegis (via Naukri.com)',
            'domain': 'arts',
            'location': 'Mumbai / Bengaluru',
            'job_type': 'Hybrid',
            'salary_range': '₹7 - ₹14 LPA',
            'experience_required': '1 - 3 Years',
            'description': 'Naukri.com Verified Listing: Graphic Designer & Creative Director. Brand campaign design, Adobe Creative Cloud (Photoshop, Illustrator, InDesign), copywriting, and fashion portfolio design.',
            'application_url': 'https://www.naukri.com/job-listings-graphic-designer-ogilvy-mumbai-401298',
            'skills': ['Graphic Design', 'Creative Writing', 'Adobe Photoshop', 'Branding']
        },

        # =========================================================================
        # 8. SCIENCE DOMAIN (BSc, MSc Physics, Chemistry, Maths, Biotech)
        # =========================================================================
        {
            'title': 'Unstop Hiring: Research Scientist & Bio-Tech Specialist',
            'company': 'CSIR Labs / Syngene International (via Unstop)',
            'domain': 'science',
            'location': 'Bengaluru / Hyderabad',
            'job_type': 'Full-time',
            'salary_range': '₹7 - ₹15 LPA',
            'experience_required': '0 - 2 Years',
            'description': 'Unstop Young Scientists Drive: Research Scientist for BSc and MSc graduates in Physics, Chemistry, Mathematics, and Biotech. Laboratory analysis, molecular biology, statistical modeling, and R&D.',
            'application_url': 'https://unstop.com/jobs/research-scientist-biotech-specialist-102345',
            'skills': ['Research', 'Biotechnology', 'Chemistry', 'Data Analysis']
        },
        {
            'title': 'GitHub Careers: Quantum Computing Researcher & Mathematical Modeler',
            'company': 'TIFR / Quantum Research Lab (via GitHub Careers)',
            'domain': 'science',
            'location': 'Remote / Pune',
            'job_type': 'Remote',
            'salary_range': '₹12 - ₹24 LPA',
            'experience_required': '1 - 3 Years',
            'description': 'GitHub Careers Science Track: Computational Physicist & Mathematical Modeler. Quantum simulation algorithms, numerical analysis using Python/NumPy, and cryptographic physics modeling.',
            'application_url': 'https://github.com/careers/positions/quantum-computing-researcher-2090',
            'skills': ['Mathematics', 'Physics', 'Python', 'Numerical Analysis']
        },
        {
            'title': 'Naukri Hiring: Analytical Chemist & Laboratory Operations Manager',
            'company': 'Sun Pharma / Reliance Life Sciences (via Naukri.com)',
            'domain': 'science',
            'location': 'Vadodara / Mumbai',
            'job_type': 'Full-time',
            'salary_range': '₹6 - ₹13 LPA',
            'experience_required': '0 - 3 Years',
            'description': 'Naukri.com Featured Listing: Analytical Chemist & Quality Control Specialist. HPLC spectroscopy, chemical synthesis, lab safety protocols, and statistical data validation.',
            'application_url': 'https://www.naukri.com/job-listings-analytical-chemist-sunpharma-mumbai-308912',
            'skills': ['Chemistry', 'Quality Control', 'Laboratory Techniques', 'Microbiology']
        },
    ]

    created_count = 0
    updated_count = 0

    for job_data in jobs_dataset:
        skill_names = job_data.pop('skills', [])
        
        job_obj, created = JobOpportunity.objects.update_or_create(
            title=job_data['title'],
            company=job_data['company'],
            defaults={
                'domain': job_data['domain'],
                'location': job_data['location'],
                'job_type': job_data['job_type'],
                'salary_range': job_data['salary_range'],
                'experience_required': job_data['experience_required'],
                'description': job_data['description'],
                'application_url': job_data['application_url'],
                'is_active': True
            }
        )

        # Attach skills to JobOpportunity
        skill_objs = []
        for sname in skill_names:
            skill_inst, _ = Skill.objects.get_or_create(
                name=sname,
                defaults={'category': job_data['domain'].title(), 'description': f'{sname} skill definition.'}
            )
            skill_objs.append(skill_inst)
        
        job_obj.required_skills.set(skill_objs)

        if created:
            created_count += 1
        else:
            updated_count += 1

    print("[SUCCESS] Successfully seeded Unstop, GitHub, and Naukri jobs!")
    print(f"[SUMMARY] Created: {created_count} new jobs | Updated: {updated_count} existing jobs.")
    print(f"[STATS] Total Active Jobs in Database: {JobOpportunity.objects.filter(is_active=True).count()}")

if __name__ == '__main__':
    seed_unstop_github_naukri_jobs()
