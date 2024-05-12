from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def article(request):
  return HttpResponse("<h1>관심있는 article를 찾아보세요!")
