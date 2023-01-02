import uuid

from django.db import models


# Create your models here.
class Employee(models.Model):
    Employee_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Employee_Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Joining = models.DateField()
    Location = models.CharField(max_length=50)
    Salary = models.IntegerField(default=0)
    Bonus = models.IntegerField(default=0)
    Role = models.CharField(max_length=50)
    Phone_No = models.CharField(max_length=10)
