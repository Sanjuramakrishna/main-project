import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import GovernmentExam

print("=== EXAM DATABASE STATUS ===")
print("Total Active Exams:", GovernmentExam.objects.filter(is_active=True).count())
print("Government & PSU Exams:", GovernmentExam.objects.filter(is_active=True, category='govt').count())
print("Private & Certification Exams:", GovernmentExam.objects.filter(is_active=True, category='private').count())

domains = sorted(list(set(GovernmentExam.objects.filter(is_active=True).values_list('domain', flat=True))))
print("\nUnique Domains (", len(domains), "):")
for d in domains:
    count = GovernmentExam.objects.filter(is_active=True, domain=d).count()
    print(f"  - {d}: {count} exams")
