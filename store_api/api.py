from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

from products.api import router as products_router
from cart.api import router as cart_router

api = NinjaExtraAPI()


api.add_router('/products/', products_router)
api.add_router('/cart/', cart_router)

api.register_controllers(NinjaJWTDefaultController)