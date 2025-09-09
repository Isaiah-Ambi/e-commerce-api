from ninja import Schema, ModelSchema
from .models import Cart
from products.schemas import ProductSchema
from typing import List



class CartSchema(ModelSchema):
    class Meta:
        model = Cart
        exclude = ['id']
