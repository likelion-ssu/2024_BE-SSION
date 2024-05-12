from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("<h1>로그인 페이지</h1>")

def signUp(request):
    return HttpResponse("<h1>회원가입 페이지</h1>")