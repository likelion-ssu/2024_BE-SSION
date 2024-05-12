from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addArticle(request):
    return HttpResponse("<h1>게시물 추가 페이지</h1>")

def verifyArticle(request):
    return HttpResponse("<h1>게시물 확인 페이지</h1>")
