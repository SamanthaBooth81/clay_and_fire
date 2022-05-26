"""Product App Forms"""
from django import forms
from .models import Products, Category, Review


class AddProductForm(forms.ModelForm):
    """Admin Add product form. Code from Boutique Ado"""

    class Meta:
        """Include all Product Model fields"""
        model = Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # Display categories by their friendly names
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """Rating and Review Form"""
    class Meta:
        """Form model and Fields"""
        model = Review
        fields = ['rating', 'review']
