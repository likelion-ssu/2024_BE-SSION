from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request) :
    return HttpResponse("<h1>로그인 페이지입니다!</h1>")

def register(request) : 
    return HttpResponse("<h1>걸어봐 위엄 라이크 어 라이🦁</h1>")

def profileedit(request) : 
    return HttpResponse("<h1>프로필 편집하는 곳</h1>")
    