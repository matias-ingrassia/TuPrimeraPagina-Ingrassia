from django import forms
from company_structure.models import AreaModel

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = ("name", "area_id", "email", "employees")
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "area_id": forms.NumberInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "employees": forms.NumberInput(attrs={'class': 'form-control'}),
        }





class DepartamentoMedicoForm2(forms.Form):
    pass