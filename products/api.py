from ninja import Router, Schema
from cart.models import Cart
from .models import Product
from .schemas import ProductSchema
from typing import List

router = Router()


@router.get('/', response=List[ProductSchema])
def list_products(request):
    products = Product.objects.all()
    return {'products': list(products.values())}


@router.get('/search/{query}', response=List[ProductSchema])
def search_products(request, query: str):
    results = Product.objects.filter(name__contains=f"{query}")
    return results
