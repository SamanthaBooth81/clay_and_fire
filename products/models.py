"""Product models"""
from django.db import models

# Models from Code Institutes Boutique Ado Follow Along Project


class Category(models.Model):
    """Category model"""

    class Meta:
        """Removes extra 's' from Model name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """returns the products friendly name if one"""
        return self.friendly_name


class Products(models.Model):
    """Products model"""
    class Meta:
        """Removes extra 's' from Model name"""
        verbose_name_plural = 'Products'

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name