from django.db import models
from django.forms import fields
from django import forms
from .models import Product

class ProductImage(forms.ModelForm):
    class meta:
        models = Product
        fields = '__all_'
