from django import forms
from .models import Buyer,Unit,MachineType

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter buyer name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter buyer email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter buyer address'}),
        }

class UnitForm(forms.ModelForm):
    UNIT_TYPE_CHOICES = [
        ('In House', 'In-House'),
        ('Out Side', 'Out Side'),

    ]
    
    type = forms.ChoiceField(
        choices=UNIT_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control select2'})
    )

    class Meta:
        model = Unit
        fields = ['name', 'type', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Unit name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Unit Location'}),
        }

class MachineTypeForm(forms.ModelForm):
    class Meta:
        model = MachineType
        fields = ['type']
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Machine Type'}),

        }
