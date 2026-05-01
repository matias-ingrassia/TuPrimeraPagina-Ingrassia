from django import forms
from company_structure.models import AreaModel, DepartmentModel, TeamModel, EmployeeModel, RoleModel

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = ("area_id", "name", "lead")
        widgets = {
            "area_id":      forms.NumberInput   (attrs={'class': 'form-control'}),
            "name":         forms.TextInput     (attrs={'class': 'form-control'}),
            "lead":         forms.TextInput     (attrs={'class': 'form-control'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields = ("department_id", "name", "lead", "area")
        widgets = {
            "department_id":forms.NumberInput   (attrs={'class': 'form-control'}),
            "name":         forms.TextInput     (attrs={'class': 'form-control'}),
            "lead":         forms.TextInput     (attrs={'class': 'form-control'}),
            "area":         forms.TextInput     (attrs={'class': 'form-control'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = TeamModel
        fields = ("team_id", "name", "lead", "department")
        widgets = {
            "team_id":      forms.NumberInput   (attrs={'class': 'form-control'}),
            "name":         forms.TextInput     (attrs={'class': 'form-control'}),
            "lead":         forms.TextInput     (attrs={'class': 'form-control'}),
            "department":   forms.TextInput     (attrs={'class': 'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ("employee_id", "name", "role", "email", "phone_number", "mobile_number", "team")
        widgets = {
            "employee_id":  forms.NumberInput   (attrs={'class': 'form-control'}),
            "name":         forms.TextInput     (attrs={'class': 'form-control'}),
            "role":         forms.TextInput     (attrs={'class': 'form-control'}),
            "email":        forms.EmailInput    (attrs={'class': 'form-control'}),
            "phone_number": forms.TextInput     (attrs={'class': 'form-control'}),
            "mobile_number":forms.TextInput     (attrs={'class': 'form-control'}),
            "team":         forms.TextInput     (attrs={'class': 'form-control'}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = RoleModel
        fields = ("role_id", "name", "description")
        widgets = {
            "role_id":      forms.NumberInput   (attrs={'class': 'form-control'}),
            "name":         forms.TextInput     (attrs={'class': 'form-control'}),
            "description":  forms.Textarea      (attrs={'class': 'form-control'}),
        }