"""Products App Admin"""
from django.contrib import admin
from .models import Products, Category


class ProductAdmin(admin.ModelAdmin):
    """Admin Panel display for Product Model"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Admin Panel display for Categories Model"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
