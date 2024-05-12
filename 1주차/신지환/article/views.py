from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def newPost(request) : 
    return HttpResponse("<h1>새 게시물 추가화면</h1>")
def checkPost(request) : 
    return HttpResponse("<h1>게시물 확인</h1>")
