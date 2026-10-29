import os
import re
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from opportunities.models import Internship
from profiles.models import Skill
from opportunities.views import is_domain_compatible

DOMAIN_SKILLS_MAP = {
    'tech': ['Python', 'Java', 'Data Structures', 'Web Development', 'SQL', 'React', 'JavaScript', 'Node.js', 'Docker', 'Git', 'C++'],
    'medical': ['Clinical Research', 'Pharmacology', 'Medical Terminology', 'Patient Care', 'Healthcare Data', 'Biomedical Science', 'Anatomy', 'Clinical Diagnosis'],
    'commerce': ['Financial Analysis', 'Accounting', 'Taxation', 'Tally Prime', 'Excel', 'Banking', 'Investment Management', 'Financial Modeling', 'Corporate Finance'],
    'legal': ['Corporate Law', 'Legal Drafting', 'Contract Law', 'Intellectual Property', 'Litigation', 'Legal Research', 'Cyber Law', 'Data Privacy'],
    'agriculture': ['Agronomy', 'Soil Science', 'Agribusiness', 'Crop Protection', 'Horticulture', 'Sericulture', 'Plant Breeding', 'AgriTech'],
    'architecture': ['AutoCAD', 'Revit BIM', '3D Modeling', 'Urban Planning', 'Interior Design', 'Structural Engineering', 'Parametric Design', 'Rhino 3D'],
    'arts': ['Graphic Design', 'Journalism', 'Content Writing', 'Digital Media', 'Public Relations', 'UI/UX Design', 'Figma', 'Adobe Photoshop', 'Branding'],
    'science': ['Research', 'Biotechnology', 'Chemistry', 'Data Analysis', 'Mathematics', 'Physics', 'Numerical Analysis', 'Laboratory Techniques', 'Microbiology']
}

def enrich_all_internships():
    print("[INFO] Enriching all 688+ internships with domain and degree required skills...")
    
    internships = Internship.objects.all()
    updated_count = 0

    for intern in internships:
        text_full = f"{intern.title} {intern.organization} {intern.description} {intern.eligibility}".lower()
        
        # Determine domain cluster
        detected_domain = intern.domain.lower() if intern.domain else 'tech'
        if detected_domain not in DOMAIN_SKILLS_MAP:
            # Detect from text
            if is_domain_compatible('medical', text_full):
                detected_domain = 'medical'
            elif is_domain_compatible('commerce', text_full):
                detected_domain = 'commerce'
            elif is_domain_compatible('legal', text_full):
                detected_domain = 'legal'
            elif is_domain_compatible('agriculture', text_full):
                detected_domain = 'agriculture'
            elif is_domain_compatible('architecture', text_full):
                detected_domain = 'architecture'
            elif is_domain_compatible('arts', text_full):
                detected_domain = 'arts'
            elif is_domain_compatible('science', text_full):
                detected_domain = 'science'
            else:
                detected_domain = 'tech'

        # Ensure internship has domain updated
        intern.domain = detected_domain
        intern.save()

        # Find matching skills from text or pick default domain skills
        candidate_skills = DOMAIN_SKILLS_MAP.get(detected_domain, DOMAIN_SKILLS_MAP['tech'])
        
        assigned_skill_objs = []
        for sname in candidate_skills:
            if sname.lower() in text_full or len(assigned_skill_objs) < 3:
                skill_obj, _ = Skill.objects.get_or_create(
                    name=sname,
                    defaults={'category': detected_domain.title(), 'description': f'{sname} skill definition.'}
                )
                assigned_skill_objs.append(skill_obj)
            if len(assigned_skill_objs) >= 5:
                break

        if assigned_skill_objs:
            intern.required_skills.set(assigned_skill_objs)
            updated_count += 1

    print(f"[SUCCESS] Successfully enriched {updated_count} internships with required skills!")
    print(f"[VERIFY] Internships with skills now: {Internship.objects.filter(required_skills__isnull=False).distinct().count()}")

if __name__ == '__main__':
    enrich_all_internships()
