from django import forms
from company_structure.models import Area, Department, Team, Employee, Role

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ("id", "name", "email", "lead")
        widgets = {
            "id": forms.NumberInput(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "lead": forms.Select(attrs={'class': 'form-control'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("id", "name", "email", "area", "lead")
        widgets = {
            "id": forms.NumberInput(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "area": forms.Select(attrs={'class': 'form-control'}),
            "lead": forms.Select(attrs={'class': 'form-control'}),
        }
    
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("id", "name", "email", "department", "lead")
        widgets = {
            "id": forms.NumberInput(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "department": forms.Select(attrs={'class': 'form-control'}),
            "lead": forms.Select(attrs={'class': 'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("id", "name", "surname", "role", "email", "phone", "mobile", "team")
        widgets = {
            "id": forms.NumberInput(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "surname": forms.TextInput(attrs={'class': 'form-control'}),
            "role": forms.Select(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'}),
            "mobile": forms.TextInput(attrs={'class': 'form-control'}),
            "team": forms.Select(attrs={'class': 'form-control'}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ("id", "name")
        widgets = {
            "id": forms.NumberInput(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'}),
        }