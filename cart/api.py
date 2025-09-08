from ninja import Router
from .models import Cart, CartITem
from products.models import Product

router = Router()


@router.get('/')
def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = CartITem.objects.filter(cart=cart).select_related('product')
        return {
            'cart_id': cart.id,
            'items': [
                {
                    'product_id': item.product.id,
                    'product_name': item.product.name,
                    'quantity': item.quantity,
                    'price': item.product.price,
                } for item in items
            ]
        }
    return {'error': 'Authentication required'}, 401
