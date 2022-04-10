"""Checkout Views"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """Checkout Form View"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, 'You currently have no items in the shopping bag')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'STRIPE_PUBLIC_KEY': 'pk_test_51Kn1vYEKAndUjYSKJu7wWV9kizg5RxPiMii1Oji9C3z1YWj9CoGDepToNr9NELAgt9gUrKIffeuZfCnglUjdRh2Q00Zel5yVzW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
