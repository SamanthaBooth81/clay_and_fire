""" Favourites App Views """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from products.models import Products
from .models import Favourites
from products.views import product_details


@login_required
def favourites_view(request):
    """
    The view to display the users favourited items
    """
    favourites_items_count = 0
    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourites_items = None
    else:
        favourites_items = all_favourites.products.all()
        favourites_items_count = all_favourites.products.all().count()

    if not favourites_items:
        messages.info(request, 'Your favourites list is empty!')

    template = 'favourites/favourites.html'
    context = {
        'favourites_items': favourites_items,
        'favourites_items_count': favourites_items_count
    }

    return render(request, template, context)


@login_required
def add_favourites(request, item_id):
    """View to add a product to favourites"""

    product = get_object_or_404(Products, pk=item_id)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)

    if product in favourites.products.all():
        messages.info(request, 'The product is already in your favourites!')
    else:
        favourites.products.add(product)
        messages.success(request, 'Product added to your favourites!')

    return redirect(reverse('product_details', args=[product.id]))


@login_required
def remove_favourites(request, item_id, redirect_from):
    """
    A view that will add a product item to favourites
    """
    product = get_object_or_404(Products, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.success(request, 'Product removed from favourites')
    else:
        messages.error(request, 'This product is not in your favourites!')

    if redirect_from == 'favourites':
        redirect_url = reverse('favourites')
    else:
        redirect_url = reverse('product_details', args=[product.id])

    return redirect(redirect_url)
