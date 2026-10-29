import os
import re
import django
import requests
import urllib3
import concurrent.futures
from urllib.parse import quote_plus

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import Course, JobOpportunity, Internship, Certification, GovernmentExam

print("=== STARTING ULTIMATE COURSE & OPPORTUNITY LINK REPAIR ===")

VALID_W3_PATHS = {
    'html', 'css', 'js', 'javascript', 'python', 'sql', 'php', 'bootstrap', 'bootstrap4', 'bootstrap5',
    'jquery', 'react', 'java', 'c', 'cpp', 'cs', 'r', 'kotlin', 'swift', 'git', 'node', 'django',
    'mysql', 'postgresql', 'mongodb', 'typescript', 'aws', 'cybersecurity', 'ai', 'data_analytics',
    'html5', 'xml', 'json', 'asp', 'pandas', 'numpy', 'scipy', 'excel', 'gdb'
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

def clean(t):
    if not t: return ""
    t = re.sub(r'#\d+', '', t)
    t = re.sub(r'\bCycle\b.*', '', t, flags=re.IGNORECASE)
    return re.sub(r'\s+', ' ', t).strip()

def get_valid_course_url(course):
    ctitle = clean(course.title)
    title_enc = quote_plus(ctitle)
    provider_lower = course.provider.lower().strip()
    url = course.url.strip()

    if provider_lower in ['w3schools']:
        skill_name = course.skill.name.lower().strip().replace(' ', '') if hasattr(course, 'skill') and course.skill else 'html'
        if skill_name in VALID_W3_PATHS:
            return f"https://www.w3schools.com/{skill_name}/"
        elif 'python' in skill_name or 'py' in skill_name:
            return "https://www.w3schools.com/python/"
        elif 'sql' in skill_name or 'db' in skill_name or 'data' in skill_name:
            return "https://www.w3schools.com/sql/"
        elif 'java' in skill_name:
            return "https://www.w3schools.com/java/"
        elif 'c++' in skill_name or 'cpp' in skill_name:
            return "https://www.w3schools.com/cpp/"
        elif 'html' in skill_name or 'web' in skill_name:
            return "https://www.w3schools.com/html/"
        elif 'css' in skill_name or 'design' in skill_name:
            return "https://www.w3schools.com/css/"
        elif 'js' in skill_name or 'script' in skill_name:
            return "https://www.w3schools.com/js/"
        else:
            return f"https://www.coursera.org/search?query={title_enc}"

    if 'udemy.com/course/' in url and re.search(r'-\d{3,5}$', url):
        return f"https://www.udemy.com/courses/search/?q={title_enc}"

    if provider_lower in ['udemy']:
        return f"https://www.udemy.com/courses/search/?q={title_enc}"
    elif provider_lower in ['coursera']:
        return f"https://www.coursera.org/search?query={title_enc}"
    elif provider_lower in ['geeksforgeeks', 'gfg']:
        return f"https://www.geeksforgeeks.org/search/?q={title_enc}"
    elif provider_lower in ['simplilearn']:
        return f"https://www.simplilearn.com/search?q={title_enc}"
    elif provider_lower in ['youtube']:
        return f"https://www.youtube.com/results?search_query={title_enc}"
    elif provider_lower in ['swayam', 'nptel']:
        return f"https://swayam.gov.in/explorer?searchText={title_enc}"
    elif provider_lower in ['leetcode']:
        return f"https://leetcode.com/problemset/all/?search={title_enc}"
    elif provider_lower in ['hackerrank']:
        return f"https://www.hackerrank.com/domains/python"
    elif provider_lower in ['infosys springboard']:
        return f"https://infyspringboard.onwingspan.com/web/en/page/search?q={title_enc}"
    elif provider_lower in ['tcs ion']:
        return "https://learning.tcsion.org/"
    elif provider_lower in ['tap academy']:
        return "https://tapacademy.com/full-stack-web-development-course/"
    elif provider_lower in ['pentagon space']:
        return "https://pentagonspace.in/courses"
    elif provider_lower in ['dhee coding']:
        return "https://dheecoding.com"
    elif provider_lower in ['github']:
        return "https://github.com/education"
    elif provider_lower in ['unstop']:
        return f"https://unstop.com/courses?searchTerm={title_enc}"
    else:
        return f"https://www.coursera.org/search?query={title_enc}"

print("Updating Course URLs in database...")
courses_updated = 0
for course in Course.objects.all():
    ctitle = clean(course.title)
    new_url = get_valid_course_url(course)
    if course.url != new_url or course.title != ctitle:
        course.title = ctitle
        course.url = new_url
        course.save()
        courses_updated += 1

print(f"Updated {courses_updated} Course records with valid platform URLs.")
