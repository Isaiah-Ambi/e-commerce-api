from django.shortcuts import render
from .models import Product
from cart.models import Cart

# Create your views here.


def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def search_products(request, query):
    results = Product.objects.filter(name__contains=f"{query}")
    return render(request, 'products/list.html', {'products': results})

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/detail.html', {'product': product})