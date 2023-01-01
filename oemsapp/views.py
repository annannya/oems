from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from oemsapp.models import Employee
from oemsapp.serializers import EmployeesSerializer


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        # to get all the data from database
        employees = Employee.objects.all()
        # to map the json data from database to serializer to send back to the user
        employees_serializer = EmployeesSerializer(employees, many=True)
        # sending data in form of json response
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        # reading the data from user input
        employee_data = JSONParser().parse(request)
        # converting json into model serializer to save into database
        employees_serializer = EmployeesSerializer(data=employee_data)
        # check if user is already exist or not
        employees = Employee.objects.filter(Employee_Name=employee_data['Employee_Name'],
                                            Phone_No=employee_data['Phone_No'])
        # check user existence
        if employees.count() != 0:
            return JsonResponse("User is already Exist in our Application", safe=False)
        elif employees_serializer.is_valid():
            # saving the new data into database
            employees_serializer.save()
            return JsonResponse("User has been registered Successfully in Application", safe=False)
        return JsonResponse("Please Enter the correct Input", safe=False)
    elif request.method == 'PUT':
        #  note:- for update employee name and phone no. is mandatory
        # reading the input data from user
        employee_data = JSONParser().parse(request)
        # get the data by id to update
        employee = Employee.objects.get(Employee_ID=employee_data['Employee_ID'])
        # updating the user input data and creating the serializer
        employees_serializer = EmployeesSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse(employees_serializer.data['Employee_Name'] + "has been Updated Successfully in our "
                                                                             "application", safe=False)
        return JsonResponse("Please check the input")
    elif request.method == 'DELETE':
        # reading the data from user input
        employee_data = JSONParser().parse(request)
        name = employee_data['Employee_Name']
        employee = Employee.objects.filter(Employee_Name=name, Phone_No=employee_data['Phone_No'])
        # check user existence
        if employee.count() == 0:
            return JsonResponse(name + " is not Exist in our Application")
        else:
            # delete the user
            employee.delete()
            return JsonResponse(name + " has been deleted Successfully", safe=False)


@csrf_exempt
def filterApi(request):
    if request.method == 'POST':
        # reading the data from user input
        employee_data = JSONParser().parse(request)
        # to get all the data from database
        employees = Employee.objects.all()
        # taking the parameter to be filtered
        if 'Employee_Name' in request.POST:
            employees = employees.filter(Employee_Name=employee_data['Employee_Name'])
        if 'Location' in request.POST:
            employees = employees.filter(Location=employee_data['Location'])
        # serializing the data from the database
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


def index(request):
    return render(request, "index.html")


def all_employee(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps

    }
    print(context)
    return render(request, "all_employee.html", context)


def add_employee(request):
    return render(request, "add_employee.html")


def remove_employee(request):
    return render(request, "remove_employee.html")


def filter_employee(request):
    return render(request, "filter_employee.html")
