from ninja import Router, Schema
from cart.models import Cart, CartITem
from .models import Product

router = Router()


@router.get('/')
def list_products(request):
    products = Product.objects.all()
    return {'products': list(products.values())}