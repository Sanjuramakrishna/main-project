import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from careers.models import Career
from opportunities.models import JobOpportunity, Internship, GovernmentExam, Course
from profiles.models import Degree
from ai_services.career_prediction.rf_knn_engine import get_degree_cluster, is_career_domain_compatible
from opportunities.views import is_domain_compatible

degrees = list(Degree.objects.all())
print(f"Total degrees: {len(degrees)}")

careers = list(Career.objects.all())
jobs = list(JobOpportunity.objects.all())
internships = list(Internship.objects.all())
exams = list(GovernmentExam.objects.all())
courses = list(Course.objects.all())

print(f"Total in DB - Careers: {len(careers)}, Jobs: {len(jobs)}, Internships: {len(internships)}, Exams: {len(exams)}, Courses: {len(courses)}\n")

for d in degrees:
    cluster = get_degree_cluster(d)
    c_count = len([c for c in careers if d in c.eligible_degrees.all() or is_career_domain_compatible(cluster, f"{c.title} {c.domain} {c.description}")])
    j_count = len([j for j in jobs if is_domain_compatible(cluster, f"{j.title} {getattr(j, 'domain', '')} {j.description}")])
    i_count = len([i for i in internships if is_domain_compatible(cluster, f"{i.title} {getattr(i, 'eligibility', '')} {i.description}")])
    e_count = len([e for e in exams if is_domain_compatible(cluster, f"{e.exam_name} {e.domain} {e.syllabus_summary}")])
    crs_count = len([cr for cr in courses if is_domain_compatible(cluster, f"{cr.title} {getattr(cr, 'provider', '')} {cr.description}")])
    print(f"Degree: {d.code:<15} Cluster: {cluster:<12} -> Careers: {c_count:<3}, Jobs: {j_count:<3}, Internships: {i_count:<3}, Exams: {e_count:<3}, Courses: {crs_count:<3}")
