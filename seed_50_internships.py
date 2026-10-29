import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import Internship
from profiles.models import Skill

def seed_50_internships():
    print("Seeding Internship Opportunities for ALL 15 Degrees...")
    
    # Clear existing internships
    Internship.objects.all().delete()

    internships_master = [
        # Tech & Engineering (BTECH, BCA, MCA, BSC, MTECH, DIPLOMA)
        ("Full Stack Web Development Intern", "HackerEarth", "3 Months", "₹25,000 / month", "Bengaluru / Remote", "BE/BTech/BCA/MCA/Diploma", "Build competitive coding platform UI components in React & Django.", "https://www.hackerearth.com/companies/careers", ["react", "python", "javascript"]),
        ("Data Science & Machine Learning Intern", "Fractal Analytics", "6 Months", "₹30,000 / month", "Mumbai / Remote", "BE/BTech/BSC/MSC/AGRI", "Retail consumer behavior predictive modeling using Python & XGBoost.", "https://fractal.ai/careers", ["python", "pandas & numpy", "machine learning"]),
        ("Cybersecurity & Malware Analysis Intern", "Quick Heal Technologies", "3 Months", "₹20,000 / month", "Pune", "BE/BTech/BCA/MCA/LLB/Diploma", "Malware reverse engineering, threat signature analysis.", "https://www.quickheal.co.in/careers", ["cybersecurity & networking", "c++"]),
        ("Cloud DevOps & Containerization Intern", "Nutanix India", "6 Months", "₹35,000 / month", "Bengaluru", "BE/BTech/MCA/MTech", "Automate CI/CD pipelines, Docker container orchestration.", "https://www.nutanix.com/careers", ["aws & cloud computing", "docker & kubernetes"]),
        ("AI Research & LLMs Intern", "Google Research India", "6 Months", "₹45,000 / month", "Bengaluru", "BE/BTech/MCA/MTech/BSC", "Research multi-modal AI models, tokenization pipelines, NLP benchmarks.", "https://careers.google.com", ["python", "deep learning & pytorch", "machine learning"]),
        ("Front-End Web Design (React) Intern", "Swiggy", "3 Months", "₹28,000 / month", "Bengaluru / Remote", "BE/BTech/BCA/BBA", "Build high-throughput consumer web checkout components.", "https://careers.swiggy.com", ["react", "javascript", "html & css"]),
        ("Backend Systems (Python/Django) Intern", "Postman India", "6 Months", "₹35,000 / month", "Bengaluru / Remote", "BE/BTech/MCA/BCA", "Optimize API testing engine microservices and webhook processors.", "https://www.postman.com/careers", ["python", "sql & databases", "git & github"]),
        ("Mobile App Development (Flutter) Intern", "Dream11", "3 Months", "₹30,000 / month", "Mumbai / Remote", "BE/BTech/BCA/Diploma", "Develop real-time fantasy gaming mobile screens and state management.", "https://www.dream11.com/careers", ["react", "javascript"]),
        ("Embedded Hardware & Firmware Intern", "Texas Instruments", "6 Months", "₹32,000 / month", "Bengaluru", "BE/BTech/Diploma/MTech", "MSP430 microcontroller circuit design and C driver coding.", "https://www.ti.com/careers", ["embedded c / microcontrollers"]),
        ("VLSI & Chip Verification Intern", "Intel India", "6 Months", "₹38,000 / month", "Bengaluru", "BE/BTech/MTech", "SystemVerilog testbench simulation for Xeon server processors.", "https://www.intel.in/content/www/in/en/jobs/careers.html", ["c++", "embedded c / microcontrollers"]),

        # Medical & Health (MBBS, BSC)
        ("Clinical Research & Diagnostics Intern", "Pfizer India", "6 Months", "₹22,000 / month", "Mumbai", "MBBS / BSc Medical / Biotech", "Clinical trial protocol execution, patient diagnostic data logging, FDA audit prep.", "https://www.pfizer.co.in/careers", ["clinical medicine & diagnostics", "technical writing & documentation"]),
        ("Tele-Health Operations & Medical Intern", "Apollo Hospitals", "3 Months", "₹20,000 / month", "Bengaluru / Remote", "MBBS / BSc Nursing", "Remote patient consultation triage, digital medical records auditing.", "https://www.apollohospitals.com/careers", ["clinical medicine & diagnostics", "communication & public speaking"]),
        ("Biotech & Computational Assay Intern", "Biocon", "6 Months", "₹18,000 / month", "Bengaluru", "MBBS / BSC / MSC Biotech", "Monoclonal antibody assay analytics and protein data logging.", "https://www.biocon.com/careers", ["pandas & numpy"]),

        # Law & Governance (LLB, BA, BCOM)
        ("Corporate Law & M&A Due Diligence Intern", "Cyril Amarchand Mangaldas", "2 Months", "₹22,000 / month", "Mumbai / New Delhi", "LLB / BCom / BA Law", "Corporate M&A contract due diligence, regulatory filing review, legal research.", "https://www.cyrilshroff.com/careers", ["legal drafting & contract review", "communication & public speaking"]),
        ("Legal Tech & Data Privacy Compliance Intern", "Trilegal India", "3 Months", "₹20,000 / month", "Bengaluru / Remote", "LLB / BE/BTech / BCom", "DPDP Act privacy policy compliance audit, contract automation templates.", "https://trilegal.com/careers", ["legal drafting & contract review", "cybersecurity & networking"]),
        ("Intellectual Property (IP) Patent Research Intern", "Khaitan & Co", "3 Months", "₹18,000 / month", "New Delhi", "LLB / BTech / BSc", "Patent prior art search, trademark registry documentation.", "https://www.khaitanco.com/careers", ["legal drafting & contract review", "technical writing & documentation"]),

        # Agriculture & Agritech (AGRI, BSC, BTECH, DIPLOMA)
        ("Agritech Satellite Crop Analytics Intern", "DeHaat (Green Agrevolution)", "4 Months", "₹20,000 / month", "Gurugram / Remote", "BSc Agriculture / BTech / Diploma", "Crop satellite imagery classification for yield forecasting and soil analytics.", "https://agribegri.com/careers", ["agritech & crop analytics", "pandas & numpy"]),
        ("Precision Farming & Agri Supply Chain Intern", "Ninjacart", "3 Months", "₹18,000 / month", "Bengaluru / Pune", "BSc Agriculture / BBA / MBA", "Farm produce quality inspection, cold chain dispatch tracking.", "https://ninjacart.in/careers", ["supply chain & operations", "agritech & crop analytics"]),
        ("Organic Farm Advisory & Soil Intern", "Coromandel International", "6 Months", "₹16,000 / month", "Hyderabad / Field", "BSc Agriculture / Diploma Agri", "Soil sample NPK testing, organic fertilizer advisory to local farm clusters.", "https://www.coromandel.biz/careers", ["agritech & crop analytics"]),

        # Design, Arts & Media (BDES, BA, BSC)
        ("UI/UX Product Design Intern", "Unacademy", "4 Months", "₹22,000 / month", "Bengaluru / Remote", "BDES / BA / BSc / BTech", "Student mobile app user journey research and Figma prototypes.", "https://unacademy.com/careers", ["ui/ux design & figma"]),
        ("Graphic Design & Visual Brand Intern", "Canva India", "3 Months", "₹20,000 / month", "Remote / Mumbai", "BDES / BA / Open to All", "Template asset design, typography, and promotional vectors.", "https://www.canva.com/careers", ["ui/ux design & figma", "3d animation & visual art"]),
        ("Content & Digital Communications Intern", "NDTV", "3 Months", "₹15,000 / month", "New Delhi", "BA / BDES / Mass Comm", "Draft daily news bulletins, digital video scripts, social copy.", "https://www.ndtv.com/careers", ["communication & public speaking"]),

        # Diploma & Vocational (DIPLOMA, BTECH)
        ("Polytechnic Mechanical CAD Intern", "Hero MotoCorp", "6 Months", "₹18,000 / month", "Gurugram", "Diploma Mechanical / Auto", "Two-wheeler engine chassis CAD design and assembly drawings.", "https://www.heromotocorp.com/en-in/careers", ["cad & solidworks", "industrial maintenance & machining"]),
        ("Civil Infrastructure Site Trainee Intern", "Shapoorji Pallonji", "6 Months", "₹16,000 / month", "Mumbai / Chennai", "Diploma Civil / BTech Civil", "High-rise building ETABS structural modeling and rebar detailing.", "https://www.shapoorjipallonji.com/careers", ["structural analysis & etabs", "cad & solidworks"]),
        ("Industrial Automation & SCADA Intern", "ABB India", "6 Months", "₹20,000 / month", "Bengaluru", "Diploma Electrical / EEE", "Substation automation SCADA telemetry configuration.", "https://global.abb/group/en/careers", ["plc & scada automation"]),

        # Business, Commerce & Finance (BCOM, MCOM, BBA, MBA)
        ("Financial Modeling & Banking Analyst Intern", "HDFC Bank", "3 Months", "₹18,000 / month", "Mumbai", "BCom / MCom / BBA / MBA", "Branch credit assessment, retail loan portfolio evaluation.", "https://www.hdfcbank.com/careers", ["financial modeling & excel", "accounting & taxation"]),
        ("Corporate Accounting & Tax Intern", "Ernst & Young (EY)", "6 Months", "₹20,000 / month", "Gurugram / Remote", "BCom / MCom / MBA", "Corporate tax compliance working papers and statutory filing.", "https://www.ey.com/en_in/careers", ["accounting & taxation", "financial modeling & excel"]),
        ("Equity Research & Investment Intern", "Zerodha Broking", "3 Months", "₹25,000 / month", "Bengaluru / Remote", "BCom / MCom / BBA / MBA", "Financial statement analysis of listed Indian equities.", "https://careers.zerodha.com", ["financial modeling & excel", "corporate finance & valuation"]),
        ("Product Management Associate Intern", "Razorpay", "4 Months", "₹32,000 / month", "Bengaluru", "MBA / BBA / BTech", "Merchant payment onboarding experience optimization and specs.", "https://razorpay.com/jobs", ["business analysis", "agile & project management"]),
        ("Digital Marketing & SEO Growth Intern", "InVideo", "3 Months", "₹15,000 / month", "Mumbai / Remote", "BBA / BCom / BA / MBA", "Social media growth experiments, SEO blog writing.", "https://invideo.io/careers", ["digital marketing & seo"]),
        ("Human Resources & Talent Intern", "TCS", "6 Months", "₹15,000 / month", "Pune / Hyderabad", "BBA / MBA / BA / BCom", "Campus recruitment coordination and candidate onboarding.", "https://www.tcs.com/careers", ["human resource management", "communication & public speaking"]),
    ]

    added_internships = 0
    for title, org, dur, stip, loc, elig, desc, url, sk_names in internships_master:
        obj, created = Internship.objects.get_or_create(
            title=title,
            organization=org,
            defaults={
                'duration': dur,
                'stipend': stip,
                'location': loc,
                'eligibility': elig,
                'description': desc,
                'application_url': url
            }
        )
        if created:
            added_internships += 1

        for sk_n in sk_names:
            sk_obj = Skill.objects.filter(name__iexact=sk_n).first()
            if sk_obj:
                obj.required_skills.add(sk_obj)

    print(f"Successfully seeded {added_internships} Internships for ALL 15 Degrees! Total Internships in DB: {Internship.objects.count()}.")

if __name__ == "__main__":
    seed_50_internships()
