from django import forms
from .models import Item


class ItemForm(forms.ModelForm): #dot notation
    class Meta: #inner class
        model = Item
        fields = ['name', 'done']

#to make sure we can use this form, import it in views.py (and any relevant tests)