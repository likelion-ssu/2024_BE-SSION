from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def followingList(request):
	return HttpResponse("<h1>✨followingList✨</h1><ol><li>🤓<li>🥸<li>🥴</ol>")
def follow(request):
	return HttpResponse("<h1>팔로팔로미</h1>")
