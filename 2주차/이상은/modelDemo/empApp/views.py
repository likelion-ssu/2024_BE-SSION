from django.shortcuts import render
from empApp.models import Employee
# Create your views here.
def renderEmployee(request):
	employees = Employee.objects.all()
	empDict = {'employees':employees}
	return render(request, 'employees.html', empDict)