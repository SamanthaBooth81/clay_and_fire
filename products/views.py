"""Products app views"""
from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.


def all_products(request):
    """View to show all products for  sale and sort/filter items"""
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
