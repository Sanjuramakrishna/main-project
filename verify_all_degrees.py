import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from profiles.models import Degree, UserProfile
from ai_services.career_prediction.rf_knn_engine import predict_top_careers

degrees = list(Degree.objects.all())
print(f"--- VERIFYING RECOMMENDATION SYSTEM FOR ALL {len(degrees)} DEGREES ---")

for d in degrees:
    test_profile = UserProfile(degree=d)
    recs = predict_top_careers(test_profile, [])
    top_1_title = recs[0]['career'].title if recs else "None"
    top_5_titles = [r['career'].title for r in recs[:5]]
    print(f"Degree Code: {d.code:<10} | Name: {d.name:<15} | Total Recs: {len(recs)} | Top Match: {top_1_title}")
    print(f"   Top 5: {top_5_titles}")
    print("-" * 80)
