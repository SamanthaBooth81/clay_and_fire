"""Order Form for checkout page"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """checkout order form"""
    class Meta:
        """form fields and model"""
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """Override init method to customise the form"""
        super().__init__(*args, **kwargs)

        # Use placeholders instead of form labels
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # set the auto focus to full_name field (first field)
        # so cursor starts here
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # iterate through the fields to add required *, placeholders,
        # remove labels and add a css class - REMOVE CLASS IF NOT USED!!!!!!
        for field in self.fields:
            # If statement to prevent an error as placeholder is
            # not required for 'country' dropdown box
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
