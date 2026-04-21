from django.db import models

class AreaModel(models.Model):
    id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    lead = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='area_lead')
    
    @property
    def employee_count(self):
        return EmployeeModel.objects.filter(team__department__area=self).count()
    
    def __str__(self):
        return f"Creation Date: {self.creation_date} / ID: {self.id} / Area: {self.name} / Email Address: {self.email} / Employees: {self.employee_count}"
    
class DepartmentModel(models.Model):
    id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    lead = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='department_lead')

    @property
    def employee_count(self):
        return EmployeeModel.objects.filter(team__department=self).count()
    
    def __str__(self):
        return f"ID: {self.id} / Creation Date: {self.creation_date} / Deparment: {self.name} / email: {self.email} / Employees: {self.employee_count} / Area: {self.area.name}"
    
class TeamModel(models.Model):
    
    id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    lead = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='team_lead')
    
    @property
    def employee_count(self):
        return EmployeeModel.objects.filter(team=self).count()
    
    def __str__(self):
        return f"ID: {self.id} / Creation Date: {self.creation_date} / Team: {self.name} / Email Address: {self.email} / Employees: {self.employee_count} / Department {self.department.name}"
    
class EmployeeModel(models.Model):
    id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20) # "54 11 1234-5678"
    mobile = models.CharField(max_length=20) # "54 11 1234-5678"
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"ID: {self.id} / Creation Date: {self.creation_date} / Employee: {self.name} {self.surname} / Role: {self.role.name} / Email Address: {self.email} / Phone Number: {self.phone} / Team: {self.team.name}"

class RoleModel(models.Model):
    id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return f"ID: {self.id} / Creation Date: {self.creation_date} / Role: {self.name} / Description: {self.description}"