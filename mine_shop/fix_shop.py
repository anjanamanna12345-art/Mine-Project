import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_shop.settings')
django.setup()

from shop.models import Product

updates = {
    "Classic Leather Oxfords": "https://images.pexels.com/photos/298864/pexels-photo-298864.jpeg?auto=compress&cs=tinysrgb&w=800"
}

for name, url in updates.items():
    items = Product.objects.filter(name=name)
    for item in items:
        item.image_url = url
        item.save()
print("Shop images updated to requested ones successfully!")
