"""Shopping Bag Views"""
from django.shortcuts import render


def view_bag(request):
    """View to return the shopping bag page"""
    return render(request, 'bag/bag.html')
