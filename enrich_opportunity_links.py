import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity, Internship, Course, Certification, GovernmentExam
from profiles.models import Skill

print("Starting opportunity data enrichment with direct official portal URLs...")

# 1. ENRICH & SEED COURSES & LEARNING RESOURCES
courses_master = [
    # GeeksforGeeks
    ("DSA Self-Paced & System Design", "GeeksforGeeks", "Intermediate", "Data Structures & Algorithms", "Master Data Structures, Algorithms, Arrays, Trees, Graphs, and DP with GeeksforGeeks.", "https://www.geeksforgeeks.org/courses/dsa-self-paced"),
    ("Python Programming Foundation", "GeeksforGeeks", "Beginner", "Python", "Complete Python syntax, data types, functions, modules, and OOP concepts on GFG.", "https://www.geeksforgeeks.org/courses/python-foundation"),
    
    # W3Schools
    ("W3Schools Complete Web Development Tutorial", "W3Schools", "Beginner", "HTML & CSS", "Learn HTML5, CSS3, JavaScript, Responsive Flexbox, and Grid with interactive code runner.", "https://www.w3schools.com/html/"),
    ("JavaScript & ES6+ Certification Course", "W3Schools", "Beginner", "JavaScript", "Master modern JavaScript, DOM manipulation, Async/Await, and Web APIs.", "https://www.w3schools.com/js/"),
    
    # Udemy
    ("The Web Developer Bootcamp 2026", "Udemy", "Beginner", "React", "Build responsive web applications with HTML, CSS, JS, Node.js, and React.", "https://www.udemy.com/course/the-web-developer-bootcamp/"),
    ("Complete SQL & Database Management", "Udemy", "Intermediate", "SQL & Databases", "Master PostgreSQL, MySQL, complex joins, subqueries, and database indexing.", "https://www.udemy.com/course/the-complete-sql-bootcamp/"),

    # Coursera
    ("Google Data Analytics Professional Certificate", "Coursera", "Beginner", "Pandas & NumPy", "Learn data cleaning, SQL queries, R/Python, Tableau, and data visualization from Google.", "https://www.coursera.org/professional-certificates/google-data-analytics"),
    ("AWS Cloud Technical Essentials", "Coursera", "Intermediate", "AWS & Cloud Computing", "Learn Amazon S3, EC2, IAM, Lambda, VPC, and cloud infrastructure best practices.", "https://www.coursera.org/learn/aws-cloud-technical-essentials"),

    # Simplilearn
    ("Machine Learning & AI SkillUp Course", "Simplilearn", "Intermediate", "Machine Learning", "Free skillup course covering supervised learning, Scikit-Learn, and regression algorithms.", "https://www.simplilearn.com/skillup-free-online-courses"),
    ("Cybersecurity Fundamentals Masterclass", "Simplilearn", "Beginner", "Cybersecurity & Networking", "Learn network security, ethical hacking concepts, cryptography, and SIEM tools.", "https://www.simplilearn.com/cyber-security-skillup-free-course-skillup"),

    # LeetCode & HackerRank
    ("LeetCode Top 150 Interview Problems", "LeetCode", "Advanced", "Data Structures & Algorithms", "Practice top technical interview problems for Google, Amazon, Microsoft, and TCS.", "https://leetcode.com/studyplan/top-interview-150/"),
    ("HackerRank Problem Solving & Python Skill Cert", "HackerRank", "Intermediate", "Python", "Solve algorithmic challenges, data structures, and earn HackerRank verified skill badges.", "https://www.hackerrank.com/domains/python"),

    # Infosys Springboard & TCS iON
    ("Infosys Springboard AI & Java Professional Track", "Infosys Springboard", "Beginner", "Java", "Official Infosys Springboard curriculum covering Object-Oriented Java and Microservices.", "https://infyspringboard.onwingspan.com"),
    ("TCS iON Digital Learning - Cloud & Agile Foundations", "TCS iON", "Beginner", "Agile & Project Management", "TCS iON certified digital learning course on Agile Scrum methodologies and IT service management.", "https://learning.tcsionhub.in"),

    # Tap Academy, Pentagon Space & Dhee Coding
    ("Full Stack Web Development & Java Bootcamp", "Tap Academy", "Beginner", "Java", "Interactive visual coding bootcamp by Tap Academy covering Core Java, SQL, and Web Tech.", "https://tapacademy.com/full-stack-web-development-course/"),
    ("Master Data Science & AI Industrial Program", "Pentagon Space", "Intermediate", "Data Visualization (Tableau/PowerBI)", "Pentagon Space comprehensive program covering Python, Data Analytics, Tableau, and Machine Learning.", "https://pentagonspace.in/courses"),
    ("Dhee Coding Complete Programming Foundations", "Dhee Coding", "Beginner", "C++", "Dhee Coding structured coding platform for mastering C++, DS, and competitive programming.", "https://dheecoding.com"),

    # GitHub Education
    ("GitHub Student Developer Pack & Git Mastery", "GitHub", "Beginner", "Git & GitHub", "Access free developer tools, domain credits, GitHub Copilot, and Git version control guides.", "https://github.com/education")
]

for title, prov, diff, sk_name, desc, url in courses_master:
    sk_obj = Skill.objects.filter(name=sk_name).first()
    if sk_obj:
        Course.objects.update_or_create(
            title=title,
            defaults={
                "provider": prov if prov in ['YouTube', 'GeeksforGeeks', 'W3Schools', 'Udemy', 'Coursera', 'Simplilearn', 'NPTEL'] else 'Coursera',
                "difficulty": diff,
                "skill": sk_obj,
                "description": desc,
                "url": url
            }
        )

