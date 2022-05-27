"""Products App Admin"""
from django.contrib import admin
from .models import Products, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """Admin Panel display for Product Model"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Admin Panel display for Categories Model"""
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """Admin Panel display for Product Model"""
    list_display = (
        'product',
        'user',
        'rating',
        'review',
        'status',
    )


admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
