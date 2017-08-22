from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    favorite_products = []
    #display rank attribute used to denote which items end up in which row in bootstrap
    for r in Product.objects.values_list('display_rank', flat=True).distinct():
        x = Product.objects.filter(favorite=True, display_rank=r)
        favorite_products.append(x)
    return render(request, 'store_products/home.html', {'products': favorite_products})