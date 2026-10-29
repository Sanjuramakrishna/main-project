import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from profiles.models import Skill
from opportunities.models import Course, Certification

def seed_courses_and_certs():
    print("Seeding courses and certifications for all streams and degrees...")

    courses_data = [
        # Technical & CS
        ("Python for Everybody Specialization", "YouTube", "Beginner", "Python", "Master Python programming fundamentals, data structures, databases, and web scraping.", "https://www.py4e.com/"),
        ("Complete Python 3 Masterclass 2026", "Udemy", "Intermediate", "Python", "Deep dive into object-oriented programming, decorators, generators, and async Python.", "https://www.udemy.com/course/python-the-complete-python-developer-bootcamp/"),
        ("Java Programming & Object-Oriented Fundamentals", "Coursera", "Beginner", "Java", "Core Java syntax, OOP design patterns, inheritance, collection framework, and exception handling.", "https://www.coursera.org/learn/java-programming"),
        ("Spring Boot & Microservices Masterclass", "Udemy", "Advanced", "Java", "Build production enterprise REST APIs with Spring Boot, Spring Security, and PostgreSQL.", "https://www.udemy.com/course/spring-hibernate-tutorial/"),
        ("Modern JavaScript (ES6+) Complete Guide", "W3Schools", "Beginner", "JavaScript", "Asynchronous JavaScript, Promises, Async/Await, DOM manipulation, and modern syntax.", "https://www.w3schools.com/js/"),
        ("React - The Complete Guide 2026", "Udemy", "Intermediate", "React", "Build modern dynamic single-page web applications with React Hooks, Context API, and Redux.", "https://www.udemy.com/course/react-the-complete-guide-incl-redux/"),
        ("HTML5, CSS3 & Responsive Web Design", "W3Schools", "Beginner", "HTML & CSS", "Create beautiful glassmorphism and mobile-responsive layouts using modern flexbox and grid.", "https://www.w3schools.com/html/"),
        ("Node.js, Express & MongoDB Developer Bootcamp", "Udemy", "Intermediate", "Node.js", "Build scalable server-side web applications and REST APIs using JavaScript.", "https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/"),
        ("SQL & Relational Database Mastery", "GeeksforGeeks", "Beginner", "SQL & Databases", "Master SQL queries, JOINs, subqueries, indexing, window functions, and database schema design.", "https://www.geeksforgeeks.org/sql-tutorial/"),
        ("Data Structures & Algorithms in Python/Java", "GeeksforGeeks", "Intermediate", "Data Structures & Algorithms", "Master stacks, queues, trees, graphs, dynamic programming, and competitive problem solving.", "https://www.geeksforgeeks.org/data-structures/"),
        ("Cybersecurity Fundamentals & Network Defense", "Coursera", "Beginner", "Cybersecurity & Networking", "Learn network protocols, cryptography, ethical hacking, OWASP Top 10, and firewall security.", "https://www.coursera.org/specializations/cyber-security"),

        # Data & AI / Science
        ("Machine Learning A-Z: Hands-on Python & R", "Udemy", "Intermediate", "Machine Learning", "Build regression, classification, clustering models, and Random Forest / XGBoost pipelines.", "https://www.udemy.com/course/machinelearning/"),
        ("Deep Learning & PyTorch Masterclass", "Coursera", "Advanced", "Deep Learning & PyTorch", "Train convolutional neural networks (CNNs), transformers, and generative AI models.", "https://www.coursera.org/specializations/deep-learning"),
        ("Data Analysis with Pandas & NumPy", "YouTube", "Beginner", "Pandas & NumPy", "Master data manipulation, cleaning, aggregation, and tabular data transformation.", "https://www.youtube.com/results?search_query=pandas+numpy+course"),
        ("Scikit-Learn for Machine Learning Pipelines", "GeeksforGeeks", "Intermediate", "Scikit-Learn", "Feature engineering, model validation, hyperparameter tuning, and model evaluation.", "https://www.geeksforgeeks.org/scikit-learn-tutorial/"),
        ("Data Visualization with Tableau & Power BI", "Udemy", "Beginner", "Data Visualization (Tableau/PowerBI)", "Create interactive dashboards, corporate KPI reports, and visual data storytelling.", "https://www.udemy.com/course/tableau10/"),

        # Tools & Cloud
        ("Docker & Kubernetes: Complete Developer Guide", "Udemy", "Intermediate", "Docker & Kubernetes", "Containerize applications, configure microservices, and deploy multi-node clusters.", "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/"),
        ("AWS Certified Solutions Architect Associate", "Simplilearn", "Intermediate", "AWS & Cloud Computing", "Master AWS EC2, S3, RDS, Lambda, VPC networking, and cloud security architecture.", "https://www.simplilearn.com/aws-certified-solutions-architect-associate-training"),
        ("Git & GitHub Complete Practical Guide", "YouTube", "Beginner", "Git & GitHub", "Learn version control, branching strategies, merge conflict resolution, and pull requests.", "https://www.youtube.com/results?search_query=git+github+full+course"),
        ("UI/UX Design Essentials with Figma", "Udemy", "Beginner", "UI/UX Design & Figma", "Design intuitive user interfaces, wireframes, interactive prototypes, and design systems.", "https://www.udemy.com/course/ui-ux-design-using-figma/"),

        # Business, Management & Commerce
        ("Financial Modeling & Valuation Complete Course", "Udemy", "Intermediate", "Financial Modeling & Excel", "Build discounted cash flow (DCF) models, corporate valuation, and advanced Excel analysis.", "https://www.udemy.com/course/beginner-to-pro-in-excel-financial-modeling-and-valuation/"),
        ("Digital Marketing & Google SEO Masterclass 2026", "Coursera", "Beginner", "Digital Marketing & SEO", "Master search engine optimization, Google Ads, content marketing, and social media ROI.", "https://www.coursera.org/specializations/digital-marketing"),
        ("Agile & Scrum Project Management Certification", "Simplilearn", "Beginner", "Agile & Project Management", "Master Scrum frameworks, sprint planning, JIRA issue tracking, and product backlog management.", "https://www.simplilearn.com/agile-and-scrum-certification-training"),
        ("Business Analysis & Requirements Engineering", "Coursera", "Intermediate", "Business Analysis", "Translate business goals into functional requirements, process flow diagrams, and user stories.", "https://www.coursera.org/specializations/business-analysis"),

        # Core Engineering & Soft Skills
        ("SolidWorks 3D CAD Modeling Masterclass", "Udemy", "Intermediate", "CAD & SolidWorks", "Design mechanical parts, 3D assemblies, technical drawings, and finite element analysis.", "https://www.udemy.com/course/solidworks-course/"),
        ("Embedded Systems Programming with C & ARM", "Coursera", "Intermediate", "Embedded C / Microcontrollers", "Program ARM Cortex microcontrollers, GPIO, timers, interrupts, and UART communication.", "https://www.coursera.org/learn/embedded-systems"),
        ("Professional Business Communication & Public Speaking", "Coursera", "Beginner", "Communication & Public Speaking", "Develop executive presentation skills, email etiquette, and persuasive technical communication.", "https://www.coursera.org/specializations/business-communications")
    ]

    added_courses = 0
    for title, provider, diff, skill_name, desc, url in courses_data:
        skill_obj = Skill.objects.filter(name__iexact=skill_name).first()
        if not skill_obj:
            # Fallback search
            skill_obj = Skill.objects.filter(name__icontains=skill_name.split()[0]).first()
        
        if skill_obj:
            course, created = Course.objects.get_or_create(
                title=title,
                skill=skill_obj,
                defaults={
                    'provider': provider,
                    'difficulty': diff,
                    'description': desc,
                    'url': url
                }
            )
            if created:
                added_courses += 1

    print(f"Successfully seeded {added_courses} new courses across all streams and degrees!")

    # Certifications Seeding
    certs_data = [
        ("AWS Certified Solutions Architect", "Amazon Web Services", "AWS & Cloud Computing", "Industry benchmark certification validating cloud architecture and AWS infrastructure setup.", "https://aws.amazon.com/certification/"),
        ("Google Data Analytics Professional Certificate", "Google", "Pandas & NumPy", "Validates end-to-end data processing, SQL querying, R/Python visualization, and storytelling.", "https://grow.google/certificates/data-analytics/"),
        ("Meta Front-End Developer Professional Certificate", "Meta", "React", "Official certification covering HTML, CSS, JavaScript, React, and UX design principles.", "https://www.coursera.org/professional-certificates/meta-front-end-developer"),
        ("Financial Modeling & Valuation Analyst (FMVA)", "CFI Institute", "Financial Modeling & Excel", "Global certification for corporate finance analyst, financial modeling, and company valuation.", "https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva/"),
        ("Google Digital Marketing & E-commerce Certificate", "Google", "Digital Marketing & SEO", "Official credential covering search optimization, Google Analytics 4, and email campaigns.", "https://grow.google/certificates/digital-marketing-ecommerce/"),
        ("Certified ScrumMaster (CSM)", "Scrum Alliance", "Agile & Project Management", "Premier agile project management credential for leading cross-functional tech teams.", "https://www.scrumalliance.org/get-certified/scrum-master-track/certified-scrummaster"),
        ("TensorFlow Developer Certificate", "Google / TensorFlow", "Machine Learning", "Validates proficiency in building computer vision and NLP models using TensorFlow & Keras.", "https://www.tensorflow.org/certificate"),
        ("Certified Information Systems Security Professional (CISSP)", "(ISC)²", "Cybersecurity & Networking", "Globally recognized gold standard certification for IT security and cybersecurity leadership.", "https://www.isc2.org/Certifications/CISSP")
    ]

    added_certs = 0
    for title, org, skill_name, desc, url in certs_data:
        skill_obj = Skill.objects.filter(name__iexact=skill_name).first()
        if not skill_obj:
            skill_obj = Skill.objects.filter(name__icontains=skill_name.split()[0]).first()

        if skill_obj:
            cert, created = Certification.objects.get_or_create(
                title=title,
                skill=skill_obj,
                defaults={
                    'issuing_organization': org,
                    'description': desc,
                    'url': url
                }
            )
            if created:
                added_certs += 1

    print(f"Successfully seeded {added_certs} new certifications across all streams!")

if __name__ == '__main__':
    seed_courses_and_certs()
