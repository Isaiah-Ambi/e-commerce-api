from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from products.models import Product
import requests
import os

# Create your views here.

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
        stripe_api_key = os.getenv("API_KEY")
        headers = {
            'Authorization': f'Bearer {stripe_api_key}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'amount': int(total_amount * 100),  # Amount in cents
            'currency': 'usd',
            'payment_method_types[]': 'card',
        }
        response = requests.post('https://api.stripe.com/v1/payment_intents', headers=headers, data=data)
        payment_intent = response.json()

        if response.status_code == 200:
            # Redirect to Stripe's hosted payment page or handle payment confirmation
            return redirect(f'/payment/{payment_intent["id"]}/')  # Example redirect URL
        else:
            error_message = payment_intent.get('error', {}).get('message', 'An error occurred while creating the payment intent.')
            return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_amount': total_amount, 'error': error_message})

    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_amount': total_amount})