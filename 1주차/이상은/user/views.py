from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
	return HttpResponse("<h1>로그인하세요!!!</h1>")
def mypage(request):
	return HttpResponse("<h1>🦁</h1><h2>이름: 아기사자</h2><h2>어흥..</h2>")
