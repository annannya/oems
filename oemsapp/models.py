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

    def __init__(self, Employee_Name, Department, Joining, Location, Salary, Bonus, Role, Phone_No):
        models.Model.__init__(self)
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Joining = Joining
        self.Location = Location
        self.Salary = Salary
        self.Bonus = Bonus
        self.Role = Role
        self.Phone_No = Phone_No

    def __init__(self, Employee_ID, Employee_Name, Department, Joining, Location, Salary, Bonus, Role, Phone_No):
        models.Model.__init__(self)
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Joining = Joining
        self.Location = Location
        self.Salary = Salary
        self.Bonus = Bonus
        self.Role = Role
        self.Phone_No = Phone_No



