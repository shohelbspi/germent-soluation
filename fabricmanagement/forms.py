from django import forms
from .models import Buyer,Unit,MachineType,Machine,YarnCount,YarnType

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


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'machine_no', 'unit', 'machine_name', 'machine_brand', 'machine_gauge',
            'machine_type', 'machine_dia', 'no_of_feeder', 'rotation_per_minute', 
            'accuracy', 'production_capacity_per_day', 'is_active'
        ]
        
        widgets = {
            'machine_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'machine_name': forms.TextInput(attrs={'class': 'form-control'}),
            'machine_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'machine_gauge': forms.TextInput(attrs={'class': 'form-control'}),
            'machine_type': forms.Select(attrs={'class': 'form-control'}),
            'machine_dia': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_feeder': forms.NumberInput(attrs={'class': 'form-control'}),
            'rotation_per_minute': forms.NumberInput(attrs={'class': 'form-control'}),
            'accuracy': forms.NumberInput(attrs={'class': 'form-control'}),
            'production_capacity_per_day': forms.NumberInput(attrs={'class': 'form-control'}),

            'is_active': forms.Select(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-control'}),
        }

class YarnCountForm(forms.ModelForm):
    class Meta:
        model = YarnCount
        fields = ['yarn_count']
        widgets = {
            'yarn_count': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Yarn Count'}),

        }

class YarnTypeForm(forms.ModelForm):
    class Meta:
        model = YarnType
        fields = ['yarn_type']
        widgets = {
            'yarn_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Yarn Type'}),

        }
