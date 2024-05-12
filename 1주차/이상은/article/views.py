from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def like(request):
	return HttpResponse("<h1>좋아요~~~👍</h1>")
def newArticle(request):
	return HttpResponse("<h1>안녕하세요</h1><h2>안녕하세요</h2>")