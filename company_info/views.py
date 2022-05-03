"""Company Info Views"""
from django.shortcuts import render


def faq_page(request):
    """View to return index page"""
    return render(request, 'help/faqs.html')
