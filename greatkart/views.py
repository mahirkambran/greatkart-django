from django.shortcuts import render
from store.models import Product, ReviewRating


def home(request):

    products = Product.objects.all().filter(is_available=True).order_by('created_date')  # Fetch latest 8 products for

    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)  # Example: Fetch reviews for the first product

    context = {
        'products' : products,
        'reviews' : reviews,
    }

    return render(request ,'home.html',context)