from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
  return HttpResponse("<h1>로그인 페이지</h1>")

def register(request):
  return HttpResponse("<h1>회원가입 페이지</h1>")

def logout(request):
  return HttpResponse("<h1>로그아웃 페이지</h1>")