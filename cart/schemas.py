from ninja import Schema

class CartItemSchema(Schema):
    product_id: int
    quantity: int
    price_per_item: float
    total_price: float
    added_at: str  # ISO format date-time string

class CartSchema(Schema):
    id: int
    user_id: int
    items: list[CartItemSchema] = []
    total_amount: float
    created_at: str  # ISO format date-time string
    updated_at: str  # ISO format date-time string

class AddToCartSchema(Schema):
    product_id: int
    quantity: int