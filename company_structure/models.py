from django.db import models

class AreaModel(models.Model):
    name = models.CharField(max_length=50)
    area_id = models.IntegerField(unique=True)
    employees = models.IntegerField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    
    def __str__(self):
        return f"Area: {self.name} / ID: {self.area_id} / Email: {self.email}"