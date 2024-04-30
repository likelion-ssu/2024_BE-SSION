from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def following_list(request):
  return HttpResponse("<h1>팔로잉 목록 페이지</h1>")