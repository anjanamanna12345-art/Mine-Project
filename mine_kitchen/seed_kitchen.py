import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_kitchen.settings')
django.setup()

from kitchen.models import FoodItem

odia_foods = [
    {
        "name": "Pakhala Bhata",
        "description": "A traditional Odia dish made of cooked rice washed or lightly fermented in water, often served with roasted vegetables and fish.",
        "price": 150.00,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Pakhala_Bhata_%28Water_Rice%29.jpg/800px-Pakhala_Bhata_%28Water_Rice%29.jpg",
        "category": "Meals"
    },
    {
        "name": "Dalma",
        "description": "A healthy, flavorful Odia lentil dish cooked with vegetables like papaya, plantain, and pumpkin, tempered with panch phutana.",
        "price": 120.00,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Dalma_%28Odia_dish%29.jpg/800px-Dalma_%28Odia_dish%29.jpg",
        "category": "Meals"
    },
    {
        "name": "Chhena Poda",
        "description": "The classic dessert of Odisha, made with well-kneaded homemade fresh cheese (chhena), sugar, and baked until perfectly browned.",
        "price": 200.00,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Chhena_Poda.JPG/800px-Chhena_Poda.JPG",
        "category": "Desserts"
    }
]

for food_data in odia_foods:
    item, created = FoodItem.objects.get_or_create(name=food_data['name'], defaults=food_data)
    if created:
        print(f"Added {food_data['name']} successfully.")
    else:
        print(f"{food_data['name']} already exists.")
