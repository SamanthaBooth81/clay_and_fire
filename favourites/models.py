"""Favourites App Models"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Products


class Favourites(models.Model):
    """Favourites model so the user can save items to their favourites"""

    products = models.ManyToManyField(Products, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return object string"""
        return f"{self.username}'s Favourites"