from ninja import Router
from ninja_jwt.authentication import JWTAuth
from .schemas import CartSchema
from products.schemas import ProductSchema
from .models import Cart
from products.models import Product
from typing import List

router = Router()

@router.get('/', response=List[ProductSchema], auth=JWTAuth())
def get_cart(request):
    user = request.auth
    cart, created = Cart.objects.get_or_create(user=user)

    print(cart.products.all(), created)
    return cart.products.all()

@router.get('/add/{id}', response=List[ProductSchema], auth=JWTAuth())
def add_to_cart(request, id: int):
    user = request.auth
    cart, created = Cart.objects.get_or_create(user=user)
    product = Product.objects.get(pk=id)
    cart.products.add(product)
    products = cart.products.all()
    return products

@router.delete('/remove/{id}', response=List[ProductSchema], auth=JWTAuth())
def remove_from_cart(request, id: int):
    user = request.auth
    cart = Cart.objects.get(user=user)
    product = Product.get(pk=id)
    Cart.products.remove(product)
    products = cart.products.all()
    return products


