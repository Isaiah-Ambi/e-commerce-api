from ninja import ModelSchema
from .models import Product

class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        exclude = ['id', 'stock']