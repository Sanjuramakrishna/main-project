import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity
from profiles.models import Skill

def seed_govt_and_psu_jobs():
    # Helper to get skill instances safely
    skills_map = {s.name.lower(): s for s in Skill.objects.all()}

    govt_jobs_data = [
        {
            "title": "Scientist / Engineer 'SC' (Computer Science / IT)",
            "company": "ISRO - Indian Space Research Organisation (Govt PSU)",
            "location": "Bengaluru / Sriharikota / Thiruvananthapuram",
            "job_type": "Full-time",
            "salary_range": "₹10.5 - ₹15.6 LPA (Pay Level 10)",
            "experience_required": "0 - 2 Years (BE/BTech)",
            "description": "Lead space mission software engineering, telemetry algorithms, real-time satellite data extraction, and flight control systems for Chandrayaan and Gaganyaan national space missions.",
            "application_url": "https://www.isro.gov.in/Careers.html",
            "skills": ["python", "c++", "linux", "data structures"]
        },
        {
            "title": "Scientist 'B' (Cyber Security & AI Research)",
            "company": "DRDO - Defence Research and Development Organisation (Govt of India)",
            "location": "New Delhi / Bengaluru / Hyderabad",
            "job_type": "Full-time",
            "salary_range": "₹10.8 - ₹16.0 LPA (Pay Level 10)",
            "experience_required": "0 - 2 Years (GATE Score Qualified)",
            "description": "Research and deploy military-grade quantum encryption, defense AI systems, automated threat detection algorithms, and hardened defense communication systems.",
            "application_url": "https://rac.gov.in",
            "skills": ["cyber security", "c++", "linux", "python", "machine learning"]
        },
        {
            "title": "Scientist 'B' (Full Stack Cloud & e-Gov Systems)",
            "company": "NIC - National Informatics Centre (MeitY Govt of India)",
            "location": "New Delhi / State Capital Hubs",
            "job_type": "Full-time",
            "salary_range": "₹9.5 - ₹14.5 LPA",
            "experience_required": "0 - 3 Years",
            "description": "Build resilient national cloud infrastructure, digital identity verification gateways, and e-Governance portals processing over 1 Billion citizen requests daily.",
            "application_url": "https://www.nic.in/recruitment",
            "skills": ["java", "react", "sql", "cloud computing", "cyber security"]
        },
        {
            "title": "Graduate Engineers / Officers (Information Technology)",
            "company": "IOCL - Indian Oil Corporation Ltd (Maharatna PSU)",
            "location": "New Delhi / Mumbai / Kolkata",
            "job_type": "Full-time",
            "salary_range": "₹14.0 - ₹18.5 LPA",
            "experience_required": "0 - 1 Year (GATE Qualified)",
            "description": "Manage Maharatna PSU enterprise ERP infrastructure, cloud pipelines, refinery IoT analytics, and high-security corporate database clusters.",
            "application_url": "https://www.iocl.com/latest-job-opening",
            "skills": ["python", "sql", "linux", "cloud computing"]
        },
        {
            "title": "Executive Trainee (IT & Power Systems)",
            "company": "NTPC Limited (Maharatna PSU)",
            "location": "New Delhi / Hyderabad / Noida",
            "job_type": "Full-time",
            "salary_range": "₹13.5 - ₹17.8 LPA",
            "experience_required": "0 - 2 Years",
            "description": "Implement smart power grid monitoring software, industrial automation networks, and predictive SCADA telemetry analytics.",
            "application_url": "https://careers.ntpc.co.in",
            "skills": ["java", "sql", "data structures"]
        },
        {
            "title": "Probationary Engineer (Defense Software & AI)",
            "company": "BEL - Bharat Electronics Limited (Navratna PSU)",
            "location": "Bengaluru / Ghaziabad / Pune",
            "job_type": "Full-time",
            "salary_range": "₹11.0 - ₹15.0 LPA",
            "experience_required": "0 - 2 Years",
            "description": "Develop radar signal processing applications, naval defense communication suites, and computer vision threat identification models.",
            "application_url": "https://www.bel-india.in/Careers.aspx",
            "skills": ["c++", "python", "machine learning"]
        },
        {
            "title": "Specialist IT Officer (Manager - Cloud & Security)",
            "company": "SBI - State Bank of India (Govt Bank PSU)",
            "location": "Mumbai / Navi Mumbai",
            "job_type": "Full-time",
            "salary_range": "₹15.0 - ₹22.0 LPA",
            "experience_required": "1 - 4 Years",
            "description": "Architect core banking cloud security, anti-money laundering AI engines, and high-frequency UPI transaction microservices.",
            "application_url": "https://bank.sbi/careers",
            "skills": ["java", "cyber security", "sql", "cloud computing"]
        },
        {
            "title": "Scientific Officer 'C' (Computer Science & High Performance Computing)",
            "company": "BARC - Bhabha Atomic Research Centre (DAE Govt of India)",
            "location": "Trombay, Mumbai",
            "job_type": "Full-time",
            "salary_range": "₹11.5 - ₹16.5 LPA",
            "experience_required": "0 - 2 Years",
            "description": "Design high-performance supercomputing simulations, nuclear safety control systems, and computational data processing algorithms.",
            "application_url": "https://barc.gov.in/careers",
            "skills": ["c++", "python", "data structures"]
        }
    ]

    added_count = 0
    for data in govt_jobs_data:
        job_obj, created = JobOpportunity.objects.get_or_create(
            title=data["title"],
            company=data["company"],
            defaults={
                "location": data["location"],
                "job_type": data["job_type"],
                "salary_range": data["salary_range"],
                "experience_required": data["experience_required"],
                "description": data["description"],
                "application_url": data["application_url"],
                "is_active": True
            }
        )
        
        # Attach matching skills
        for sk_name in data["skills"]:
            if sk_name in skills_map:
                job_obj.required_skills.add(skills_map[sk_name])

        if created:
            added_count += 1
            print(f"Added Govt/PSU Job: {job_obj.title} at {job_obj.company}")

    print(f"Successfully seeded {added_count} Government & PSU Job Opportunities!")

if __name__ == "__main__":
    seed_govt_and_psu_jobs()
