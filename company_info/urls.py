"""Company info urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq_page, name='faq'),
    path('shipping-returns/', views.shipping_returns, name='shipping-returns'),
    path('about-us/', views.about_us, name='about-us'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('contact-us/', views.contact, name='contact'),
]
