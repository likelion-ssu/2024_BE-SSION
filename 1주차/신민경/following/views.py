from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def following(request):
    return HttpResponse("<h1>여기는 팔로잉앱</h1>")
def following_loading(request):
    return HttpResponse("<h1>...로딩중...</h1>")