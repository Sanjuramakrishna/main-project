import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import ProjectIdea
from profiles.models import Skill

print("Seeding Project Ideas across all categories...")

# Project data definitions with skill names
PROJECTS_DATA = [
    # ----------------------------------------------------
    # TECH & SOFTWARE ENGINEERING
    # ----------------------------------------------------
    {
        "title": "AI-Powered Medical Image Diagnostic Dashboard",
        "domain": "Tech",
        "difficulty": "Advanced",
        "skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "React"],
        "description": "Build an end-to-end web application that processes chest X-rays and MRI scans using Convolutional Neural Networks (CNN) to assist radiologists with preliminary abnormality detection.",
        "expected_outcome": "Working full-stack web dashboard with image upload, real-time inference heatmap visualization, and automated PDF medical diagnostic report generation."
    },
    {
        "title": "Full-Stack E-Commerce Platform with Microservices",
        "domain": "Tech",
        "difficulty": "Intermediate",
        "skills": ["Python", "Django", "JavaScript", "React", "PostgreSQL", "Docker"],
        "description": "Design and develop a scalable multi-vendor e-commerce portal with user authentication, shopping cart state management, Stripe payment gateway integration, and order tracking.",
        "expected_outcome": "Deployed containerized web application on Cloud with JWT authentication, RESTful APIs, and responsive mobile-first UI."
    },
    {
        "title": "Real-Time Stock Market Data Pipeline & Analytics",
        "domain": "Tech",
        "difficulty": "Intermediate",
        "skills": ["Python", "SQL", "Apache Kafka", "Data Analysis", "Pandas"],
        "description": "Engineer a streaming data ingestion pipeline consuming real-time financial ticker data, storing time-series aggregates in SQL, and calculating technical indicators (RSI, Moving Averages).",
        "expected_outcome": "Interactive dashboard with live price streaming charts and automated threshold alert notifications."
    },
    {
        "title": "Zero-Trust Cloud Security & Identity Compliance Auditor",
        "domain": "Tech",
        "difficulty": "Advanced",
        "skills": ["Cybersecurity", "Cloud Computing", "AWS", "Python", "Linux"],
        "description": "Automate security auditing across AWS cloud infrastructure to identify misconfigured S3 buckets, open security groups, and non-compliant IAM role policies according to CIS benchmarks.",
        "expected_outcome": "Command-line and web portal tool generating comprehensive JSON/PDF risk assessment reports."
    },

    # ----------------------------------------------------
    # MEDICAL & HEALTHCARE
    # ----------------------------------------------------
    {
        "title": "Telemedicine Consultation & Electronic Health Record (EHR) Portal",
        "domain": "Medical",
        "difficulty": "Advanced",
        "skills": ["Clinical Diagnostics", "Patient Care", "Medical Terminology", "Health Informatics"],
        "description": "Design a HIPAA-compliant clinical tele-consultation workflow complete with structured patient intake, ICD-10 diagnostic coding, e-prescriptions, and vital signs monitoring history.",
        "expected_outcome": "Interactive patient chart prototype and clinical consultation protocol documentation."
    },
    {
        "title": "Pharmacovigilance Adverse Drug Reaction (ADR) Monitoring System",
        "domain": "Medical",
        "difficulty": "Intermediate",
        "skills": ["Pharmacology", "Drug Safety", "Clinical Research", "Data Analysis"],
        "description": "Analyze clinical trial and post-marketing surveillance dataset to flag potential adverse drug interactions and calculate safety signals using WHO-UMC causality assessment scale.",
        "expected_outcome": "Comprehensive pharmacovigilance audit report and signal detection statistical matrix."
    },
    {
        "title": "Hospital Emergency Triage Protocol & ICU Occupancy Simulator",
        "domain": "Medical",
        "difficulty": "Intermediate",
        "skills": ["Emergency Medicine", "Patient Care", "Clinical Diagnostics", "Healthcare Management"],
        "description": "Establish a patient triage categorization model based on Emergency Severity Index (ESI) levels to streamline ER patient flow and optimize ventilator/ICU bed allocation.",
        "expected_outcome": "Emergency Department triage operational manual and resource allocation workflow chart."
    },

    # ----------------------------------------------------
    # COMMERCE & FINANCE
    # ----------------------------------------------------
    {
        "title": "Corporate Financial Statement Modeling & Valuation Dashboard",
        "domain": "Commerce",
        "difficulty": "Advanced",
        "skills": ["Financial Modeling", "Corporate Finance", "Financial Analysis", "Accounting", "Excel"],
        "description": "Construct a dynamic 3-statement integrated financial model (P&L, Balance Sheet, Cash Flow) with Discounted Cash Flow (DCF) valuation and sensitivity analysis for listed companies.",
        "expected_outcome": "Fully automated Excel financial model with dynamic scenario analysis toggles and valuation summary pitch deck."
    },
    {
        "title": "Automated GST Compliance & Tax Audit Reconciliation Tool",
        "domain": "Commerce",
        "difficulty": "Intermediate",
        "skills": ["GST & Income Tax", "Statutory Audit", "Accounting", "Tally", "Excel"],
        "description": "Build an automated reconciliation engine comparing GSTR-2B purchase logs against internal books of accounts to detect mismatched input tax credits (ITC) and vendor tax defaults.",
        "expected_outcome": "Tax reconciliation report highlighting tax discrepancies and vendor compliance ratings."
    },
    {
        "title": "Personal Wealth & Multi-Asset Portfolio Performance Tracker",
        "domain": "Commerce",
        "difficulty": "Beginner",
        "skills": ["Financial Analysis", "Investment Banking", "Excel", "Data Analysis"],
        "description": "Create a portfolio management workbook tracking mutual funds, equity stocks, and fixed income yields with Sharpe Ratio and CAGR calculations.",
        "expected_outcome": "Interactive financial dashboard showcasing asset allocation heatmaps and risk-adjusted return metrics."
    },

    # ----------------------------------------------------
    # LAW & LEGAL SERVICES
    # ----------------------------------------------------
    {
        "title": "AI Legal Contract Clause Analyzer & Risk Screener",
        "domain": "Legal",
        "difficulty": "Advanced",
        "skills": ["Legal Drafting", "Contract Law", "Legal Research", "Corporate Law"],
        "description": "Develop a legal document analysis framework to review Commercial NDAs and Master Service Agreements (MSA) for indemnity clauses, termination notice periods, and jurisdiction liabilities.",
        "expected_outcome": "Redlined contract report with risk scores and standardized renegotiation clause suggestions."
    },
    {
        "title": "Corporate Mergers & Acquisitions (M&A) Legal Due Diligence Toolkit",
        "domain": "Legal",
        "difficulty": "Intermediate",
        "skills": ["Corporate Law", "Legal Drafting", "Legal Research", "Compliance"],
        "description": "Draft a comprehensive due diligence checklist and regulatory approval roadmap under the Companies Act for cross-border corporate mergers.",
        "expected_outcome": "Complete legal due diligence binder, regulatory filing schedule, and risk mitigation framework."
    },

    # ----------------------------------------------------
    # AGRICULTURE & FORESTRY
    # ----------------------------------------------------
    {
        "title": "IoT Smart Agriculture & Soil Nutrient Recommendation Engine",
        "domain": "Agriculture",
        "difficulty": "Intermediate",
        "skills": ["Agronomy", "Soil Science", "Data Analysis", "Python"],
        "description": "Analyze NPK (Nitrogen, Phosphorus, Potassium) soil moisture sensor readings to recommend optimal fertilizer dosage and crop rotation schedules for sustainable farming.",
        "expected_outcome": "Crop yield advisory report and soil nutrient decision support system prototype."
    },

    # ----------------------------------------------------
    # ARCHITECTURE & DESIGN
    # ----------------------------------------------------
    {
        "title": "Sustainable Eco-Friendly Urban Residential Housing Blueprint",
        "domain": "Architecture",
        "difficulty": "Advanced",
        "skills": ["CAD Drafting", "BIM", "Structural Design", "Urban Planning"],
        "description": "Design a net-zero residential complex integrating passive solar design, rainwater harvesting systems, and energy-efficient HVAC spatial layouts in accordance with NBC norms.",
        "expected_outcome": "Complete 3D architectural elevation render, BIM model, and LEED green building rating compliance sheet."
    },

    # ----------------------------------------------------
    # ARTS, MEDIA & DESIGN
    # ----------------------------------------------------
    {
        "title": "Digital Media Brand Identity & Design System",
        "domain": "Arts",
        "difficulty": "Intermediate",
        "skills": ["Graphic Design", "UI/UX Design", "Content Writing", "Digital Marketing"],
        "description": "Construct a cohesive visual design system including typography guidelines, color palettes, micro-interactions, and component UI design systems for a modern digital media publication.",
        "expected_outcome": "Figma design system UI kit, brand guidelines book, and high-fidelity interactive prototype."
    },

    # ----------------------------------------------------
    # BASIC SCIENCE & RESEARCH
    # ----------------------------------------------------
    {
        "title": "Bioinformatics Enzyme Active Site Sequence Matcher",
        "domain": "Science",
        "difficulty": "Intermediate",
        "skills": ["Biotechnology", "Data Analysis", "Python", "Genomics"],
        "description": "Build an algorithmic tool parsing FASTA protein sequences to identify conserved catalytic domain motifs and infer enzymatic function against UniProt databases.",
        "expected_outcome": "Multiple sequence alignment pipeline and phylogenetic tree visualizer."
    }
]

created_count = 0
for data in PROJECTS_DATA:
    proj, created = ProjectIdea.objects.get_or_create(
        title=data["title"],
        defaults={
            "domain": data["domain"],
            "difficulty": data["difficulty"],
            "description": data["description"],
            "expected_outcome": data["expected_outcome"],
        }
    )
    if not created:
        proj.domain = data["domain"]
        proj.difficulty = data["difficulty"]
        proj.description = data["description"]
        proj.expected_outcome = data["expected_outcome"]
        proj.save()

    # Attach matching skills
    skill_objs = []
    for sname in data["skills"]:
        s_obj, _ = Skill.objects.get_or_create(
            name=sname,
            defaults={"category": data["domain"] if data["domain"] != "Tech" else "Technical"}
        )
        skill_objs.append(s_obj)
    
    proj.required_skills.set(skill_objs)
    created_count += 1

print(f"Successfully seeded {created_count} Project Ideas across all categories!")
