from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from products.models import Product
import requests
import os

import stripe

stripe.api_key = os.getenv("API_KEY")

MY_DOMAIN = "http://localhost:8000"

def get_user_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.products.all()
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    cart.products.add(product)
    return redirect('get_user_cart')

def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    cart.products.remove(product)
    return redirect('get_user_cart')

def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.products.clear()
    return redirect('get_user_cart')

def cart_item_count(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return cart.products.count()

def cart_total_price(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total = sum(product.price for product in cart.products.all())
    return total


def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.products.all()
    total_amount = sum(item.price for item in cart_items)  # Assuming 'price' is a field in Product model

    if request.method == 'POST':
        # Create a payment intent with Stripe
        check_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1Qx8zN4dM1hku9cAjvR9JJbm', # Replace with your actual price ID
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=MY_DOMAIN + 'cart/success/',
            cancel_url=MY_DOMAIN + 'cart/cancel/',
        )
        return redirect(check_session.url, code=303)

    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_amount': total_amount})

def checkout_success(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.products.clear()  # Clear the cart after successful payment
    return render(request, 'cart/success.html')

def checkout_cancel(request):
    return render(request, 'cart/cancel.html')