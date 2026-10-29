import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import GovernmentExam

EXAM_DETAILS = [
    # =========================================================================
    # GOVERNMENT & PSU EXAMS (1 to 40)
    # =========================================================================
    # 1. UPSC Civil Services
    {
        'exam_name': 'UPSC Civil Services Examination (IAS/IPS/IFS)',
        'category': 'govt',
        'domain': 'Civil Services & Administration',
        'conducting_body': 'UPSC',
        'website_url': 'https://upsc.gov.in/examinations/Civil%20Services%20%28Preliminary%29%20Examination',
        'eligibility': "Qualification: Graduation degree in any discipline from a recognized University. Age Limit: 21–32 years (Relaxation: 3 yrs for OBC, 5 yrs for SC/ST, 10 yrs for PwBD). Nationality: Citizen of India for IAS & IPS. Percentage: Pass class/marks eligible.",
        'syllabus_summary': "Prelims: Paper I (GS - 200 Marks: History, Geography, Polity, Economy, Environment) & Paper II (CSAT - 200 Marks: Quant & Reasoning, qualifying 33%). Mains: 9 Descriptive papers (1750 Marks) + Personality Test (275 Marks). Total: 2025 Marks.",
        'preparation_resources': "• NPTEL & RSTV UPSC Prep Lectures: https://www.youtube.com/results?search_query=UPSC+Civil+Services+preparation+free+lectures\n• Sleepy Classes IAS GS Complete Course: https://www.youtube.com/results?search_query=Sleepy+Classes+UPSC+GS+complete+course\n• StudyIQ IAS Polity & Economy Series: https://www.youtube.com/results?search_query=StudyIQ+IAS+Polity+and+Economy+free+playlist",
        'application_start_date': "February 2026",
        'application_last_date': "March 2026",
        'exam_date': "May 2026 (Prelims) / Sept 2026 (Mains)",
        'exam_timings': "Morning Shift: 09:30 AM – 11:30 AM | Afternoon Shift: 02:30 PM – 04:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 2. GATE 2027
    {
        'exam_name': 'GATE 2027 (Graduate Aptitude Test in Engineering)',
        'category': 'govt',
        'domain': 'Computer Science & Engineering',
        'conducting_body': 'IIT Madras / GATE Committee',
        'website_url': 'https://gate2027.iitm.ac.in/',
        'eligibility': "Qualification: Currently in 3rd year or higher of B.E/B.Tech/B.Arch/B.Sc/M.Sc/MCA or completed degree. Age Limit: No age limit. Nationality: Indian and international candidates from eligible nations. Percentage: No minimum percentage requirement.",
        'syllabus_summary': "Duration: 3 Hours (CBT). Total Questions: 65 (100 Marks). Format: MCQs, MSQs, and NATs. Distribution: General Aptitude (15 Marks) + Engineering Mathematics (13 Marks) + Core Discipline (72 Marks). Negative marking for MCQs (1/3rd for 1-mark, 2/3rd for 2-mark Qs).",
        'preparation_resources': "• Gate Smashers CS & Engineering Complete Playlists: https://www.youtube.com/results?search_query=Gate+Smashers+GATE+CS+complete+playlist\n• NPTEL Official GATE Preparation Lectures: https://www.youtube.com/results?search_query=NPTEL+GATE+Engineering+Mathematics+and+CS\n• Unacademy Computer Science Free GATE Series: https://www.youtube.com/results?search_query=Unacademy+GATE+CS+lectures+playlist",
        'application_start_date': "August 2026",
        'application_last_date': "October 2026",
        'exam_date': "February 2027",
        'exam_timings': "Forenoon Shift: 09:30 AM – 12:30 PM | Afternoon Shift: 02:30 PM – 05:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 3. Karnataka PGCET
    {
        'exam_name': 'Karnataka PGCET / PG KCET 2026-2027',
        'category': 'govt',
        'domain': 'Engineering & Management',
        'conducting_body': 'KEA Karnataka',
        'website_url': 'https://cetonline.karnataka.gov.in/kea/pgcet2026',
        'eligibility': "Qualification: B.E/B.Tech/BCA/B.Sc/B.Com/BBA from recognized university. Minimum Marks: 50% aggregate (45% for SC/ST/Cat-I candidates of Karnataka). Domicile: Mandatory for state quota seats. Age Limit: No upper age limit.",
        'syllabus_summary': "Mode: Offline OMR. Questions: 100 MCQs (100 Marks). Duration: 120 Minutes. Sections: Core Technical Subjects (Mathematics, CS, ECE, Mechanical), Quantitative Aptitude, Reasoning, General Knowledge. No negative marking.",
        'preparation_resources': "• Karnataka PGCET MCA & Engineering Prep: https://www.youtube.com/results?search_query=Karnataka+PGCET+MCA+MBA+Engineering+preparation\n• KEA PGCET Maths & Reasoning Classes: https://www.youtube.com/results?search_query=KEA+PGCET+preparation+lectures",
        'application_start_date': "May 2026",
        'application_last_date': "June 2026",
        'exam_date': "August 2026",
        'exam_timings': "Morning Shift: 10:30 AM – 12:30 PM | Afternoon Shift: 02:30 PM – 04:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 4. SSC CGL
    {
        'exam_name': 'SSC CGL (Staff Selection Commission Combined Graduate Level)',
        'category': 'govt',
        'domain': 'Staff Selection & Administrative',
        'conducting_body': 'SSC Govt of India',
        'website_url': 'https://ssc.gov.in/candidate-portal/examinations/cgl',
        'eligibility': "Qualification: Bachelor's degree in any discipline from a recognized University. Age Limit: 18–32 years (depending on target post). Relaxation: 3 yrs OBC, 5 yrs SC/ST. Nationality: Citizen of India. Percentage: Passing degree.",
        'syllabus_summary': "Tier I (CBT - Qualifying): 100 Qs (200 Marks, 60 mins): Intelligence, Reasoning, GK, Quant, English. Tier II: Paper I (Mathematical Abilities, Reasoning, English, General Awareness, Computer Knowledge) + Data Entry Speed Test.",
        'preparation_resources': "• RBF Revolution SSC CGL Free Course: https://www.youtube.com/results?search_query=SSC+CGL+maths+reasoning+english+complete+course\n• Rankers Gurukul SSC CGL Complete Playlist: https://www.youtube.com/results?search_query=Rankers+Gurukul+SSC+CGL+full+playlist\n• Aditya Ranjan Sir Maths CGL Playlists: https://www.youtube.com/results?search_query=Aditya+Ranjan+Sir+Maths+SSC+CGL",
        'application_start_date': "June 2026",
        'application_last_date': "July 2026",
        'exam_date': "September 2026",
        'exam_timings': "Shift 1: 09:00 AM – 10:00 AM | Shift 2: 12:30 PM – 01:30 PM | Shift 3: 04:00 PM – 05:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 5. ISRO Scientist B
    {
        'exam_name': 'ISRO Scientist / Engineer SC Cadre Exam',
        'category': 'govt',
        'domain': 'Space Research & Supercomputing',
        'conducting_body': 'ISRO ICRB',
        'website_url': 'https://www.isro.gov.in/Careers.html',
        'eligibility': "Qualification: B.E/B.Tech or equivalent in CSE, ECE, Mechanical, Electrical with First Class. Minimum Percentage: 65% aggregate or 6.84/10 CGPA. Age Limit: 28 years (Relaxable for OBC/SC/ST). Nationality: Citizen of India.",
        'syllabus_summary': "Written Test: 80 Objective MCQs (75% Core Discipline + 25% Allied areas), 3 marks each, -1 negative mark for wrong answers. Duration: 120 Minutes. Personal Interview: 100 Marks (Qualifying min: 50% for UR).",
        'preparation_resources': "• ISRO Scientist B Preparation Series: https://www.youtube.com/results?search_query=ISRO+Scientist+Engineer+exam+preparation+lectures\n• Gate Smashers ISRO PYQs & Practice: https://www.youtube.com/results?search_query=Gate+Smashers+ISRO+Scientist+B+preparation",
        'application_start_date': "May 2026",
        'application_last_date': "June 2026",
        'exam_date': "November 2026",
        'exam_timings': "Single Shift: 10:00 AM – 12:00 PM",
        'exam_date_info': "Annual Recruitment Drive"
    },
    # 6. DRDO Scientist B
    {
        'exam_name': 'DRDO Scientist B Recruitment Exam',
        'category': 'govt',
        'domain': 'Defense Research & AI',
        'conducting_body': 'DRDO RAC',
        'website_url': 'https://rac.gov.in/index.php?lang=en&id=0',
        'eligibility': "Qualification: First Class Bachelor's Degree in Engineering/Technology in CSE, ECE, Mechanical, EE, Chemical from recognized University. Shortlisting: Valid GATE score card mandatory. Age Limit: 28–35 years. Nationality: Indian.",
        'syllabus_summary': "Selection Process: GATE Score Weightage (80%) + Personal Interview (20%) OR RAC Descriptive Written Exam (2 Papers, 300 Marks each, 3 hours each in Core Engineering discipline) followed by Personal Interview.",
        'preparation_resources': "• DRDO RAC Scientist B Guide & Lectures: https://www.youtube.com/results?search_query=DRDO+RAC+Scientist+B+preparation+guide\n• Made Easy DRDO & PSU Interview Prep: https://www.youtube.com/results?search_query=Made+Easy+DRDO+Scientist+B+interview+guidance",
        'application_start_date': "July 2026",
        'application_last_date': "August 2026",
        'exam_date': "October 2026",
        'exam_timings': "Paper 1: 09:30 AM – 12:30 PM | Paper 2: 02:00 PM – 05:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 7. NIC Scientist B
    {
        'exam_name': 'NIC Scientist B & Technical Assistant A',
        'category': 'govt',
        'domain': 'e-Governance & Full Stack Cloud',
        'conducting_body': 'NIELIT / NIC MeitY',
        'website_url': 'https://recruitment.nic.in/',
        'eligibility': "Qualification: B.E/B.Tech/M.Sc/MCA/M.Tech in CS, IT, Electronics, Cyber Security. Age Limit: 30 years (UR), 33 years (OBC), 35 years (SC/ST). Nationality: Citizen of India. Percentage: Pass class degree.",
        'syllabus_summary': "CBT Exam: 120 MCQs (120 Minutes, 1 Mark each, 0.25 Negative marking). Distribution: 65% Technical (CS/IT/Electronics - Data Structures, OS, DBMS, Security, Web Dev) + 35% Generic (Reasoning, Quant, English).",
        'preparation_resources': "• NIELIT NIC Scientist B Free Prep Videos: https://www.youtube.com/results?search_query=NIC+Scientist+B+NIELIT+exam+preparation+playlist\n• Knowledge Gate NIC Technical Assistant Lectures: https://www.youtube.com/results?search_query=Knowledge+Gate+NIC+Scientist+B",
        'application_start_date': "March 2026",
        'application_last_date': "April 2026",
        'exam_date': "July 2026",
        'exam_timings': "Single Shift: 10:00 AM – 12:00 PM",
        'exam_date_info': "Periodic MeitY Drive"
    },
    # 8. UPSC ESE / IES
    {
        'exam_name': 'UPSC Engineering Services Examination (ESE / IES)',
        'category': 'govt',
        'domain': 'Engineering & Power Systems',
        'conducting_body': 'UPSC',
        'website_url': 'https://upsc.gov.in/examinations/Engineering%20Services%20%28Preliminary%29%20Examination',
        'eligibility': "Qualification: Degree in Engineering (B.E/B.Tech) in Civil, Mechanical, Electrical, or ECE. Age Limit: 21–30 years (Relaxations: 3 yrs OBC, 5 yrs SC/ST). Nationality: Citizen of India. Percentage: Passing degree.",
        'syllabus_summary': "Stage I Prelims: 500 Marks (Paper 1 GS & Engineering Aptitude 200M + Paper 2 Discipline 300M). Stage II Mains: 600 Marks (2 Conventional Papers 300M each). Stage III Personality Test: 200 Marks. Total: 1300 Marks.",
        'preparation_resources': "• Made Easy ESE Prelims GS Lectures: https://www.youtube.com/results?search_query=UPSC+ESE+IES+Engineering+Services+free+lectures\n• ACE Engineering Academy ESE Prep Series: https://www.youtube.com/results?search_query=ACE+Academy+ESE+Engineering+Services+playlist",
        'application_start_date': "September 2026",
        'application_last_date': "October 2026",
        'exam_date': "February 2027 (Prelims) / June 2027 (Mains)",
        'exam_timings': "Paper I: 10:00 AM – 12:00 PM | Paper II: 02:00 PM – 05:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 9. RRB JE
    {
        'exam_name': 'RRB Junior Engineer (JE) & IT Officers Drive',
        'category': 'govt',
        'domain': 'Railway Software & Infrastructure',
        'conducting_body': 'Railway Recruitment Boards',
        'website_url': 'https://www.rrbcdg.gov.in/',
        'eligibility': "Qualification: 3-year Diploma or B.E/B.Tech in relevant Engineering branch (Civil, Mechanical, Electrical, CS, IT, Electronics). Age Limit: 18–33 years (Relaxable for reserved categories). Nationality: Indian citizen.",
        'syllabus_summary': "CBT 1 (Qualifying): 100 Qs (90 Mins: Mathematics 30, General Intelligence 25, General Awareness 15, General Science 30). CBT 2: 150 Qs (120 Mins: Technical Abilities 100 + Physics/Chemistry/Computers 50). Negative: 1/3rd.",
        'preparation_resources': "• Testbook RRB JE Tech Classes: https://www.youtube.com/results?search_query=RRB+JE+technical+classes+free+playlist\n• Engineers Academy RRB JE Classes: https://www.youtube.com/results?search_query=Engineers+Academy+RRB+JE+preparation",
        'application_start_date': "July 2026",
        'application_last_date': "August 2026",
        'exam_date': "December 2026",
        'exam_timings': "Shift 1: 09:00 AM – 10:30 AM | Shift 2: 12:30 PM – 02:00 PM | Shift 3: 04:00 PM – 05:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 10. SBI SCO
    {
        'exam_name': 'SBI Specialist Cadre Officer (SCO) & IT Officer',
        'category': 'govt',
        'domain': 'Banking & Financial IT',
        'conducting_body': 'State Bank of India',
        'website_url': 'https://bank.sbi/web/careers/current-openings',
        'eligibility': "Qualification: B.E/B.Tech/MCA/M.Sc in CS, IT, ECE from recognized University. Work Experience: Minimum 1–5 years post-qualification IT experience required for specific cadres. Age Limit: 25–35 years.",
        'syllabus_summary': "Online Test: Test of Knowledge (Reasoning, Quant, English - Qualifying) + Professional Knowledge Test (70 Qs, 100 Marks on Systems, Cloud Architecture, DB, Security, Networking). Personal Interview: 25 Marks.",
        'preparation_resources': "• SBI SCO IT Officer Exam Preparation: https://www.youtube.com/results?search_query=SBI+SCO+IT+Officer+preparation+lectures\n• BankPedia IT Officer Professional Knowledge: https://www.youtube.com/results?search_query=Bank+IT+Officer+professional+knowledge+lectures",
        'application_start_date': "September 2026",
        'application_last_date': "October 2026",
        'exam_date': "December 2026",
        'exam_timings': "Single Shift: 10:00 AM – 12:30 PM",
        'exam_date_info': "Annual SBI Specialist Drive"
    },
    # 11. IBPS PO
    {
        'exam_name': 'IBPS PO 2027 (Probationary Officer)',
        'category': 'govt',
        'domain': 'Banking & Public Sector Finance',
        'conducting_body': 'IBPS',
        'website_url': 'http://www.ibps.in/',
        'eligibility': "Qualification: Graduation degree in any discipline from a recognized University. Age Limit: 20–30 years (OBC +3 yrs, SC/ST +5 yrs). Nationality: Citizen of India. Percentage: Passing degree.",
        'syllabus_summary': "Prelims: 100 Qs (100 Marks, 60 mins: English 30, Quant 35, Reasoning 35). Mains: 155 Qs (200 Marks, 3 Hours: Reasoning & Computer, Data Analysis, General Banking, English) + English Essay & Letter (25 Marks). Interview: 100 Marks.",
        'preparation_resources': "• Adda247 IBPS PO Complete Course: https://www.youtube.com/results?search_query=Adda247+IBPS+PO+complete+preparation+playlist\n• Testbook IBPS PO Maths & Reasoning: https://www.youtube.com/results?search_query=Testbook+IBPS+PO+free+preparation+classes",
        'application_start_date': "August 2026",
        'application_last_date': "August 2026",
        'exam_date': "October 2026 (Prelims) / November 2026 (Mains)",
        'exam_timings': "Shift 1: 09:00 AM – 10:00 AM | Shift 2: 11:30 AM – 12:30 PM | Shift 3: 02:00 PM – 03:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 12. IBPS AFO
    {
        'exam_name': 'IBPS AFO 2027 (Agricultural Field Officer)',
        'category': 'govt',
        'domain': 'Agricultural Banking & Credit',
        'conducting_body': 'IBPS',
        'website_url': 'http://www.ibps.in/',
        'eligibility': "Qualification: 4-Year B.Sc degree in Agriculture, Horticulture, Forestry, Animal Husbandry, Veterinary Science, Agricultural Engineering, Food Science. Age Limit: 20–30 years. Nationality: Indian.",
        'syllabus_summary': "Prelims: 150 Qs (125 Marks, 120 mins: English 50, Reasoning 50, Quant 50). Mains: Professional Knowledge Test (60 Qs, 60 Marks, 45 Mins in Agricultural Sciences). Personal Interview: 100 Marks.",
        'preparation_resources': "• Agri Coaching India AFO Playlists: https://www.youtube.com/results?search_query=IBPS+AFO+Agriculture+Field+Officer+lectures\n• Agramer AFO Agriculture Science Prep: https://www.youtube.com/results?search_query=IBPS+AFO+Agriculture+preparation+classes",
        'application_start_date': "November 2026",
        'application_last_date': "December 2026",
        'exam_date': "December 2026 (Prelims) / January 2027 (Mains)",
        'exam_timings': "Shift 1: 09:00 AM – 11:00 AM | Shift 2: 01:00 PM – 03:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 13. RBI Grade B
    {
        'exam_name': 'RBI Grade B Officer Exam',
        'category': 'govt',
        'domain': 'Central Banking & Economics',
        'conducting_body': 'Reserve Bank of India',
        'website_url': 'https://opportunities.rbi.org.in/scripts/vacancies.aspx',
        'eligibility': "Qualification: Graduation in any discipline with min 60% marks (50% for SC/ST/PwBD) OR Post Graduation with min 55% marks. Age Limit: 21–30 years (34 for Ph.D. holders). Nationality: Indian citizen.",
        'syllabus_summary': "Phase I (200 Marks, 120 mins: General Awareness 80, Quant 30, Reasoning 60, English 30). Phase II (300 Marks: Paper 1 Economic & Social Issues, Paper 2 Descriptive English, Paper 3 Finance & Management). Interview: 75 Marks.",
        'preparation_resources': "• Anuj Jindal RBI Grade B Complete Playlist: https://www.youtube.com/results?search_query=Anuj+Jindal+RBI+Grade+B+preparation+playlist\n• EduTap RBI Grade B ESI & FM Lectures: https://www.youtube.com/results?search_query=EduTap+RBI+Grade+B+free+lectures",
        'application_start_date': "July 2026",
        'application_last_date': "August 2026",
        'exam_date': "September 2026 (Phase 1) / October 2026 (Phase 2)",
        'exam_timings': "Shift 1: 09:30 AM – 11:30 AM | Shift 2: 02:00 PM – 04:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 14. NABARD Grade A
    {
        'exam_name': 'NABARD Grade A Officer Exam',
        'category': 'govt',
        'domain': 'Rural Development & Agriculture Credit',
        'conducting_body': 'NABARD',
        'website_url': 'https://www.nabard.org/careers-notices.aspx',
        'eligibility': "Qualification: Bachelor's Degree in any subject with min 60% marks (55% SC/ST/PWBD) OR Post Graduation with min 55% marks. Age Limit: 21–30 years. Nationality: Citizen of India.",
        'syllabus_summary': "Phase I (200 Qs, 120 mins: Reasoning, English, Computer, Quant, Decision Making, General Awareness, Agriculture & Rural Development, Economic & Social Issues). Phase II (Descriptive English + ESI & ARD). Interview: 50 Marks.",
        'preparation_resources': "• EduTap NABARD Grade A Preparation: https://www.youtube.com/results?search_query=EduTap+NABARD+Grade+A+free+lectures\n• Anuj Jindal NABARD ARD & ESI Playlists: https://www.youtube.com/results?search_query=Anuj+Jindal+NABARD+Grade+A+preparation",
        'application_start_date': "July 2026",
        'application_last_date': "August 2026",
        'exam_date': "September 2026 (Phase 1) / October 2026 (Phase 2)",
        'exam_timings': "Forenoon Shift: 09:00 AM – 11:00 AM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 15. SEBI Grade A
    {
        'exam_name': 'SEBI Grade A Officer Exam (General / Finance / Legal)',
        'category': 'govt',
        'domain': 'Capital Markets & Legal Governance',
        'conducting_body': 'SEBI',
        'website_url': 'https://www.sebi.gov.in/',
        'eligibility': "Qualification: Master's Degree in any discipline OR Bachelor's Degree in Law / Engineering OR CA / CFA / CS / Cost Accountant. Age Limit: Maximum 30 years. Nationality: Indian citizen.",
        'syllabus_summary': "Phase 1: Paper 1 (GS, Aptitude - 100M) + Paper 2 (Commerce, Accountancy, Management, Finance, Costing, Companies Act, Economics - 100M). Phase 2: Paper 1 Descriptive English + Paper 2 Core Stream. Interview: 15% weightage.",
        'preparation_resources': "• IXAMBEE SEBI Grade A Free Preparation: https://www.youtube.com/results?search_query=ixamBee+SEBI+Grade+A+preparation+videos\n• EduTap SEBI Grade A Commerce & Finance: https://www.youtube.com/results?search_query=EduTap+SEBI+Grade+A+lectures",
        'application_start_date': "March 2026",
        'application_last_date': "April 2026",
        'exam_date': "July 2026 (Phase 1) / August 2026 (Phase 2)",
        'exam_timings': "Paper 1: 09:30 AM – 10:30 AM | Paper 2: 11:30 AM – 12:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 16. NEET-PG
    {
        'exam_name': 'NEET-PG 2027 (Postgraduate Medical Entrance)',
        'category': 'govt',
        'domain': 'Medical & Clinical Medicine',
        'conducting_body': 'NBE / NMC',
        'website_url': 'https://natboard.edu.in/',
        'eligibility': "Qualification: MBBS degree or Provisional Pass Certificate recognized under NMC Act 2019 + 1-year compulsory rotatory internship completion. NMC Registration: Permanent or Provisional registration mandatory.",
        'syllabus_summary': "Duration: 3 Hours 30 Minutes (CBT). Total Questions: 200 MCQs (800 Total Marks). Marking: +4 for correct, -1 for wrong response. Coverage: Pre-Clinical (Anatomy, Physiology, Biochem), Para-Clinical (Patho, Pharm, Micro, FMT, PSM), Clinical (Medicine, Surgery, OBG, Pediatrics).",
        'preparation_resources': "• Marrow / PrepLadder NEET PG High Yield Lectures: https://www.youtube.com/results?search_query=NEET+PG+preparation+high+yield+lectures\n• Dr. Bhanu Prakash Medical Prep: https://www.youtube.com/results?search_query=Dr+Bhanu+Prakash+NEET+PG+lectures",
        'application_start_date': "April 2026",
        'application_last_date': "May 2026",
        'exam_date': "July 2026",
        'exam_timings': "Single Shift: 09:00 AM – 12:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 17. NEET-MDS
    {
        'exam_name': 'NEET-MDS 2027 (Dental Surgery)',
        'category': 'govt',
        'domain': 'Dental & Surgery',
        'conducting_body': 'NBE / DCI',
        'website_url': 'https://natboard.edu.in/',
        'eligibility': "Qualification: Bachelor of Dental Surgery (BDS) from recognized institute + completion of 12-month compulsory rotatory internship. DCI Registration: Permanent or Provisional DCI registration required.",
        'syllabus_summary': "Duration: 3 Hours (CBT). Total Questions: 240 MCQs (960 Marks). Marking: +4 correct, -1 wrong. Part A: 100 Qs (Basic Medical & Dental Sciences). Part B: 140 Qs (Clinical Dental Subjects & Oral Surgery).",
        'preparation_resources': "• Dental Pulse NEET MDS Prep Lectures: https://www.youtube.com/results?search_query=NEET+MDS+preparation+videos+playlist\n• Dental Academy NEET MDS MCQs: https://www.youtube.com/results?search_query=Dental+Academy+NEET+MDS+lectures",
        'application_start_date': "January 2026",
        'application_last_date': "February 2026",
        'exam_date': "March 2026",
        'exam_timings': "Single Shift: 09:00 AM – 12:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 18. INI-CET
    {
        'exam_name': 'INI-CET 2027 (Medical & Dental)',
        'category': 'govt',
        'domain': 'AIIMS Clinical Medicine',
        'conducting_body': 'AIIMS New Delhi',
        'website_url': 'https://www.aiimsexams.ac.in/inicet',
        'eligibility': "Qualification: MBBS / BDS degree from institution recognized by NMC/DCI with min 55% aggregate marks (50% for SC/ST). Internship: 12 months internship completion mandatory prior to cutoff.",
        'syllabus_summary': "Duration: 3 Hours (CBT). Questions: 200 Objective MCQs (Single Choice & Multiple True-False type). Negative Marking: 1/3rd mark deducted per wrong answer. High-yield medical, surgical, and diagnostic subjects.",
        'preparation_resources': "• AIIMS INI-CET Top Ranker Lectures: https://www.youtube.com/results?search_query=INI+CET+preparation+AIIMS+lectures\n• Cerebellum Academy INI-CET Rapid Revision: https://www.youtube.com/results?search_query=Cerebellum+Academy+INI+CET+playlist",
        'application_start_date': "September 2026",
        'application_last_date': "October 2026",
        'exam_date': "November 2026 (January Session) / May 2027 (July Session)",
        'exam_timings': "Single Shift: 09:00 AM – 12:00 PM",
        'exam_date_info': "Biannual Exam Cycle"
    },
    # 19. INI-SS
    {
        'exam_name': 'INI-SS 2027 (Super Speciality)',
        'category': 'govt',
        'domain': 'Clinical Super Speciality',
        'conducting_body': 'AIIMS New Delhi',
        'website_url': 'https://www.aiimsexams.ac.in/iniss',
        'eligibility': "Qualification: MD/MS/DNB/MDS degree in concerned discipline from NMC/DCI recognized university. Age Limit: 35 years (Relaxable by 5 yrs for SC/ST, 3 yrs for OBC).",
        'syllabus_summary': "Stage 1: 80 Objective Questions (90 Mins). 30 Qs from General Component + 50 Qs from Speciality. Stage 2: Departmental Clinical & Practical Assessment (20 Marks) for AIIMS candidate pool.",
        'preparation_resources': "• INI SS DM MCh Entrance Preparation: https://www.youtube.com/results?search_query=INI+SS+super+speciality+exam+preparation\n• DocTutorials INI-SS High Yield Prep: https://www.youtube.com/results?search_query=DocTutorials+INI+SS+preparation",
        'application_start_date': "March 2026",
        'application_last_date': "April 2026",
        'exam_date': "May 2026",
        'exam_timings': "Single Shift: 09:00 AM – 10:30 AM",
        'exam_date_info': "Biannual Exam Cycle"
    },
    # 20. UPSC CMS
    {
        'exam_name': 'UPSC Combined Medical Services (CMS) 2027',
        'category': 'govt',
        'domain': 'Central Govt Medical Services',
        'conducting_body': 'UPSC',
        'website_url': 'https://upsc.gov.in/examinations/Combined%20Medical%20Services%20Examination',
        'eligibility': "Qualification: Passed final MBBS examination (both written & practical). Age Limit: Maximum 32 years as of 1st August. Relaxation: 3 yrs OBC, 5 yrs SC/ST. Nationality: Citizen of India.",
        'syllabus_summary': "Part I Computer Based Written Test: 2 Papers (250 Marks each, 2 Hours each). Paper I: General Medicine (96 Qs) & Pediatrics (24 Qs). Paper II: Surgery (40 Qs), Gynaecology & Obstetrics (40 Qs), PSM (40 Qs). Part II: Personality Test (100 Marks).",
        'preparation_resources': "• UPSC CMS Preparation Guide & PYQs: https://www.youtube.com/results?search_query=UPSC+CMS+exam+preparation+lectures\n• Medical PG Prep UPSC CMS Guidance: https://www.youtube.com/results?search_query=UPSC+Combined+Medical+Services+preparation",
        'application_start_date': "April 2026",
        'application_last_date': "May 2026",
        'exam_date': "July 2026",
        'exam_timings': "Paper I: 09:30 AM – 11:30 AM | Paper II: 02:00 PM – 04:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 21. FMGE
    {
        'exam_name': 'FMGE 2027 (Foreign Medical Graduate Exam)',
        'category': 'govt',
        'domain': 'Medical Licensing',
        'conducting_body': 'NBE',
        'website_url': 'https://natboard.edu.in/',
        'eligibility': "Qualification: Primary medical qualification (MBBS equivalent) awarded by foreign medical university registered with Indian Embassy + NMC Eligibility Certificate. Must be Indian citizen or OCI cardholder.",
        'syllabus_summary': "Mode: CBT. Total Questions: 300 MCQs (2 Papers of 150 Qs each, 150 Minutes per paper). Qualifying Criterion: Minimum 150 out of 300 Marks (50%). No negative marking. Clinical & Para-clinical medical sciences.",
        'preparation_resources': "• FMGE High Yield Rapid Revision: https://www.youtube.com/results?search_query=FMGE+rapid+revision+lectures+playlist\n• PrepLadder FMGE Solution Series: https://www.youtube.com/results?search_query=PrepLadder+FMGE+free+revision+lectures",
        'application_start_date': "October 2026",
        'application_last_date': "November 2026",
        'exam_date': "December 2026 (December Session) / June 2027 (June Session)",
        'exam_timings': "Part A: 09:00 AM – 11:30 AM | Part B: 02:00 PM – 04:30 PM",
        'exam_date_info': "Biannual Exam Cycle"
    },
    # 22. GPAT
    {
        'exam_name': 'GPAT 2027 (Graduate Pharmacy Aptitude Test)',
        'category': 'govt',
        'domain': 'Pharmacy & Clinical Pharmacology',
        'conducting_body': 'NTA',
        'website_url': 'https://gpat.nta.nic.in/',
        'eligibility': "Qualification: Bachelor's degree in Pharmacy (B.Pharm 4 years) or final year B.Pharm students from recognized University/AICTE approved institute. Age Limit: No age restriction.",
        'syllabus_summary': "Duration: 3 Hours (CBT). Total Questions: 125 MCQs (500 Marks). Marking: +4 correct, -1 negative. Pharmaceutics (38 Qs), Pharmaceutical Chemistry (38 Qs), Pharmacology (28 Qs), Pharmacognosy (11 Qs), Allied (10 Qs).",
        'preparation_resources': "• GPAT Discussion Center (GDC) Classes: https://www.youtube.com/results?search_query=GPAT+Discussion+Center+free+lectures\n• Pharma Prep GPAT Model Papers: https://www.youtube.com/results?search_query=GPAT+exam+preparation+free+lectures",
        'application_start_date': "April 2026",
        'application_last_date': "May 2026",
        'exam_date': "June 2026",
        'exam_timings': "Single Shift: 03:00 PM – 06:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 23. CLAT-PG
    {
        'exam_name': 'CLAT-PG 2027 (Common Law Admission Test for LLM)',
        'category': 'govt',
        'domain': 'Legal Jurisprudence & Corporate Law',
        'conducting_body': 'Consortium of NLUs',
        'website_url': 'https://consortiumofnlus.ac.in/',
        'eligibility': "Qualification: LL.B. degree or equivalent examination from a recognized University with min 50% aggregate marks (45% for SC/ST). Age Limit: No upper age limit. Candidates in final LL.B year eligible.",
        'syllabus_summary': "Duration: 120 Minutes (Offline OMR). Questions: 120 Objective MCQs based on extract passages (120 Marks). Negative Marking: 0.25 Mark per wrong answer. Constitutional Law, Jurisprudence, Admin Law, Contracts, Torts, Criminal Law, International Law, IPR.",
        'preparation_resources': "• LegalEdge CLAT PG LLM Preparation: https://www.youtube.com/results?search_query=LegalEdge+CLAT+PG+preparation+lectures\n• Lawctopus CLAT PG Strategy Series: https://www.youtube.com/results?search_query=CLAT+PG+LLM+preparation+playlist",
        'application_start_date': "July 2026",
        'application_last_date': "November 2026",
        'exam_date': "December 2026",
        'exam_timings': "Single Shift: 02:00 PM – 04:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 24. AIBE
    {
        'exam_name': 'AIBE 2027 (All India Bar Examination)',
        'category': 'govt',
        'domain': 'Legal Practice & Bar Advocacy',
        'conducting_body': 'Bar Council of India',
        'website_url': 'https://allindiabarexamination.com/',
        'eligibility': "Qualification: 3-year or 5-year LL.B degree from a BCI recognized Law School + Active enrolment as an Advocate with a State Bar Council under Advocates Act 1961. No age limit.",
        'syllabus_summary': "Mode: Offline OMR (Bare Acts allowed without notes). Questions: 100 MCQs (100 Marks, 3.5 Hours duration). Passing Criterion: 45% for General/OBC, 40% for SC/ST. Constitutional Law, CPC, CrPC, IPC, Evidence Act, Family Law, Professional Ethics.",
        'preparation_resources': "• AIBE Exam Bare Act & Preparation Lectures: https://www.youtube.com/results?search_query=AIBE+All+India+Bar+Exam+preparation\n• Unacademy Law AIBE Revision Series: https://www.youtube.com/results?search_query=Unacademy+AIBE+preparation+playlist",
        'application_start_date': "August 2026",
        'application_last_date': "September 2026",
        'exam_date': "November 2026",
        'exam_timings': "Single Shift: 10:00 AM – 01:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 25. Judicial Services Exam
    {
        'exam_name': 'Judicial Services Exam 2027 (PCS-J)',
        'category': 'govt',
        'domain': 'Judicial Services & Court Advocacy',
        'conducting_body': 'State High Courts / Public Service Commission',
        'website_url': 'https://upsc.gov.in/examinations/notifications',
        'eligibility': "Qualification: LL.B. degree from a recognized University in India + Enrolled/Eligible to enroll as an Advocate under Advocates Act 1961. Age Limit: 21–35 years (state specific relaxations for SC/ST/OBC).",
        'syllabus_summary': "Stage I Prelims: Objective MCQs (General Knowledge, English & Central/State Laws). Stage II Mains: 4-5 Written Descriptive Papers (Civil Law I, Civil Law II, Criminal Law, Local State Laws, Language & Judgment Writing). Stage III Viva-Voce.",
        'preparation_resources': "• Judiciary Gold PCS-J Free Preparation: https://www.youtube.com/results?search_query=Judiciary+Gold+PCS+J+preparation+lectures\n• Physics Wallah Judiciary Prep: https://www.youtube.com/results?search_query=PW+Judiciary+PCS+J+free+lectures",
        'application_start_date': "Varies by State (Jan-Dec)",
        'application_last_date': "Varies by State",
        'exam_date': "State Specific Cycles 2026-2027",
        'exam_timings': "Morning Shift: 09:30 AM – 12:30 PM | Afternoon Shift: 02:00 PM – 05:00 PM",
        'exam_date_info': "State Civil Judge Drive"
    },
    # 26. ICAR AIEEA PG
    {
        'exam_name': 'ICAR AIEEA PG 2027',
        'category': 'govt',
        'domain': 'Agriculture & Soil Sciences',
        'conducting_body': 'ICAR / NTA',
        'website_url': 'https://icar.org.in/',
        'eligibility': "Qualification: 4-year B.Sc degree in Agriculture/Horticulture/Forestry/Community Science/Agril Engineering with min 6.0/10 CGPA (5.0 for SC/ST/PwBD). Age Limit: Minimum 19 years old.",
        'syllabus_summary': "Mode: CBT (120 Minutes). Questions: 120 MCQs (480 Marks). Marking: +4 correct, -1 wrong. Plant Sciences, Agronomy, Soil Science, Horticulture, Agricultural Economics, Entomology, Agricultural Extension.",
        'preparation_resources': "• ICAR AIEEA PG Agriculture Preparation: https://www.youtube.com/results?search_query=ICAR+AIEEA+PG+Agriculture+prep+playlist\n• Agri Toppers Academy ICAR Prep: https://www.youtube.com/results?search_query=Agri+Toppers+Academy+ICAR+AIEEA",
        'application_start_date': "April 2026",
        'application_last_date': "May 2026",
        'exam_date': "June 2026",
        'exam_timings': "Single Shift: 10:00 AM – 12:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 27. CSIR NET
    {
        'exam_name': 'CSIR NET Chemical & Life Sciences 2027',
        'category': 'govt',
        'domain': 'Science & Biotechnology Research',
        'conducting_body': 'CSIR / NTA',
        'website_url': 'https://csirnet.nta.ac.in/',
        'eligibility': "Qualification: M.Sc or equivalent degree / BS-MS / B.Tech / MBBS / B.Pharm with min 55% marks (50% SC/ST/PwD). Age Limit: Max 28 years for JRF (No upper age limit for Assistant Professorship).",
        'syllabus_summary': "Duration: 3 Hours (CBT). Total Marks: 200. Part A: 20 Qs General Science & Reasoning (Attempt 15, 30 Marks). Part B: 50 Qs Subject Core MCQs (Attempt 35, 70 Marks). Part C: 75 Qs Analytical Subject MCQs (Attempt 25, 100 Marks).",
        'preparation_resources': "• IFAS CSIR NET Life & Chemical Sciences: https://www.youtube.com/results?search_query=IFAS+CSIR+NET+Life+Sciences+lectures\n• Bansal Biology CSIR NET Playlists: https://www.youtube.com/results?search_query=Bansal+Biology+CSIR+NET+preparation",
        'application_start_date': "May 2026",
        'application_last_date': "June 2026",
        'exam_date': "July 2026 (June Cycle) / Dec 2026 (Dec Cycle)",
        'exam_timings': "Shift 1: 09:00 AM – 12:00 PM | Shift 2: 03:00 PM – 06:00 PM",
        'exam_date_info': "Biannual Exam Cycle"
    },
    # 28. UGC NET Mass Comm
    {
        'exam_name': 'UGC NET Mass Communication & Journalism 2027',
        'category': 'govt',
        'domain': 'Arts & Media Journalism',
        'conducting_body': 'UGC / NTA',
        'website_url': 'https://ugcnet.nta.ac.in/',
        'eligibility': "Qualification: Master's degree in Mass Communication, Journalism, Electronic Media, or Communication Studies with min 55% marks (50% SC/ST/OBC-NCL). Age: No limit for Asst Professor, 30 yrs for JRF.",
        'syllabus_summary': "Duration: 3 Hours (CBT). Paper I: 50 Qs (100 Marks: Teaching & Research Aptitude, Reasoning, ICT). Paper II: 100 Qs (200 Marks: Communication Theory, Print/Broadcast Media, Digital Media, Media Law, Advertising & PR). No negative marking.",
        'preparation_resources': "• UGC NET Mass Communication Paper 2 Prep: https://www.youtube.com/results?search_query=UGC+NET+Mass+Communication+and+Journalism+preparation\n• Mass Comm Junction Free Series: https://www.youtube.com/results?search_query=Mass+Comm+Junction+UGC+NET",
        'application_start_date': "April 2026",
        'application_last_date': "May 2026",
        'exam_date': "June 2026",
        'exam_timings': "Shift 1: 09:00 AM – 12:00 PM | Shift 2: 03:00 PM – 06:00 PM",
        'exam_date_info': "Biannual Exam Cycle"
    },
    # 29. NIMCET
    {
        'exam_name': 'NIMCET 2027 (MCA Entrance Exam)',
        'category': 'govt',
        'domain': 'Computer Applications',
        'conducting_body': 'NITs Consortium',
        'website_url': 'https://nimcet.admissions.nic.in/',
        'eligibility': "Qualification: B.Sc / B.Sc (Hons) / BCA / BIT / B.E / B.Tech with min 60% marks or 6.5/10 CGPA (55% or 6.0 CGPA for SC/ST). Mathematics/Statistics in 10+2 or Graduation mandatory. Age limit: No limit.",
        'syllabus_summary': "Duration: 2 Hours (CBT). Questions: 120 Qs (1000 Total Weighted Marks). Mathematics (50 Qs, 600 Marks), Analytical Ability & Reasoning (40 Qs, 240 Marks), Computer Awareness (20 Qs, 120 Marks), English (10 Qs, 40 Marks).",
        'preparation_resources': "• INPS Classes NIMCET Preparation: https://www.youtube.com/results?search_query=NIMCET+preparation+INPS+classes+maths+computer\n• ACET NIMCET Maths & Computer Playlists: https://www.youtube.com/results?search_query=ACET+NIMCET+maths+lectures",
        'application_start_date': "March 2026",
        'application_last_date': "April 2026",
        'exam_date': "June 2026",
        'exam_timings': "Single Shift: 02:00 PM – 04:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 30. C-DAC C-CAT
    {
        'exam_name': 'C-DAC C-CAT 2027 (Computer Applications)',
        'category': 'govt',
        'domain': 'Advanced Computing & Software',
        'conducting_body': 'C-DAC',
        'website_url': 'https://www.cdac.in/index.aspx?id=edu_act_ccat',
        'eligibility': "Qualification: Graduate in Engineering (CS/IT/EC/EE) or MCA / M.Sc CS/IT with minimum 50% marks in qualifying degree. Age Limit: No age restriction.",
        'syllabus_summary': "Format: 3 Sections (50 Qs each, 1 Hour per section, total 150 Qs, 450 Marks). Section A: English, Quant, Reasoning. Section B: C Programming, Data Structures, OOPs in C++, OS, Networking. Section C: Data Analytics, Microprocessors.",
        'preparation_resources': "• C-DAC C-CAT Free Preparation Lectures: https://www.youtube.com/results?search_query=CDAC+CCAT+exam+preparation+lectures\n• CDAC Prep Corner Playlists: https://www.youtube.com/results?search_query=CDAC+CCAT+C+programming+data+structures",
        'application_start_date': "December 2026",
        'application_last_date': "January 2027",
        'exam_date': "January 2027",
        'exam_timings': "Section A+B: 10:00 AM – 12:00 PM | Section C: 02:00 PM – 03:00 PM",
        'exam_date_info': "Biannual Cycle (Jan & July)"
    },
    # 31. BARC OCES
    {
        'exam_name': 'BARC OCES/DGFS 2027 (Scientific Officer Recruitment)',
        'category': 'govt',
        'domain': 'Nuclear Science & Engineering',
        'conducting_body': 'BARC / DAE',
        'website_url': 'https://barcoces.isro.gov.in/',
        'eligibility': "Qualification: B.E/B.Tech/B.Sc (Engg) in CS, ECE, EE, Mechanical, Chemical, Metallurgy, Civil with min 60% aggregate. Shortlisting via Online Exam or GATE score. Max age: 26 years.",
        'syllabus_summary': "Format: 100 Objective MCQs (300 Marks, 120 Mins, +3 correct, -1 wrong). Core Discipline Engineering & Applied Physics. Followed by intensive Personal Interview.",
        'preparation_resources': "• BARC OCES Scientific Officer Prep Series: https://www.youtube.com/results?search_query=BARC+OCES+Scientific+Officer+preparation+lectures\n• Gate Smashers BARC Exam PYQs: https://www.youtube.com/results?search_query=Gate+Smashers+BARC+OCES+exam+preparation",
        'application_start_date': "January 2027",
        'application_last_date': "February 2027",
        'exam_date': "March 2027",
        'exam_timings': "Single Shift: 10:00 AM – 12:00 PM",
        'exam_date_info': "Annual BARC Recruitment"
    },
    # 32. ECIL Technical Officer
    {
        'exam_name': 'ECIL Technical Officer Recruitment',
        'category': 'govt',
        'domain': 'Embedded Systems & Defense Electronics',
        'conducting_body': 'ECIL Govt of India',
        'website_url': 'https://www.ecil.co.in/jobs.html',
        'eligibility': "Qualification: B.E/B.Tech in ECE, EEE, CSE, IT, Mechanical with min 65% marks (55% for SC/ST). Age limit: 30 years.",
        'syllabus_summary': "Format: 100 MCQs (100 Marks, 90 Mins). 70% Core Technical + 30% Aptitude, Reasoning, and General Awareness.",
        'preparation_resources': "• ECIL Technical Officer Exam Guide: https://www.youtube.com/results?search_query=ECIL+Technical+Officer+exam+preparation+classes",
        'application_start_date': "May 2026",
        'application_last_date': "June 2026",
        'exam_date': "July 2026",
        'exam_timings': "Single Shift: 10:00 AM – 11:30 AM",
        'exam_date_info': "Annual ECIL Drive"
    },
    # 33. BEL Probationary Engineer
    {
        'exam_name': 'BEL Probationary Engineer Exam',
        'category': 'govt',
        'domain': 'Radar, Telecom & Aerospace Electronics',
        'conducting_body': 'Bharat Electronics Limited (BEL)',
        'website_url': 'https://jobapply.in/bel2026/',
        'eligibility': "Qualification: B.E/B.Tech/B.Sc (Engg) 4-year degree in ECE, CSE, Mechanical, Electrical, Civil with First Class (Pass Class for SC/ST/PwBD). Max age: 28 years.",
        'syllabus_summary': "Written Test (85% weightage): Part 1 Technical Core (120 Qs), Part 2 General Aptitude (30 Qs). Duration: 150 Mins. Personal Interview (15% weightage).",
        'preparation_resources': "• BEL Probationary Engineer Preparation: https://www.youtube.com/results?search_query=BEL+Probationary+Engineer+exam+preparation+lectures",
        'application_start_date': "March 2026",
        'application_last_date': "April 2026",
        'exam_date': "May 2026",
        'exam_timings': "Single Shift: 10:00 AM – 12:30 PM",
        'exam_date_info': "Annual BEL Recruitment"
    },
    # 34. ONGC Graduate Trainee
    {
        'exam_name': 'ONGC Graduate Trainee Recruitment',
        'category': 'govt',
        'domain': 'Petroleum, Mechanical & Software Systems',
        'conducting_body': 'ONGC India',
        'website_url': 'https://ongcindia.com/web/eng/careers',
        'eligibility': "Qualification: Graduate degree in Engineering (B.E/B.Tech) or Post Graduate in Geophysics/Geology/CS/IT with min 60% aggregate. Shortlisting via valid GATE score. Max age: 30 years.",
        'syllabus_summary': "GATE Score Weightage (60 Marks) + Qualification Weightage (25 Marks) + Personal Interview (15 Marks). Total: 100 Marks.",
        'preparation_resources': "• ONGC Graduate Trainee Interview Prep: https://www.youtube.com/results?search_query=ONGC+Graduate+Trainee+GATE+interview+preparation",
        'application_start_date': "May 2026",
        'application_last_date': "June 2026",
        'exam_date': "July 2026",
        'exam_timings': "Interview Shift Slots",
        'exam_date_info': "Annual GATE ONGC Drive"
    },
    # 35. GAIL Executive Trainee
    {
        'exam_name': 'GAIL Executive Trainee Exam',
        'category': 'govt',
        'domain': 'Natural Gas & Energy Systems',
        'conducting_body': 'GAIL (India) Limited',
        'website_url': 'https://gailonline.com/CRApplyinggail.html',
        'eligibility': "Qualification: B.E/B.Tech in Chemical, Petrochemical, Mechanical, Electrical, Instrumentation, Civil, CS/IT with min 65% aggregate (60% for SC/ST). Shortlisting via GATE score. Max age: 28 years.",
        'syllabus_summary': "GATE score weightage (85%) + Group Discussion / Behavioral Test & Personal Interview (15%).",
        'preparation_resources': "• GAIL Executive Trainee Prep Guide: https://www.youtube.com/results?search_query=GAIL+Executive+Trainee+preparation+guidance",
        'application_start_date': "February 2026",
        'application_last_date': "March 2026",
        'exam_date': "April 2026",
        'exam_timings': "Interview Shift Slots",
        'exam_date_info': "Annual GAIL Recruitment"
    },
    # 36. SSC JE
    {
        'exam_name': 'SSC JE (Junior Engineer - Civil, Electrical, Mechanical)',
        'category': 'govt',
        'domain': 'Civil, Electrical & Mechanical Infrastructure',
        'conducting_body': 'SSC Govt of India',
        'website_url': 'https://ssc.gov.in/candidate-portal/examinations/je',
        'eligibility': "Qualification: Diploma or B.E/B.Tech degree in Civil, Electrical, or Mechanical Engineering from recognized institute. Age limit: 18–32 years.",
        'syllabus_summary': "Paper I (CBT - 200 Marks, 120 mins: General Intelligence 50, General Awareness 50, General Engineering 100). Paper II (CBT - 300 Marks, 120 mins: Core Technical Engineering MCQs with calculator).",
        'preparation_resources': "• SSC JE Electrical & Civil Classes: https://www.youtube.com/results?search_query=SSC+JE+Civil+Electrical+Mechanical+preparation+classes\n• Engineers Academy SSC JE PYQs: https://www.youtube.com/results?search_query=Engineers+Academy+SSC+JE+lectures",
        'application_start_date': "March 2026",
        'application_last_date': "April 2026",
        'exam_date': "June 2026 (Paper 1) / October 2026 (Paper 2)",
        'exam_timings': "Shift 1: 09:00 AM – 11:00 AM | Shift 2: 02:00 PM – 04:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 37. NIMHANS M.Phil / PG
    {
        'exam_name': 'NIMHANS M.Phil / PG Entrance Exam',
        'category': 'govt',
        'domain': 'Neuroscience & Clinical Psychology',
        'conducting_body': 'NIMHANS Bengaluru',
        'website_url': 'https://nimhans.ac.in/academic-incharge/',
        'eligibility': "Qualification: MA / M.Sc in Psychology / Clinical Psychology or M.Sc Neuroscience / MBBS with min 55% aggregate marks.",
        'syllabus_summary': "Online Entrance Test: 100 MCQs (100 Marks, 90 Mins, 0.25 negative marking). Clinical Psychology, Neuroanatomy, Neurophysiology, Psychopathology, Research Methodology.",
        'preparation_resources': "• NIMHANS Entrance Exam Preparation: https://www.youtube.com/results?search_query=NIMHANS+entrance+exam+preparation+psychology+neuroscience",
        'application_start_date': "April 2026",
        'application_last_date': "May 2026",
        'exam_date': "June 2026",
        'exam_timings': "Single Shift: 10:00 AM – 11:30 AM",
        'exam_date_info': "Annual NIMHANS Drive"
    },
    # 38. TIFR GS-2027
    {
        'exam_name': 'TIFR Graduate Studies Entrance (GS-2027)',
        'category': 'govt',
        'domain': 'Pure Sciences & Mathematical Computing',
        'conducting_body': 'Tata Institute of Fundamental Research',
        'website_url': 'https://www.tifr.res.in/~academics/gs_advertisement.php',
        'eligibility': "Qualification: B.Sc / B.E / B.Tech / M.Sc in Physics, Chemistry, Biology, Mathematics, or CS/Systems Science with min 60% aggregate.",
        'syllabus_summary': "Written Test (180 Mins): Multiple choice & numerical questions testing deep fundamental problem solving in target subject. Shortlisted candidates proceed to two rounds of interviews.",
        'preparation_resources': "• TIFR GS Entrance Preparation & PYQs: https://www.youtube.com/results?search_query=TIFR+GS+Physics+CS+Mathematics+preparation",
        'application_start_date': "October 2026",
        'application_last_date': "November 2026",
        'exam_date': "December 2026",
        'exam_timings': "Single Shift: 09:30 AM – 12:30 PM",
        'exam_date_info': "Annual TIFR GS Drive"
    },
    # 39. GATE Engineering Disciplines
    {
        'exam_name': 'GATE Core Engineering Papers (ME/EE/EC/CE)',
        'category': 'govt',
        'domain': 'Core Engineering & Applied Sciences',
        'conducting_body': 'IIT Madras / GATE Committee',
        'website_url': 'https://gate2027.iitm.ac.in/',
        'eligibility': "Qualification: Bachelor's degree in B.E/B.Tech (Civil/Mechanical/Electrical/ECE) or currently in 3rd year or higher. No age limit.",
        'syllabus_summary': "65 Qs (100 Marks, 3 Hours). General Aptitude (15 Marks) + Engineering Mathematics (13 Marks) + Core Discipline Subjects (72 Marks). MCQs, MSQs, NATs.",
        'preparation_resources': "• NPTEL Core Engineering GATE Series: https://www.youtube.com/results?search_query=NPTEL+GATE+Mechanical+Civil+Electrical+ECE\n• Unacademy GATE Engineering Lectures: https://www.youtube.com/results?search_query=Unacademy+GATE+Engineering+lectures",
        'application_start_date': "August 2026",
        'application_last_date': "October 2026",
        'exam_date': "February 2027",
        'exam_timings': "Forenoon: 09:30 AM – 12:30 PM | Afternoon: 02:30 PM – 05:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 40. UGC NET CS
    {
        'exam_name': 'NTA UGC NET Computer Science & Applications',
        'category': 'govt',
        'domain': 'Computer Science Research & Academia',
        'conducting_body': 'UGC / NTA',
        'website_url': 'https://ugcnet.nta.ac.in/',
        'eligibility': "Qualification: Master's degree in Computer Science, MCA, or M.Tech in CS/IT with min 55% marks (50% for SC/ST/OBC-NCL).",
        'syllabus_summary': "Paper I (50 Qs, 100 Marks: Teaching & Research Aptitude). Paper II (100 Qs, 200 Marks: Discrete Struct, OS, DBMS, Algorithms, Theory of Computation, Compilers, Networks, AI, Software Engg).",
        'preparation_resources': "• Gate Smashers UGC NET CS Complete Playlist: https://www.youtube.com/results?search_query=Gate+Smashers+UGC+NET+Computer+Science+playlist\n• Knowledge Gate UGC NET Computer Science: https://www.youtube.com/results?search_query=Knowledge+Gate+UGC+NET+Computer+Science",
        'application_start_date': "April 2026",
        'application_last_date': "May 2026",
        'exam_date': "June 2026",
        'exam_timings': "Shift 1: 09:00 AM – 12:00 PM | Shift 2: 03:00 PM – 06:00 PM",
        'exam_date_info': "Biannual Exam Cycle"
    },

    # =========================================================================
    # PRIVATE & TECH CERTIFICATION EXAMS (41 to 80)
    # =========================================================================
    # 41. AWS SAA-C03
    {
        'exam_name': 'AWS Certified Solutions Architect Associate (SAA-C03)',
        'category': 'private',
        'domain': 'Cloud Computing & Infrastructure',
        'conducting_body': 'Amazon Web Services',
        'website_url': 'https://aws.amazon.com/certification/certified-solutions-architect-associate/',
        'eligibility': "Qualification: Open to students, cloud architects, developers, and IT professionals. Prerequisites: None. Hands-on experience with AWS Cloud services recommended.",
        'syllabus_summary': "Format: 65 Multiple Choice & Multiple Response Qs (130 Mins, Passing: 720/1000). Domain 1: Design Secure Architectures (30%), Domain 2: Design Resilient Architectures (26%), Domain 3: Design High-Performing Architectures (24%), Domain 4: Design Cost-Optimized Architectures (20%).",
        'preparation_resources': "• freeCodeCamp AWS SAA-C03 Complete Course: https://www.youtube.com/results?search_query=freeCodeCamp+AWS+Certified+Solutions+Architect+Associate+full+course\n• Stephane Maarek AWS SAA-C03 Study Guide: https://www.youtube.com/results?search_query=Stephane+Maarek+AWS+Solutions+Architect+Associate",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Online Proctored / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 42. GCP ACE
    {
        'exam_name': 'Google Associate Cloud Engineer (GCP Certification)',
        'category': 'private',
        'domain': 'Cloud Infrastructure',
        'conducting_body': 'Google Cloud',
        'website_url': 'https://cloud.google.com/learn/certification/cloud-engineer',
        'eligibility': "Qualification: Open to engineers, system administrators, and IT graduates. Recommended: 6+ months hands-on experience with Google Cloud Console & gcloud CLI.",
        'syllabus_summary': "Format: 50 Multiple Choice & Multiple Select Qs (120 Mins). Domains: Setting up cloud solution environment, Planning & configuring cloud solution, Deploying cloud applications, Ensuring successful operation, Configuring access & security.",
        'preparation_resources': "• freeCodeCamp Google Associate Cloud Engineer Course: https://www.youtube.com/results?search_query=freeCodeCamp+Google+Associate+Cloud+Engineer+full+course\n• Google Cloud Tech Official Tutorials: https://www.youtube.com/results?search_query=Google+Cloud+Tech+Associate+Cloud+Engineer+tutorials",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Kryterion)",
        'exam_timings': "Flexible Online Proctored / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 43. CKA
    {
        'exam_name': 'Certified Kubernetes Administrator (CKA)',
        'category': 'private',
        'domain': 'Cloud Native & DevOps',
        'conducting_body': 'Linux Foundation / CNCF',
        'website_url': 'https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/',
        'eligibility': "Qualification: Open to DevOps practitioners, systems administrators, and cloud developers. Recommended: Familiarity with Linux terminal and Docker container concepts.",
        'syllabus_summary': "Format: 100% Performance-based practical exam on live K8s command-line cluster (2 Hours, Passing: 66%). Domains: Storage (10%), Troubleshooting (30%), Workloads & Scheduling (15%), Cluster Architecture & Installation (25%), Services & Networking (20%).",
        'preparation_resources': "• KodeKloud CKA Free Tutorials & Tips: https://www.youtube.com/results?search_query=KodeKloud+CKA+Certified+Kubernetes+Administrator\n• TechWorld with Nana Kubernetes Course: https://www.youtube.com/results?search_query=TechWorld+with+Nana+Kubernetes+full+course",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (PSI Online)",
        'exam_timings': "24/7 Online Remote Proctored Exam",
        'exam_date_info': "Continuous Certification"
    },
    # 44. CCNA 200-301
    {
        'exam_name': 'Cisco Certified Network Associate (CCNA 200-301)',
        'category': 'private',
        'domain': 'Networking & Telecom',
        'conducting_body': 'Cisco Systems',
        'website_url': 'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html',
        'eligibility': "Qualification: Open to computer science students and network engineering aspirants. No formal prerequisites. Knowledge of IP addressing and subnetting recommended.",
        'syllabus_summary': "Format: 100–120 Questions (120 Mins). Domains: Network Fundamentals (20%), Network Access (20%), IP Connectivity (25%), IP Services (10%), Security Fundamentals (15%), Automation & Programmability (10%).",
        'preparation_resources': "• NetworkChuck CCNA Full Free Course: https://www.youtube.com/results?search_query=NetworkChuck+CCNA+full+course+playlist\n• Jeremy's IT Lab CCNA 200-301 Complete Course: https://www.youtube.com/results?search_query=Jeremys+IT+Lab+CCNA+200+301+complete+playlist",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Online / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 45. AZ-305
    {
        'exam_name': 'Microsoft Certified: Azure Solutions Architect Expert (AZ-305)',
        'category': 'private',
        'domain': 'Cloud Architecture',
        'conducting_body': 'Microsoft',
        'website_url': 'https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/',
        'eligibility': "Qualification: Prerequisite: Earn Azure Administrator Associate (AZ-104) certification. Advanced experience in Azure governance, compute, network, and storage architecture.",
        'syllabus_summary': "Format: 40–60 Questions including case studies (120 Mins). Design Identity, Governance, and Monitoring Solutions (25-30%), Design Data Storage Solutions (25-30%), Design Business Continuity Solutions (10-15%), Design Infrastructure Solutions (25-30%).",
        'preparation_resources': "• John Savill's Azure Master Class & AZ-305 Study Cram: https://www.youtube.com/results?search_query=John+Savill+AZ+305+Azure+Solutions+Architect+cram\n• freeCodeCamp Azure Architect Course: https://www.youtube.com/results?search_query=freeCodeCamp+Azure+Solutions+Architect+AZ+305",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Online / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 46. CISSP
    {
        'exam_name': 'Certified Information Systems Security Professional (CISSP)',
        'category': 'private',
        'domain': 'Cybersecurity Governance',
        'conducting_body': '(ISC)²',
        'website_url': 'https://www.isc2.org/certifications/cissp',
        'eligibility': "Qualification: Min 5 years cumulative paid work experience in 2 or more of the 8 CISSP domains (1 year waived for 4-year degree). Associate status available for students.",
        'syllabus_summary': "Format: CAT (Computer Adaptive Test): 100–150 Qs (3 Hours, Passing: 700/1000). 8 Security Domains: Security & Risk Management, Asset Security, Security Architecture, Communication & Network Security, IAM, Security Assessment, Security Operations, Software Dev Security.",
        'preparation_resources': "• Destination Certification CISSP Masterclass: https://www.youtube.com/results?search_query=Destination+Certification+CISSP+mindmap+playlist\n• Pete Zerger CISSP Exam Cram: https://www.youtube.com/results?search_query=Pete+Zerger+CISSP+exam+cram",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE PPC)",
        'exam_timings': "Flexible Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 47. Terraform Associate
    {
        'exam_name': 'HashiCorp Certified: Terraform Associate (003)',
        'category': 'private',
        'domain': 'Infrastructure as Code',
        'conducting_body': 'HashiCorp',
        'website_url': 'https://www.hashicorp.com/certification/terraform-associate',
        'eligibility': "Qualification: Open to cloud engineers, DevOps practitioners, and system administrators. Basic understanding of cloud architecture and Linux command line.",
        'syllabus_summary': "Format: 57 Questions (Multiple choice, multiple select, fill-in-the-blank, 60 Mins). IaC concepts, Terraform basics, Terraform CLI, Terraform modules, State management, Cloud/Enterprise capabilities.",
        'preparation_resources': "• freeCodeCamp Terraform Associate Course: https://www.youtube.com/results?search_query=freeCodeCamp+Terraform+Associate+003+full+course\n• Bryan Krausen Terraform Certification Guide: https://www.youtube.com/results?search_query=Bryan+Krausen+Terraform+Associate",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (PSI Online)",
        'exam_timings': "Flexible Online Remote Proctored Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 48. Wipro NLTH
    {
        'exam_name': 'Wipro NLTH (National Hiring Drive)',
        'category': 'private',
        'domain': 'Software Development',
        'conducting_body': 'Wipro',
        'website_url': 'https://careers.wipro.com/careers-home',
        'eligibility': "Qualification: B.E/B.Tech/M.E/M.Tech (All engineering streams) with min 60% or 6.0 CGPA in 10th, 12th, and Graduation. Max 3 years education gap allowed. Age limit: 25 years.",
        'syllabus_summary': "Format: Online Test (128 Mins). Aptitude Test: Quant, Logical Reasoning, Verbal Ability (48 Mins). Written Communication: Essay Writing (20 Mins). Online Coding Test: 2 Programs in C, C++, Java, or Python (60 Mins).",
        'preparation_resources': "• PrepInsta Wipro NLTH Coding & Aptitude: https://www.youtube.com/results?search_query=PrepInsta+Wipro+NLTH+preparation+playlist\n• Talent Battle Wipro NLTH Free Classes: https://www.youtube.com/results?search_query=Talent+Battle+Wipro+NLTH+lectures",
        'application_start_date': "September 2026",
        'application_last_date': "October 2026",
        'exam_date': "November 2026",
        'exam_timings': "Online Shift Slots: 10:00 AM / 02:00 PM",
        'exam_date_info': "Annual Campus Drive"
    },
    # 49. TCS NQT
    {
        'exam_name': 'TCS NQT (National Qualifier Test)',
        'category': 'private',
        'domain': 'Software Development & IT Services',
        'conducting_body': 'TCS iON',
        'website_url': 'https://learning.tcsionhub.in/test/nqt/',
        'eligibility': "Qualification: B.E/B.Tech/M.E/M.Tech/MCA/M.Sc (All streams). Minimum 60% or 6.0 CGPA in 10th, 12th, and Graduation. Max 2 years gap allowed.",
        'syllabus_summary': "Format: Foundation Section (75 Mins: Numerical, Verbal, Reasoning) + Advanced Section (35 Mins: Advanced Quant & Reasoning) + Hands-on Coding (45 Mins: 2 Programs in C/C++/Java/Python).",
        'preparation_resources': "• PrepInsta TCS NQT Preparation Series: https://www.youtube.com/results?search_query=PrepInsta+TCS+NQT+preparation+playlist\n• Knowledge Gate TCS NQT Coding & Aptitude: https://www.youtube.com/results?search_query=Knowledge+Gate+TCS+NQT+lectures",
        'application_start_date': "August 2026",
        'application_last_date': "September 2026",
        'exam_date': "October 2026",
        'exam_timings': "Shift 1: 09:00 AM – 12:00 PM | Shift 2: 02:00 PM – 05:00 PM",
        'exam_date_info': "Biannual Hiring Drive"
    },
    # 50. Infosys HackWithInfy
    {
        'exam_name': 'Infosys HackWithInfy & INFYTQ Certification',
        'category': 'private',
        'domain': 'Software Engineering & Data Structures',
        'conducting_body': 'Infosys',
        'website_url': 'https://infytq.onwingspan.com/',
        'eligibility': "Qualification: B.E/B.Tech/M.E/M.Tech/MCA/M.Sc students (Final year & Pre-final year). Open to all engineering branches. No percentage barrier.",
        'syllabus_summary': "Round 1: 3 Coding Questions on Data Structures, Algorithms, Dynamic Programming (180 Mins). Round 2: System Design & Technical Interview for Specialist Programmer / Digital Specialist Engineer roles.",
        'preparation_resources': "• Infytq & HackWithInfy Coding Preparation: https://www.youtube.com/results?search_query=Infytq+HackWithInfy+coding+preparation+playlist\n• Striver TakeUForward DSA Playlists: https://www.youtube.com/results?search_query=takeUforward+striver+sde+sheet",
        'application_start_date': "February 2026",
        'application_last_date': "March 2026",
        'exam_date': "April 2026",
        'exam_timings': "Single Slot: 10:00 AM – 01:00 PM",
        'exam_date_info': "Annual Hackathon & Certification"
    },
    # 51. Cognizant GenC Next
    {
        'exam_name': 'Cognizant GenC & GenC Next Hiring Drive',
        'category': 'private',
        'domain': 'Full Stack & Enterprise Software',
        'conducting_body': 'Cognizant (CTS)',
        'website_url': 'https://www.cognizant.com/in/en/careers',
        'eligibility': "Qualification: B.E/B.Tech/MCA/M.Sc (CS, IT, ECE, EE) with min 60% aggregate. No active backlogs at time of selection. Max 1 year gap.",
        'syllabus_summary': "GenC Assessment: Quant, Reasoning, Verbal & Communication (100 Mins). GenC Next Assessment: 2 Complex Algorithmic Programs (120 Mins) + Technical & HR Interview.",
        'preparation_resources': "• Cognizant GenC & GenC Next Prep: https://www.youtube.com/results?search_query=Cognizant+GenC+Next+coding+preparation\n• PrepInsta Cognizant Model Test: https://www.youtube.com/results?search_query=PrepInsta+Cognizant+GenC+preparation",
        'application_start_date': "August 2026",
        'application_last_date': "September 2026",
        'exam_date': "October 2026",
        'exam_timings': "Online Shift Slots: 10:00 AM / 02:00 PM",
        'exam_date_info': "Annual Campus Drive"
    },
    # 52. Accenture ASE Drive
    {
        'exam_name': 'Accenture National Hiring Drive (ASE / FSE)',
        'category': 'private',
        'domain': 'Cloud Applications & Consulting',
        'conducting_body': 'Accenture',
        'website_url': 'https://www.accenture.com/in-en/careers/local/technology-recruitment',
        'eligibility': "Qualification: B.E/B.Tech/M.E/M.Tech/MCA/M.Sc (All streams) with min 60% or 6.0 CGPA. Max 1 year education gap.",
        'syllabus_summary': "Stage 1: Cognitive Assessment (50 Qs) & Technical Assessment (40 Qs - Pseudocode, Security, Cloud) (90 Mins). Stage 2: Coding Assessment (2 Programs - 45 Mins). Stage 3: Communication Assessment (20 Mins).",
        'preparation_resources': "• Accenture Recruitment Test Preparation: https://www.youtube.com/results?search_query=Accenture+recruitment+exam+pseudocode+coding+prep\n• Talent Battle Accenture Free Classes: https://www.youtube.com/results?search_query=Talent+Battle+Accenture+preparation",
        'application_start_date': "August 2026",
        'application_last_date': "September 2026",
        'exam_date': "October 2026",
        'exam_timings': "Online Shift Slots: 10:00 AM / 02:00 PM",
        'exam_date_info': "Annual Hiring Drive"
    },
    # 53. RHCSA EX200
    {
        'exam_name': 'Red Hat Certified System Administrator (RHCSA EX200)',
        'category': 'private',
        'domain': 'Linux System Administration',
        'conducting_body': 'Red Hat',
        'website_url': 'https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-exam',
        'eligibility': "Qualification: Open to Linux administrators, DevOps engineers, and students. Red Hat System Administration I & II training recommended.",
        'syllabus_summary': "Format: 100% Performance-based practical exam on live RHEL environment (3 Hours, Passing: 210/300). Understand core tools, Shell scripting, Storage, User management, Security & firewalls.",
        'preparation_resources': "• Sander van Vugt RHCSA EX200 Course: https://www.youtube.com/results?search_query=Sander+van+Vugt+RHCSA+EX200+full+course\n• Learn Linux TV RHCSA Series: https://www.youtube.com/results?search_query=LearnLinuxTV+RHCSA+Red+Hat+Certified+System+Administrator",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Red Hat Kiosk / Remote)",
        'exam_timings': "Flexible Online / Kiosk Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 54. AWS DevOps Pro
    {
        'exam_name': 'AWS Certified DevOps Engineer Professional (DOP-C02)',
        'category': 'private',
        'domain': 'DevOps & Cloud Automation',
        'conducting_body': 'Amazon Web Services',
        'website_url': 'https://aws.amazon.com/certification/certified-devops-engineer-professional/',
        'eligibility': "Qualification: Prerequisite: AWS Associate Certification recommended. 2+ years experience provisioning, operating, and managing AWS environments.",
        'syllabus_summary': "Format: 75 Multiple Choice & Multiple Response Qs (180 Mins, Passing: 750/1000). SDLC Automation (22%), Configuration Management & IaC (17%), Resilient Cloud Systems (15%), Monitoring & Logging (15%), Incident Management (14%), Security (17%).",
        'preparation_resources': "• Stephane Maarek AWS DevOps Professional: https://www.youtube.com/results?search_query=Stephane+Maarek+AWS+DevOps+Engineer+Professional\n• freeCodeCamp AWS DevOps Pro Course: https://www.youtube.com/results?search_query=freeCodeCamp+AWS+DevOps+Engineer+Professional",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 55. Azure Data Engineer DP-203
    {
        'exam_name': 'Microsoft Certified: Azure Data Engineer Associate (DP-203)',
        'category': 'private',
        'domain': 'Cloud Data Pipelines & Synapse Analytics',
        'conducting_body': 'Microsoft',
        'website_url': 'https://learn.microsoft.com/en-us/credentials/certifications/azure-data-engineer/',
        'eligibility': "Qualification: Open to data engineers, database administrators, and cloud analytics developers. Knowledge of Azure Data Factory, Synapse, and Databricks.",
        'syllabus_summary': "Format: 40–60 Questions (120 Mins). Design and Implement Data Storage (15-20%), Develop Data Processing (40-45%), Secure, Monitor, and Optimize Storage & Processing (30-35%).",
        'preparation_resources': "• Eshaan Sharma Azure Data Engineer DP-203: https://www.youtube.com/results?search_query=Eshaan+Sharma+Azure+Data+Engineer+DP+203\n• freeCodeCamp Azure DP-203 Full Course: https://www.youtube.com/results?search_query=freeCodeCamp+Azure+Data+Engineer+DP+203",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 56. Google Professional Cloud Architect
    {
        'exam_name': 'Google Professional Cloud Architect',
        'category': 'private',
        'domain': 'Enterprise Cloud Architecture',
        'conducting_body': 'Google Cloud',
        'website_url': 'https://cloud.google.com/learn/certification/cloud-architect',
        'eligibility': "Qualification: Open to experienced cloud architects and enterprise infrastructure engineers. 3+ years industry experience including 1+ years designing GCP solutions recommended.",
        'syllabus_summary': "Format: 50 Multiple Choice Qs including case study analysis (120 Mins). Design and plan cloud solution architecture, Manage and provision cloud infrastructure, Ensure security and compliance, Analyze and optimize business processes.",
        'preparation_resources': "• freeCodeCamp Google Professional Cloud Architect: https://www.youtube.com/results?search_query=freeCodeCamp+Google+Professional+Cloud+Architect\n• Google Cloud Tech Architect Case Studies: https://www.youtube.com/results?search_query=Google+Cloud+Tech+Professional+Cloud+Architect",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Kryterion)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 57. CCNP Enterprise ENCOR
    {
        'exam_name': 'Cisco Certified Network Professional (CCNP Enterprise 350-401 ENCOR)',
        'category': 'private',
        'domain': 'Enterprise Networking & Security',
        'conducting_body': 'Cisco Systems',
        'website_url': 'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/professional/ccnp-enterprise.html',
        'eligibility': "Qualification: Recommended: 3-5 years experience implementing enterprise networking solutions. CCNA certification or equivalent knowledge.",
        'syllabus_summary': "Format: 90–110 Questions (120 Mins). Architecture (15%), Virtualization (10%), Infrastructure (30%), Network Assurance (10%), Security (20%), Automation (15%).",
        'preparation_resources': "• Jeremy's IT Lab CCNP ENCOR Series: https://www.youtube.com/results?search_query=Jeremys+IT+Lab+CCNP+ENCOR+350+401\n• NetworkChuck CCNP Enterprise Guide: https://www.youtube.com/results?search_query=NetworkChuck+CCNP+Enterprise",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 58. CISM
    {
        'exam_name': 'Certified Information Security Manager (CISM)',
        'category': 'private',
        'domain': 'Cybersecurity Management & Strategy',
        'conducting_body': 'ISACA',
        'website_url': 'https://www.isaca.org/credentialing/cism',
        'eligibility': "Qualification: 5+ years of verified information security work experience, with at least 3 years in 2 or more CISM domain areas.",
        'syllabus_summary': "Format: 150 Multiple Choice Questions (4 Hours, Passing: 450/800). Information Security Governance (17%), Information Security Risk Management (20%), Information Security Program (33%), Incident Management (30%).",
        'preparation_resources': "• Hemang Doshi CISM Exam Preparation: https://www.youtube.com/results?search_query=Hemang+Doshi+CISM+exam+preparation\n• Luke Ahmed CISM Prep Series: https://www.youtube.com/results?search_query=Luke+Ahmed+CISM+preparation",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (PSI Online / Test Center)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 59. AWS Security Specialist
    {
        'exam_name': 'AWS Certified Security Specialist (SCS-C02)',
        'category': 'private',
        'domain': 'Cloud Security & IAM Governance',
        'conducting_body': 'Amazon Web Services',
        'website_url': 'https://aws.amazon.com/certification/certified-security-specialty/',
        'eligibility': "Qualification: Recommended: 2+ years of hands-on experience securing AWS workloads and 5+ years IT security experience.",
        'syllabus_summary': "Format: 65 Questions (170 Mins, Passing: 750/1000). Threat Detection and Incident Response (14%), Security Logging and Monitoring (18%), Infrastructure Security (20%), Identity and Access Management (16%), Data Protection (32%).",
        'preparation_resources': "• Stephane Maarek AWS Security Specialty: https://www.youtube.com/results?search_query=Stephane+Maarek+AWS+Security+Specialty\n• freeCodeCamp AWS Security Specialist Course: https://www.youtube.com/results?search_query=freeCodeCamp+AWS+Security+Specialist",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 60. Oracle Java 1Z0-819
    {
        'exam_name': 'Oracle Certified Professional: Java SE Developer (1Z0-819)',
        'category': 'private',
        'domain': 'Object-Oriented Programming & Enterprise Java',
        'conducting_body': 'Oracle Corporation',
        'website_url': 'https://education.oracle.com/java-se-11-developer/pexam_1Z0-819',
        'eligibility': "Qualification: Open to software developers, students, and Java programmers. Knowledge of Java SE syntax, OOP, Streams, and Concurrency recommended.",
        'syllabus_summary': "Format: 50 Multiple Choice Questions (90 Mins, Passing: 68%). Fundamentals, OOP Design, Exception Handling, Collections & Generics, Streams & Lambda Expressions, Concurrency, I/O & NIO.2.",
        'preparation_resources': "• freeCodeCamp Java Certification Guide: https://www.youtube.com/results?search_query=freeCodeCamp+Java+full+course+programming\n• Java Brains OCP Java Certification Series: https://www.youtube.com/results?search_query=Java+Brains+OCP+Java+SE+Developer",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Online / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 61. CEH v12
    {
        'exam_name': 'Certified Ethical Hacker (CEH v12)',
        'category': 'private',
        'domain': 'Cybersecurity & Penetration Testing',
        'conducting_body': 'EC-Council',
        'website_url': 'https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/',
        'eligibility': "Qualification: Completion of official EC-Council training OR 2+ years documented work experience in InfoSec domain.",
        'syllabus_summary': "Format: 125 Multiple Choice Questions (4 Hours, Passing: 60%-85% adaptive). Footprinting, Scanning Networks, System Hacking, Malware Threats, Sniffing, Social Engineering, DoS, Web Server Hacking, Cryptography.",
        'preparation_resources': "• freeCodeCamp Ethical Hacking Course: https://www.youtube.com/results?search_query=freeCodeCamp+Ethical+Hacking+full+course\n• NetworkChuck CEH Cybersecurity Series: https://www.youtube.com/results?search_query=NetworkChuck+Certified+Ethical+Hacker+CEH",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (ECC Exam Centre)",
        'exam_timings': "Flexible Online Remote Proctored Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 62. CompTIA Security+
    {
        'exam_name': 'CompTIA Security+ (SY0-701)',
        'category': 'private',
        'domain': 'Cybersecurity & Information Assurance',
        'conducting_body': 'CompTIA',
        'website_url': 'https://www.comptia.org/certifications/security',
        'eligibility': "Qualification: Open to all IT security aspirants. CompTIA Network+ and 2 years IT administration experience recommended.",
        'syllabus_summary': "Format: Max 90 Questions (Multiple choice & Performance-based, 90 Mins, Passing: 750/900). General Security (12%), Threats & Vulnerabilities (22%), Architecture (18%), Operations (28%), Program Management (20%).",
        'preparation_resources': "• Professor Messer CompTIA Security+ SY0-701 Course: https://www.youtube.com/results?search_query=Professor+Messer+CompTIA+Security+SY0+701+course\n• Inside Cloud and Security CompTIA Prep: https://www.youtube.com/results?search_query=Inside+Cloud+and+Security+CompTIA+Security",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Online / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 63. Salesforce ADM-201
    {
        'exam_name': 'Salesforce Certified Administrator (ADM-201)',
        'category': 'private',
        'domain': 'CRM Architecture & Cloud Administration',
        'conducting_body': 'Salesforce',
        'website_url': 'https://trailhead.salesforce.com/credentials/administrator',
        'eligibility': "Qualification: Open to CRM administrators, developers, and business analysts. Hands-on experience with Salesforce Trailhead modules recommended.",
        'syllabus_summary': "Format: 60 Multiple Choice Qs (105 Mins, Passing: 65%). Configuration & Setup (20%), Object Manager & Lightning App Builder (20%), Sales & Service Applications (12%), Data & Analytics Management (14%), Automation (16%).",
        'preparation_resources': "• Salesforce Trailhead Official Guides: https://www.youtube.com/results?search_query=Salesforce+Admin+ADM+201+full+course\n• Salesforce Hulk Certification Playlists: https://www.youtube.com/results?search_query=Salesforce+Hulk+Admin+201+preparation",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Kryterion Webassessor)",
        'exam_timings': "Flexible Online / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 64. PMI PMP
    {
        'exam_name': 'PMI Project Management Professional (PMP)',
        'category': 'private',
        'domain': 'Agile & Enterprise Project Management',
        'conducting_body': 'Project Management Institute (PMI)',
        'website_url': 'https://www.pmi.org/certifications/project-management-pmp',
        'eligibility': "Qualification: 4-year degree + 36 months leading projects + 35 hours PM education OR High school diploma + 60 months leading projects + 35 hours PM education.",
        'syllabus_summary': "Format: 180 Questions (230 Mins). People Domain (42%), Process Domain (50%), Business Environment Domain (8%). Predictive, Agile, and Hybrid project management frameworks.",
        'preparation_resources': "• Andrew Ramdayal PMP Exam Prep & Mindset: https://www.youtube.com/results?search_query=Andrew+Ramdayal+PMP+exam+prep+mindset\n• David McLachlan 200 Agile PMP Questions: https://www.youtube.com/results?search_query=David+McLachlan+PMP+Agile+questions",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 65. Scrum Master CSM
    {
        'exam_name': 'Scrum Alliance Certified ScrumMaster (CSM)',
        'category': 'private',
        'domain': 'Agile Leadership & Software Development',
        'conducting_body': 'Scrum Alliance',
        'website_url': 'https://www.scrumalliance.org/get-certified/scrum-master-track/certified-scrummaster',
        'eligibility': "Qualification: Completion of a 16-hour live Certified ScrumMaster course from a Certified Scrum Trainer (CST). No age limit.",
        'syllabus_summary': "Format: 50 Multiple Choice Questions (60 Mins, Passing: 37/50 or 74%). Lean & Agile Values, Scrum Theory, Scrum Framework (Events, Artifacts, Roles), Agile Coaching & Facilitation.",
        'preparation_resources': "• Scrum Master Prep Free Lectures: https://www.youtube.com/results?search_query=Certified+ScrumMaster+CSM+exam+prep\n• Development That Pays Scrum Master Series: https://www.youtube.com/results?search_query=Development+That+Pays+Scrum+Master",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand Online Exam",
        'exam_timings': "24/7 Online Exam Slot",
        'exam_date_info': "Continuous Certification"
    },
    # 66. APICS CSCP
    {
        'exam_name': 'APICS Certified Supply Chain Professional (CSCP)',
        'category': 'private',
        'domain': 'Supply Chain Management & Logistics',
        'conducting_body': 'ASCM / APICS',
        'website_url': 'https://www.ascm.org/learning-development/certifications-credentials/cscp/',
        'eligibility': "Qualification: 3 years related business experience OR Bachelor's degree OR hold CPIM, CLTD, CSCP, or SCOR-P designation.",
        'syllabus_summary': "Format: 150 Questions (3.5 Hours, Passing: 300/350 scale). Supply Chains & Demand Management (30%), Global Supply Networks (20%), Source, Make & Deliver (30%), Risk Management (20%).",
        'preparation_resources': "• APICS CSCP Exam Preparation Lectures: https://www.youtube.com/results?search_query=APICS+CSCP+exam+preparation+lectures",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 67. PMI-ACP
    {
        'exam_name': 'PMI Agile Certified Practitioner (PMI-ACP)',
        'category': 'private',
        'domain': 'Agile Project Management & Scrum',
        'conducting_body': 'Project Management Institute (PMI)',
        'website_url': 'https://www.pmi.org/certifications/agile-acp',
        'eligibility': "Qualification: 8 months agile project experience within last 3 years + 12 months general project experience + 21 contact hours of agile training.",
        'syllabus_summary': "Format: 120 Questions (3 Hours, Passing: 70%). Agile Principles, Value-Driven Delivery, Stakeholder Engagement, Team Performance, Adaptive Planning, Continuous Improvement.",
        'preparation_resources': "• David McLachlan PMI-ACP Exam Prep: https://www.youtube.com/results?search_query=David+McLachlan+PMI+ACP+preparation",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Test Center / Online Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 68. Databricks Data Engineer
    {
        'exam_name': 'Databricks Certified Data Engineer Associate',
        'category': 'private',
        'domain': 'Big Data & Apache Spark Engineering',
        'conducting_body': 'Databricks',
        'website_url': 'https://www.databricks.com/university/certification/data-engineer-associate',
        'eligibility': "Qualification: Open to data engineers and Big Data developers. Knowledge of PySpark, Delta Lake, SQL, and Databricks workflows recommended.",
        'syllabus_summary': "Format: 45 Multiple Choice Questions (90 Mins, Passing: 70%). Databricks Lakehouse Platform (24%), ELT with Spark SQL and Python (29%), Incremental Processing with Delta Live Tables (22%), Production Pipelines (16%), Data Governance (9%).",
        'preparation_resources': "• Databricks Academy Data Engineering Course: https://www.youtube.com/results?search_query=Databricks+Certified+Data+Engineer+Associate+full+course\n• Advancing Analytics Databricks Tutorials: https://www.youtube.com/results?search_query=Advancing+Analytics+Databricks+Data+Engineering",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Kryterion)",
        'exam_timings': "Flexible Online Remote Proctored Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 69. TensorFlow Developer
    {
        'exam_name': 'TensorFlow Developer Certificate (Google AI)',
        'category': 'private',
        'domain': 'Artificial Intelligence & Deep Learning',
        'conducting_body': 'TensorFlow / Google',
        'website_url': 'https://www.tensorflow.org/certificate',
        'eligibility': "Qualification: Open to AI developers, data scientists, and ML engineers. Proficiency in Python, TensorFlow 2.x, Computer Vision, and NLP required.",
        'syllabus_summary': "Format: Hands-on practical exam building ML models in PyCharm/Python (5 Hours duration). Building & training neural networks, Computer Vision (CNNs), Natural Language Processing (RNNs, LSTMs), Time Series Forecasting.",
        'preparation_resources': "• freeCodeCamp TensorFlow Developer Certificate Course: https://www.youtube.com/results?search_query=freeCodeCamp+TensorFlow+Developer+Certificate+full+course\n• Daniel Bourke TensorFlow Deep Learning: https://www.youtube.com/results?search_query=Daniel+Bourke+TensorFlow+2+complete+course",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand Online Practical Exam",
        'exam_timings': "24/7 Self-Paced 5-Hour Exam Window",
        'exam_date_info': "Continuous Certification"
    },
    # 70. Snowflake SnowPro Core
    {
        'exam_name': 'Snowflake SnowPro Core Certification',
        'category': 'private',
        'domain': 'Cloud Data Warehousing & Analytics',
        'conducting_body': 'Snowflake',
        'website_url': 'https://www.snowflake.com/en/resources/certifications/',
        'eligibility': "Qualification: Open to data engineers, database administrators, and cloud architects. Recommended: 6+ months experience working with Snowflake Cloud Data Platform.",
        'syllabus_summary': "Format: 100 Questions (115 Mins, Passing: 750/1000). Snowflake Architecture & Features (20-25%), Security & Protection (20-25%), Performance Concepts (10-15%), Data Loading & Transformation (20-25%), Storage & Protection (10-15%).",
        'preparation_resources': "• Snowflake Official Essentials Tutorials: https://www.youtube.com/results?search_query=Snowflake+SnowPro+Core+Certification+full+course\n• K21Academy Snowflake SnowPro Core Guide: https://www.youtube.com/results?search_query=K21Academy+Snowflake+SnowPro+Core",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Pearson VUE)",
        'exam_timings': "Flexible Online / Test Center Slots",
        'exam_date_info': "Continuous Certification"
    },
    # 71. CFA Level 1 & 2
    {
        'exam_name': 'CFA Level 1 & Level 2 Exam',
        'category': 'private',
        'domain': 'Investment Banking & Equity Research',
        'conducting_body': 'CFA Institute',
        'website_url': 'https://www.cfainstitute.org/en/programs/cfa/exam',
        'eligibility': "Qualification: Bachelor's degree (or final year undergraduate student) OR 4,000 hours of professional work experience. International Passport: Mandatory for registration.",
        'syllabus_summary': "Format Level 1: 180 MCQs (two 135-minute sessions). Ethical & Professional Standards, Quantitative Methods, Economics, Financial Statement Analysis, Corporate Issuers, Equity, Fixed Income, Derivatives, Alternative Investments.",
        'preparation_resources': "• Mark Meldrum CFA Level 1 Free Lectures: https://www.youtube.com/results?search_query=Mark+Meldrum+CFA+Level+1+free+lectures\n• Fintree CFA Level 1 Preparation: https://www.youtube.com/results?search_query=Fintree+CFA+Level+1+playlist",
        'application_start_date': "February / May / August / November Sessions",
        'application_last_date': "Rolling Deadlines",
        'exam_date': "Feb, May, Aug, Nov 2026",
        'exam_timings': "Session 1: 09:00 AM – 11:15 AM | Session 2: 01:30 PM – 03:45 PM",
        'exam_date_info': "Quarterly Exam Windows"
    },
    # 72. CA Final
    {
        'exam_name': 'CA Final Exam (Chartered Accountancy)',
        'category': 'private',
        'domain': 'Corporate Auditing & Taxation',
        'conducting_body': 'ICAI',
        'website_url': 'https://www.icai.org/',
        'eligibility': "Qualification: Passed CA Intermediate exam + completed mandatory 2/3 years articleship practical training under a practicing Chartered Accountant. Registered with ICAI.",
        'syllabus_summary': "Format: Group 1 (Financial Reporting, Advanced Financial Management, Advanced Auditing) + Group 2 (Direct Tax & International Tax, Indirect Tax Laws, Integrated Business Solutions). 3 Hours per paper, 100 Marks each.",
        'preparation_resources': "• ICAI Official CA Final Revision Series: https://www.youtube.com/results?search_query=ICAI+CA+Final+free+revision+lectures\n• CA Swapnil Patni Final Revision: https://www.youtube.com/results?search_query=CA+Final+revision+lectures",
        'application_start_date': "March 2026 / August 2026",
        'application_last_date': "April 2026 / September 2026",
        'exam_date': "May 2026 / November 2026",
        'exam_timings': "Single Shift: 02:00 PM – 05:00 PM",
        'exam_date_info': "Biannual ICAI Cycle"
    },
    # 73. CS Professional
    {
        'exam_name': 'CS Professional Exam (Company Secretary)',
        'category': 'private',
        'domain': 'Corporate Governance & Law',
        'conducting_body': 'ICSI',
        'website_url': 'https://www.icsi.edu/students/examination/',
        'eligibility': "Qualification: Passed CS Executive Programme examination + enrolled in CS Professional Programme with ICSI + completed compulsory practical training.",
        'syllabus_summary': "Format: Group 1 (ESG, Drafting & Pleadings, Compliance Management) + Group 2 (Strategic Management & Corporate Finance, Corporate Restructuring, Arbitrations & Dispute Resolution). 3 Hours per paper, 100 Marks.",
        'preparation_resources': "• Inspire Academy CS Professional Preparation: https://www.youtube.com/results?search_query=Inspire+Academy+CS+Professional+lectures\n• Unique Academy CS Professional Series: https://www.youtube.com/results?search_query=Unique+Academy+CS+Professional+lectures",
        'application_start_date': "March 2026 / August 2026",
        'application_last_date': "April 2026 / September 2026",
        'exam_date': "June 2026 / December 2026",
        'exam_timings': "Single Shift: 09:00 AM – 12:00 PM",
        'exam_date_info': "Biannual ICSI Cycle"
    },
    # 74. CMA Final
    {
        'exam_name': 'CMA Final Exam (Cost & Management Accounting)',
        'category': 'private',
        'domain': 'Management Accounting & Finance',
        'conducting_body': 'ICMAI',
        'website_url': 'https://icmai.in/',
        'eligibility': "Qualification: Passed CMA Intermediate examination from ICMAI + completed mandatory practical training requirements.",
        'syllabus_summary': "Format: Group III (Corporate Laws & Compliance, Strategic Financial Management, Strategic Cost Management, Direct Tax & International Taxation) + Group IV (Financial Reporting, Cost & Management Audit, Indirect Tax Laws). 3 Hours per paper, 100 Marks.",
        'preparation_resources': "• CA CS CMA Nikunj Shah Free Classes: https://www.youtube.com/results?search_query=CMA+Final+exam+preparation+free+lectures\n• SJC Institute CMA Final Prep: https://www.youtube.com/results?search_query=SJC+Institute+CMA+Final+lectures",
        'application_start_date': "March 2026 / August 2026",
        'application_last_date': "April 2026 / September 2026",
        'exam_date': "June 2026 / December 2026",
        'exam_timings': "Single Shift: 02:00 PM – 05:00 PM",
        'exam_date_info': "Biannual ICMAI Cycle"
    },
    # 75. USMLE Step 1 & 2
    {
        'exam_name': 'USMLE Step 1 & Step 2 CK',
        'category': 'private',
        'domain': 'Medical Licensing (USA)',
        'conducting_body': 'FSMB / NBME',
        'website_url': 'https://www.usmle.org/',
        'eligibility': "Qualification: Medical student or graduate of US/Canadian medical school or international medical school listed in World Directory of Medical Schools with ECFMG eligibility.",
        'syllabus_summary': "Format Step 1 (Pass/Fail): 280 MCQs (7 blocks of 60 Mins). Pathology, Physiology, Pharmacology, Anatomy, Biochem. Step 2 CK: 318 MCQs (8 blocks of 60 Mins). Clinical Knowledge in Internal Medicine, Surgery, Pediatrics, OBG, Psychiatry.",
        'preparation_resources': "• Dirty Medicine USMLE High Yield: https://www.youtube.com/results?search_query=Dirty+Medicine+USMLE+Step+1+playlist\n• Rahul Damania USMLE Prep: https://www.youtube.com/results?search_query=Rahul+Damania+USMLE+high+yield+lectures",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Prometric Centers)",
        'exam_timings': "Flexible Test Center Slots",
        'exam_date_info': "Continuous Medical Licensing"
    },
    # 76. USMLE Step 3
    {
        'exam_name': 'USMLE Step 3 Exam',
        'category': 'private',
        'domain': 'Independent Medical Practice (USA)',
        'conducting_body': 'FSMB / NBME',
        'website_url': 'https://www.usmle.org/step-exams/step-3',
        'eligibility': "Qualification: MD or DO degree from US/Canadian medical school OR ECFMG certified international medical graduate + Passed USMLE Step 1 and Step 2 CK.",
        'syllabus_summary': "Day 1 (FIP - 232 MCQs, 7 Hours): Foundations of Independent Practice. Day 2 (ACM - 180 MCQs + 13 Computer-based Case Simulations - CCS, 9 Hours): Advanced Clinical Management.",
        'preparation_resources': "• USMLE Step 3 High Yield CCS & Prep: https://www.youtube.com/results?search_query=USMLE+Step+3+CCS+cases+preparation",
        'application_start_date': "Open Year-Round",
        'application_last_date': "Flexible Scheduling",
        'exam_date': "On-Demand (Prometric Centers)",
        'exam_timings': "Two-Day Examination Slots",
        'exam_date_info': "Continuous Medical Licensing"
    },
    # 77. NATA
    {
        'exam_name': 'NATA 2027 (National Aptitude Test in Architecture)',
        'category': 'private',
        'domain': 'Architecture Design',
        'conducting_body': 'Council of Architecture',
        'website_url': 'https://www.nata.in/',
        'eligibility': "Qualification: Passed 10+2 examination with Physics, Chemistry & Mathematics OR 10+3 Diploma with Mathematics with min 50% aggregate marks. No age limit.",
        'syllabus_summary': "Format: 125 Questions (200 Marks, 180 Minutes). Part A: Drawing & Composition Test (Offline). Part B: Online MCQs on Visual Reasoning, Architectural Awareness, Physics, Chemistry, Mathematics, Spatial Intelligence.",
        'preparation_resources': "• Design Studio NATA Preparation: https://www.youtube.com/results?search_query=NATA+architecture+exam+preparation+drawing+aptitude\n• Silica Institute NATA Prep Series: https://www.youtube.com/results?search_query=Silica+NATA+preparation+drawing+lectures",
        'application_start_date': "March 2026",
        'application_last_date': "April 2026",
        'exam_date': "April / May / June 2026 (Multiple Phases)",
        'exam_timings': "Session 1: 10:00 AM – 01:00 PM | Session 2: 02:30 PM – 05:30 PM",
        'exam_date_info': "Multi-Phase Annual Exam"
    },
    # 78. NIFT PG
    {
        'exam_name': 'NIFT PG 2027 (Master of Design / Fashion)',
        'category': 'private',
        'domain': 'Fashion & Visual Design',
        'conducting_body': 'NIFT India',
        'website_url': 'https://nift.ac.in/',
        'eligibility': "Qualification: Undergraduate degree in any discipline from a recognized University OR 3-year Diploma in UG Design from NIFT/NID. Age limit: No age limit for PG courses.",
        'syllabus_summary': "Format: GAT (General Ability Test: English, Quant, Reasoning, GK - 30%) + CAT (Creative Ability Test: Design Thinking, Illustration, Sketching - 40%) + Situation Test / Personal Interview (30%).",
        'preparation_resources': "• SILICA NIFT CAT & GAT Free Lectures: https://www.youtube.com/results?search_query=SILICA+NIFT+preparation+CAT+GAT+lectures\n• BRDS NIFT Preparation Tutorials: https://www.youtube.com/results?search_query=BRDS+NIFT+preparation+sketching+lectures",
        'application_start_date': "November 2026",
        'application_last_date': "December 2026",
        'exam_date': "February 2027",
        'exam_timings': "GAT: 10:00 AM – 12:00 PM | CAT: 01:30 PM – 04:30 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 79. NID DAT PG
    {
        'exam_name': 'NID DAT PG 2027',
        'category': 'private',
        'domain': 'Industrial & Product Design',
        'conducting_body': 'National Institute of Design',
        'website_url': 'https://admissions.nid.edu/',
        'eligibility': "Qualification: Bachelor's degree of min 4-year duration in any specialization OR 4-year Post Graduate Diploma in Design from recognized institute. Max Age Limit: 30 years.",
        'syllabus_summary': "Stage 1 DAT Prelims: Objective & Descriptive Design Test (Lateral Thinking, Problem Solving, Visual Communication, Storyboarding). Stage 2 DAT Mains: Studio Test & Portfolio Review / Personal Interview.",
        'preparation_resources': "• DQ Labs NID DAT Prep Tutorials: https://www.youtube.com/results?search_query=DQ+Labs+NID+DAT+preparation+tutorials\n• AFA NID DAT Design Preparation: https://www.youtube.com/results?search_query=AFA+NID+DAT+preparation+lectures",
        'application_start_date': "September 2026",
        'application_last_date': "December 2026",
        'exam_date': "December 2026 (Prelims) / April 2027 (Mains)",
        'exam_timings': "Single Shift: 10:00 AM – 01:00 PM",
        'exam_date_info': "Annual Cycle 2026-2027"
    },
    # 80. CEPT Master of Architecture
    {
        'exam_name': 'CEPT Master of Architecture / Planning 2027',
        'category': 'private',
        'domain': 'Urban Design & Architecture',
        'conducting_body': 'CEPT University',
        'website_url': 'https://admissions.cept.ac.in/postgraduate/faculty-of-architecture',
        'eligibility': "Qualification: Bachelor's degree in Architecture (B.Arch) or Planning (B.Plan) recognized by COA / AICTE with minimum 55% aggregate marks (50% for SC/ST).",
        'syllabus_summary': "Stage 1: Design Aptitude Test & Essay Writing (Architectural History, Spatial Analysis, Urban Planning Concepts). Stage 2: Design Portfolio Evaluation & Personal Interview.",
        'preparation_resources': "• CEPT PG Entrance Exam Portfolio & Prep Guide: https://www.youtube.com/results?search_query=CEPT+University+PG+entrance+exam+preparation\n• Architecture Prep CEPT Guide: https://www.youtube.com/results?search_query=CEPT+M+Arch+entrance+preparation",
        'application_start_date': "January 2027",
        'application_last_date': "March 2027",
        'exam_date': "April 2027",
        'exam_timings': "Single Shift: 10:00 AM – 01:00 PM",
        'exam_date_info': "Annual CEPT PG Drive"
    }
]

print(f"Updating database for all {len(EXAM_DETAILS)} canonical exams...")

for detail in EXAM_DETAILS:
    exam_obj, created = GovernmentExam.objects.update_or_create(
        exam_name=detail['exam_name'],
        defaults={
            'category': detail['category'],
            'domain': detail['domain'],
            'conducting_body': detail['conducting_body'],
            'website_url': detail['website_url'],
            'eligibility': detail['eligibility'],
            'syllabus_summary': detail['syllabus_summary'],
            'preparation_resources': detail['preparation_resources'],
            'application_start_date': detail['application_start_date'],
            'application_last_date': detail['application_last_date'],
            'exam_date': detail['exam_date'],
            'exam_timings': detail['exam_timings'],
            'exam_date_info': detail['exam_date_info'],
            'is_active': True
        }
    )
    status = "Created" if created else "Updated"
    print(f"[{status}] {exam_obj.exam_name} -> {exam_obj.category.upper()} | {exam_obj.domain}")

print(f"\nSuccessfully updated {GovernmentExam.objects.count()} total exams in db.sqlite3!")
print(f"Government & PSU Exams: {GovernmentExam.objects.filter(category='govt').count()}")
print(f"Private & Tech Certification Exams: {GovernmentExam.objects.filter(category='private').count()}")
