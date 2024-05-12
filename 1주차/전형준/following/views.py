from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def requestFollow(request):
    return HttpResponse("<h1>팔로우 요청 페이지</h1>")

def approveFollow(request):
    return HttpResponse("<h1>팔로우 승인 페이지</h1>")