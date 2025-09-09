from ninja import Router
from ninja_jwt.authentication import JWTAuth
from .schemas import CartSchema
from products.schemas import ProductSchema
from .models import Cart
from typing import List

router = Router()

@router.get('/', response=List[ProductSchema], auth=JWTAuth())
def get_cart(request):
    user = request.auth
    cart, created = Cart.objects.get_or_create(user=user)

    print(cart.products.all(), created)
    return cart.products.all()
