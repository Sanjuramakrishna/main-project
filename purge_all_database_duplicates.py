import os
import sys
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import JobOpportunity, Internship, ProjectIdea, Certification
from careers.models import Career, CareerRecommendation

def clean_key(text):
    if not text:
        return ""
    text = re.sub(r'#\d+', '', text)
    text = re.sub(r'\s*Specialist\s*', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    return text

def purge_duplicate_jobs():
    print("[INFO] Purging duplicate JobOpportunity database records...")
    jobs = list(JobOpportunity.objects.order_by('id').all())
    seen = {}
    deleted = 0
    for j in jobs:
        key = (clean_key(j.title), clean_key(j.company))
        if key in seen:
            j.delete()
            deleted += 1
        else:
            seen[key] = j.id
    print(f"[SUCCESS] Deleted {deleted} duplicate JobOpportunity records. Remaining unique: {JobOpportunity.objects.count()}")

def purge_duplicate_internships():
    print("[INFO] Purging duplicate Internship database records...")
    interns = list(Internship.objects.order_by('id').all())
    seen = {}
    deleted = 0
    for i in interns:
        key = (clean_key(i.title), clean_key(i.organization))
        if key in seen:
            i.delete()
            deleted += 1
        else:
            seen[key] = i.id
    print(f"[SUCCESS] Deleted {deleted} duplicate Internship records. Remaining unique: {Internship.objects.count()}")

def purge_duplicate_projects():
    print("[INFO] Purging duplicate ProjectIdea database records...")
    projects = list(ProjectIdea.objects.order_by('id').all())
    seen = {}
    deleted = 0
    for p in projects:
        key = clean_key(p.title)
        if key in seen:
            p.delete()
            deleted += 1
        else:
            seen[key] = p.id
    print(f"[SUCCESS] Deleted {deleted} duplicate ProjectIdea records. Remaining unique: {ProjectIdea.objects.count()}")

def purge_duplicate_certifications():
    print("[INFO] Purging duplicate Certification database records...")
    certs = list(Certification.objects.order_by('id').all())
    seen = {}
    deleted = 0
    for c in certs:
        key = clean_key(c.title)
        if key in seen:
            c.delete()
            deleted += 1
        else:
            seen[key] = c.id
    print(f"[SUCCESS] Deleted {deleted} duplicate Certification records. Remaining unique: {Certification.objects.count()}")

def purge_duplicate_recommendations():
    print("[INFO] Purging duplicate Career & CareerRecommendation records...")
    # Deduplicate Careers first
    careers = list(Career.objects.order_by('id').all())
    seen_careers = {}
    career_map = {}
    for car in careers:
        key = clean_key(car.title)
        if key in seen_careers:
            canonical_id = seen_careers[key]
            career_map[car.id] = canonical_id
            # Move recommendations to canonical career
            CareerRecommendation.objects.filter(career_id=car.id).update(career_id=canonical_id)
            car.delete()
        else:
            seen_careers[key] = car.id

    # Deduplicate User CareerRecommendations
    recs = list(CareerRecommendation.objects.order_by('-match_percentage', 'id').all())
    seen_recs = {}
    deleted_recs = 0
    for r in recs:
        key = (r.user_id, clean_key(r.career.title))
        if key in seen_recs:
            r.delete()
            deleted_recs += 1
        else:
            seen_recs[key] = r.id

    print(f"[SUCCESS] Deleted duplicate Career/CareerRecommendation records. Remaining unique recommendations: {CareerRecommendation.objects.count()}")

if __name__ == '__main__':
    purge_duplicate_jobs()
    purge_duplicate_internships()
    purge_duplicate_projects()
    purge_duplicate_certifications()
    purge_duplicate_recommendations()
    print("[SUCCESS] All 5 entity database deduplications complete!")
