from django.db import models

class AreaModel(models.Model):
    area_id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    lead = models.CharField(max_length=50)
    
    def __str__(self):
        return f"ID: {self.area_id} / Area: {self.name}  / Lead: {self.lead}"
    
class DepartmentModel(models.Model):
    department_id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    lead = models.CharField(max_length=50)
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.department_id} / Department: {self.name} / Lead: {self.lead} / Area: {self.area}"
    
class TeamModel(models.Model):
    team_id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    lead = models.CharField(max_length=50)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.team_id} / Team: {self.name} / Department: {self.department} / Lead: {self.lead}"
    
class EmployeeModel(models.Model):
    employee_id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    role = models.ForeignKey("RoleModel", on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.employee_id} / Employee: {self.name} / Email Address: {self.email} / Phone Number: {self.phone_number} / Mobile Number: {self.mobile_number} / Role: {self.role} / Team: {self.team}"
    
class RoleModel(models.Model):
    role_id = models.IntegerField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return f"ID: {self.role_id} / Role: {self.name} / Description: {self.description}"