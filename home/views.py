"""Home Views"""
from django.shortcuts import render


def index(request):
    """View to return index page"""
    return render(request, 'home/index.html')


def handel_404(request, *args, **argv):
    """View to return 404 error page if page does not exists"""
    return render(request, 'home/404.html')
