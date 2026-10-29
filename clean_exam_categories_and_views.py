import os
import re
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import GovernmentExam
from update_all_exam_details_and_youtube_links import EXAM_DETAILS

print("=== STARTING EXAM CATEGORIES CLEANUP & CANONICAL DEDUPLICATION ===")

# Delete all existing non-canonical or duplicate exam entries
GovernmentExam.objects.all().delete()

created_count = 0
for item in EXAM_DETAILS:
    GovernmentExam.objects.create(
        exam_name=item['exam_name'],
        category=item['category'],
        domain=item['domain'],
        conducting_body=item['conducting_body'],
        website_url=item['website_url'],
        eligibility=item['eligibility'],
        syllabus_summary=item['syllabus_summary'],
        preparation_resources=item['preparation_resources'],
        application_start_date=item['application_start_date'],
        application_last_date=item['application_last_date'],
        exam_date=item['exam_date'],
        exam_timings=item['exam_timings'],
        exam_date_info=item['exam_date_info'],
        is_active=True
    )
    created_count += 1

print(f"Created {created_count} canonical, unique exam records with full details and YouTube links.")
print(f"Govt & PSU Exams: {GovernmentExam.objects.filter(category='govt').count()}")
print(f"Private & Tech Certification Exams: {GovernmentExam.objects.filter(category='private').count()}")
print(f"Total Exams: {GovernmentExam.objects.count()}")
