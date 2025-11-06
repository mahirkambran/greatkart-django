#!/usr/bin/env python3
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greatkart.settings')
django.setup()

from store.models import Product
from category.models import Category

print("Testing database connection...")
print(f"Products count: {Product.objects.count()}")
print(f"Categories count: {Category.objects.count()}")

# Try to get some products
products = Product.objects.all()[:5]
print(f"First 5 products: {list(products)}")

print("Database test completed!")
