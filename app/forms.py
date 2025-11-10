from django import forms
from .models import Product
from django.forms import TextInput, NumberInput

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = '__all__'
    labels = {
      'product_id': 'Product ID',
      'name': 'Name',
      'sku': 'SKU',
      'price': 'Price',
      'quantity': 'Quantity',
      'supplier': 'Supplier',
    }
    widgets = {
      'product_id': forms.NumberInput(
        attrs={'placeholder': 'e.g. 1', 'class': 'form-control'}),
      'name': TextInput(
        attrs={'placeholder': 'e.g. Shirt', 'class': 'form-control'}),
      'sku': TextInput(
        attrs={'placeholder': 'e.g. S12345', 'class': 'form-control'}),
      'price': NumberInput(
        attrs={'placeholder': 'e.g. 19.99', 'class': 'form-control'}),
      'quantity': NumberInput(
        attrs={'placeholder': 'e.g. 1', 'class': 'form-control'}),
      'supplier': TextInput(
        attrs={'placeholder': 'e.g. ABC corp', 'class': 'form-control'}),

    }