import os
import sys
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity, Internship, ProjectIdea

def deduplicate_jobs():
    print("[INFO] Deduplicating JobOpportunity database records...")
    jobs = list(JobOpportunity.objects.order_by('id').all())
    seen = {}
    deleted_count = 0
    for job in jobs:
        norm_title = re.sub(r'\s+', ' ', job.title.strip().lower())
        norm_company = re.sub(r'\s+', ' ', job.company.strip().lower())
        key = (norm_title, norm_company)
        if key in seen:
            job.delete()
            deleted_count += 1
        else:
            seen[key] = job.id
    print(f"[SUCCESS] Deleted {deleted_count} duplicate JobOpportunity records. Remaining: {JobOpportunity.objects.count()}")

def deduplicate_internships():
    print("[INFO] Deduplicating Internship database records...")
    internships = list(Internship.objects.order_by('id').all())
    seen = {}
    deleted_count = 0
    for intern in internships:
        norm_title = re.sub(r'\s+', ' ', intern.title.strip().lower())
        norm_org = re.sub(r'\s+', ' ', intern.organization.strip().lower())
        key = (norm_title, norm_org)
        if key in seen:
            intern.delete()
            deleted_count += 1
        else:
            seen[key] = intern.id
    print(f"[SUCCESS] Deleted {deleted_count} duplicate Internship records. Remaining: {Internship.objects.count()}")

def deduplicate_projects():
    print("[INFO] Deduplicating ProjectIdea database records...")
    projects = list(ProjectIdea.objects.order_by('id').all())
    seen = {}
    deleted_count = 0
    for proj in projects:
        norm_title = re.sub(r'\s+', ' ', proj.title.strip().lower())
        key = norm_title
        if key in seen:
            proj.delete()
            deleted_count += 1
        else:
            seen[key] = proj.id
    print(f"[SUCCESS] Deleted {deleted_count} duplicate ProjectIdea records. Remaining: {ProjectIdea.objects.count()}")

if __name__ == '__main__':
    deduplicate_jobs()
    deduplicate_internships()
    deduplicate_projects()
    print("[SUCCESS] All database record deduplication complete!")
