from django import forms
from .models import Buyer

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter buyer name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter buyer email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter buyer address'}),
        }
