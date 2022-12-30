from rest_framework import serializers
from oemsapp.models import Employee


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('Employee_ID', 'Employee_Name', 'Department', 'Joining', 'Location', 'Salary', 'Bonus', 'Role',
                  'Phone_No')
