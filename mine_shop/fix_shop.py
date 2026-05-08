import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_shop.settings')
django.setup()

from shop.models import Product

updates = {
    "Sambalpuri Handloom Saree": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800",
    "Classic Leather Oxfords": "https://images.unsplash.com/photo-1614252209825-980f82635bc1?w=800",
    "Premium Leather Tote Bag": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800"
}

for name, url in updates.items():
    items = Product.objects.filter(name=name)
    for item in items:
        item.image_url = url
        item.save()
print("Shop images updated successfully!")
