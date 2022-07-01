"""Checkout urls"""
from django.urls import path
from . import views


urlpatterns = [
    path('favourites/', views.favourites_view, name='favourites'),
    path('add_favourites/<item_id>/',
         views.add_favourites, name='add_favourites'),
]
