# from django.db import models
# from django.forms import fields
from django import forms
from .models import Product

class ProductImage(forms.ModelForm):
    class Meta:
        models = Product
        fields = [
            'productName',
            'productDescription',
            'productImage',
            'price',
            'manufacturer',
            'category'
        ]
