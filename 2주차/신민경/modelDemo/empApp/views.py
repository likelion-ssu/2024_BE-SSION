from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def renderEmployees(request) :
    employees = Employee.objects.all() # select * from emp_employee와 같은 역할
    empDict = {'employees': employees}
    return render(request, 'employees.html', empDict)