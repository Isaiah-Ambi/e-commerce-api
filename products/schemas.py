from ninja import Schema

class ProductSchema(Schema):
    id: int
    name: str
    description: str
    price: float
    stock: int