"""Admin setup for the checkout models"""
from django.contrib import admin
from .models import Order, OrderLineItem, Coupon


class OrderLineItemAdminInline(admin.TabularInline):
    """Admin setup for the OrderLineItem model
    Tabular Inline allows admin to edit line items
    inside the Order model"""
    model = OrderLineItem
    # Read Only Fields
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Admin setup for the Order model"""
    # Inlines creates the ability to edit models
    # on the same page as a parent model
    inlines = (OrderLineItemAdminInline,)

    # Read Only Fields
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    # Keep the order the same as the model
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    # Show only key items
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Most recent orders first
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon)
