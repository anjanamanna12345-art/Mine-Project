import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_kitchen.settings')
django.setup()

from kitchen.models import FoodItem

updates = {
    "Pakhala Bhata": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800",
    "Dalma": "https://images.unsplash.com/photo-1548943487-a2e4b43b4850?w=800",
    "Chhena Poda": "https://images.unsplash.com/photo-1587314168485-3236d6710814?w=800"
}

for name, url in updates.items():
    items = FoodItem.objects.filter(name=name)
    for item in items:
        item.image_url = url
        item.save()
print("Kitchen images updated successfully!")
