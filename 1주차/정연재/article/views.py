from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def article_list(request):
  return HttpResponse("<h1>게시글 목록 페이지</h1>")

def article_detail(request):
  return HttpResponse("<h1>게시글 상세 페이지</h1>")

def article_create(request):
  return HttpResponse("<h1>게시글 생성 페이지</h1>")