"""Company Info Views"""
from django.shortcuts import render


def faq_page(request):
    """View to return FAQ's page"""
    return render(request, 'help/faqs.html')


def shipping_returns(request):
    """View to return shipping and returns info page"""
    return render(request, 'help/shipping-returns.html')


def about_us(request):
    """View to return shipping and returns info page"""
    return render(request, 'company/about-us.html')
