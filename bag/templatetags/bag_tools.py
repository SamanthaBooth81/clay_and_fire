"""Created to calculate subtotal in shopping bag.
Code from CI Boutique Ado Project"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """calculate subtotal in shopping bag"""
    return price * quantity
