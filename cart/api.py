from ninja import Router
from ninja_jwt.authentication import JWTAuth
from .schemas import CartSchema, AddToCartSchema
from .models import Cart, CartItem

router = Router()

def get_cart_for_user(user):
    # Placeholder function to retrieve cart for a user
    cart = Cart.objects.filter(user=user).first()
    
    if not cart:
        cart = Cart.objects.create(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    return cart_items

@router.get('/', response=CartSchema, auth=JWTAuth())
def get_cart(request):
    """
    Retrieve the current user's cart.
    """
    user = request.auth
    cart = get_cart_for_user(user)
    return cart

