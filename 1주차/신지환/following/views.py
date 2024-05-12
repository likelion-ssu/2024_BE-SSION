from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def requestFollow(request) : 
    return HttpResponse("<h1>팔로우 요청화면</h1>")

def admitFollow(request) : 
    return HttpResponse("<h1>팔로우 승인화면</h1>")