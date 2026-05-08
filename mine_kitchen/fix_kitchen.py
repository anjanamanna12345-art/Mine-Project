import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_kitchen.settings')
django.setup()

from kitchen.models import FoodItem

updates = {
    "Pakhala Bhata": "https://img.youtube.com/vi/pdgXnhEDV9s/maxresdefault.jpg",
    "Dalma": "https://img.youtube.com/vi/BaeOKMhYwLQ/maxresdefault.jpg",
    "Chhena Poda": "https://img.youtube.com/vi/hV4VhLtofWQ/maxresdefault.jpg"
}

for name, url in updates.items():
    items = FoodItem.objects.filter(name=name)
    for item in items:
        item.image_url = url
        item.save()
print("Kitchen images updated to requested ones successfully!")
