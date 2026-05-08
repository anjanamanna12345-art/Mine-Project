import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_kitchen.settings')
django.setup()

from kitchen.models import FoodItem

updates = {
    "Pakhala Bhata": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Pakhala_01.jpg/960px-Pakhala_01.jpg",
    "Chhena Poda": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Bhubaneswar_Odia_Meetup_2013Jan29-23.JPG/960px-Bhubaneswar_Odia_Meetup_2013Jan29-23.JPG"
}

for name, url in updates.items():
    items = FoodItem.objects.filter(name=name)
    for item in items:
        item.image_url = url
        item.save()
print("Kitchen images updated to remove the woman and fix Chhena Poda successfully!")
