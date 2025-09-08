from ninja import NinjaAPI, Form
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from cart.api import router as cart_router
from products.api import router as products_router
from ninja.security import HttpBearer

api = NinjaAPI()

# Register JWT endpoints (token obtain, refresh, verify, etc.)
# api.add_router("/auth/", NinjaJWTDefaultController().as_view(), tags=["auth"])

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}

@api.post("/token", auth=None)
def get_token(request, username: str = Form(...)):
    if username == "admin" and password == "admin":
        return {"token": "supersecret"}

api.add_router('/products/', products_router)
api.add_router('/cart/', cart_router)