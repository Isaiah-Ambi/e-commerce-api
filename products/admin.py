from django.contrib import admin

from .models import Product
from cart.models import Cart


admin.site.register(Product)
admin.site.register(Cart)

