from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You need to add something to your cart first!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q5CZ9LZBXn2Dva69kbTaLF6F6rs3LbKwTLfcDxhvTWuCoU83LzU2FvknBNV6ci7rM2hirggv9No0zyQQXT9wKGX00VHcPbrr5',
        'client_secret': 'test secret key',
    }

    return render(request, template, context)