# 2. ENRICH & SEED JOBS & INTERNSHIPS WITH DIRECT PORTAL LINKS
jobs_master = [
    ("Associate Software Engineer", "Google Careers", "Tech", "Bengaluru (Hybrid)", "Full-time", "₹14.0 - ₹24 LPA", "0 - 2 Years", "Build scalable global web services, backend APIs, and distributed data pipelines at Google.", "https://careers.google.com/jobs/results/?q=software%20engineer"),
    ("System Engineer Trainee", "TCS iON", "Tech", "Bengaluru / Hyderabad / Chennai", "Full-time", "₹4.5 - ₹7.5 LPA", "0 - 1 Years", "Develop enterprise software solutions, Cloud deployments, and database automation.", "https://www.tcs.com/careers"),
    ("Systems Engineer", "Infosys", "Tech", "Bengaluru / Mysuru", "Full-time", "₹4.2 - ₹8.0 LPA", "0 - 1 Years", "Full-stack development, Java microservices, and cloud infrastructure support at Infosys.", "https://www.infosys.com/careers/"),
    ("Application Development Associate", "Accenture", "Tech", "Bengaluru / Pune", "Full-time", "₹4.8 - ₹8.5 LPA", "0 - 2 Years", "Design and deploy web applications using React, Java, Node.js, and Cloud services.", "https://www.accenture.com/in-en/careers/jobsearch"),
    ("Junior AI & Machine Learning Developer", "Unstop Opportunities", "Tech", "Remote / Bengaluru", "Remote", "₹8.0 - ₹12 LPA", "0 - 2 Years", "Work on predictive modeling, NLP pipelines, and computer vision datasets.", "https://unstop.com/jobs"),
    ("Data Analyst & Business Intelligence Specialist", "Naukri Portal", "Tech", "Mumbai / Gurgaon", "Full-time", "₹5.5 - ₹9.5 LPA", "0 - 2 Years", "Extract business insights using SQL, Python pandas, and Tableau / PowerBI dashboards.", "https://www.naukri.com/data-analyst-jobs"),
    ("Full Stack Software Engineer", "LinkedIn Jobs", "Tech", "Remote / Hyderabad", "Remote", "₹7.0 - ₹15 LPA", "0 - 2 Years", "Develop REST APIs, Django backend models, and React single-page frontend interfaces.", "https://www.linkedin.com/jobs/search/?keywords=Full%20Stack%20Developer"),
    ("Graduate Engineer Trainee (GET)", "Pentagon Space Placement Cell", "Tech", "Bengaluru", "Full-time", "₹5.0 - ₹8.0 LPA", "Freshers", "Placement opportunity for trained GET candidates in Java, Python, and SQL.", "https://pentagonspace.in/careers"),
    ("Junior Software Developer", "Tap Academy Placements", "Tech", "Bengaluru / Remote", "Full-time", "₹4.5 - ₹7.0 LPA", "Freshers", "Direct recruiter hiring for Tap Academy trained software engineering candidates.", "https://tapacademy.com/placements"),
    ("Junior Developer", "Dhee Coding Placements", "Tech", "Bengaluru", "Full-time", "₹4.0 - ₹6.5 LPA", "Freshers", "Targeted hiring for competitive coders proficient in C++, Data Structures, and Web Tech.", "https://dheecoding.com")
]

for jtitle, comp, dom, loc, jtype, sal, exp, desc, url in jobs_master:
    JobOpportunity.objects.update_or_create(
        title=jtitle, company=comp,
        defaults={
            "domain": dom,
            "location": loc,
            "job_type": jtype,
            "salary_range": sal,
            "experience_required": exp,
            "description": desc,
            "application_url": url,
            "is_active": True
        }
    )

internships_master = [
    ("Software Development Intern 2026", "Unstop Internships", "Tech", "6 Months", "₹25,000 / month", "Remote", "BE / BTech / BCA / MCA", "Build real-world web apps and algorithms with mentorship on Unstop.", "https://unstop.com/internships"),
    ("VTU University Portal Internship Drive", "Seek VTU / VTU Internship", "Tech", "3 Months", "₹15,000 / month", "Bengaluru / Belagavi", "VTU Affiliated Engineering Students", "Official VTU internship initiative connecting students with leading Karnataka technology companies.", "https://internship.vtu.ac.in"),
    ("Google STEP Software Internship", "Google Careers", "Tech", "3 Months", "₹50,000 / month", "Bengaluru / Hyderabad", "BTech 2nd & 3rd Year CS Students", "Google Student Training in Engineering Program (STEP) software engineering internship.", "https://careers.google.com/jobs/results/?q=intern"),
    ("Infosys Springboard AI Internship", "Infosys Springboard", "Tech", "3 Months", "₹18,000 / month", "Remote", "All Engineering & Degree Students", "Guided project-based virtual internship on AI, Cloud, and Web technologies.", "https://infyspringboard.onwingspan.com"),
    ("TCS iON Remote Internship Program", "TCS iON", "Tech", "2 Months", "Certificate + Stipend", "Remote", "Final & Pre-Final Year Students", "TCS iON industry-aligned virtual internship with live project mentorship.", "https://learning.tcsionhub.in"),
    ("Open Source Developer Fellow", "GitHub Education", "Tech", "4 Months", "₹20,000 / month", "Remote", "GitHub Student Pack Members", "Contribute to high-impact open source repositories and toolings on GitHub.", "https://github.com/education")
]

for ititle, org, dom, dur, stip, loc, elig, desc, url in internships_master:
    Internship.objects.update_or_create(
        title=ititle, organization=org,
        defaults={
            "domain": dom,
            "duration": dur,
            "stipend": stip,
            "location": loc,
            "eligibility": elig,
            "description": desc,
            "application_url": url
        }
    )

print("SUCCESS: Enriched opportunities data with direct official portal URLs!")
