from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def follow(request):
  return HttpResponse("<h1>팔로우 목록입니다</h1>")

def following(request):
  return HttpResponse("<h1>팔로우 수를 늘려보세요!</h1>")