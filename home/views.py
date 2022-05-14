"""Home Views"""
from django.shortcuts import render


def index(request):
    """View to return index page"""
    return render(request, 'home/index.html')


def handel_404(request, *args, **argv):
    """404 error page"""
    return render(request, 'home/404.html')
