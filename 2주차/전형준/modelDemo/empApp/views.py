from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def renderEmployees(request):
    employees = Employee.objects.all() #Employee 라는 모델 클래스에 있는 모든 오브젝트들을 가져온다
    empDict = {'employees': employees}
    return render(request, 'employees.html', context=empDict)