import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_shop.settings')
django.setup()

from shop.models import Category, Product

# Categories
fashion_cat, _ = Category.objects.get_or_create(name="Fashion", description="Apparel and clothing.")
shoes_cat, _ = Category.objects.get_or_create(name="Footwear", description="Shoes and footwear.")
accessories_cat, _ = Category.objects.get_or_create(name="Accessories", description="Bags, belts, and more.")

products = [
    {
        "category": fashion_cat,
        "name": "Sambalpuri Handloom Saree",
        "description": "Authentic traditional Sambalpuri saree with intricate Ikat weave patterns.",
        "price": 3500.00,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Sambalpuri_Saree.jpg/800px-Sambalpuri_Saree.jpg",
        "stock": 10
    },
    {
        "category": shoes_cat,
        "name": "Classic Leather Oxfords",
        "description": "Premium genuine leather formal shoes for men. Perfect for any formal occasion.",
        "price": 2500.00,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Castellano_Shoes.jpg/800px-Castellano_Shoes.jpg",
        "stock": 15
    },
    {
        "category": accessories_cat,
        "name": "Premium Leather Tote Bag",
        "description": "Spacious and durable genuine leather tote bag for everyday use.",
        "price": 1800.00,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Leather_tote_bag.jpg/800px-Leather_tote_bag.jpg",
        "stock": 20
    }
]

for product_data in products:
    item, created = Product.objects.get_or_create(name=product_data['name'], defaults=product_data)
    if created:
        print(f"Added {product_data['name']} successfully.")
    else:
        print(f"{product_data['name']} already exists.")
