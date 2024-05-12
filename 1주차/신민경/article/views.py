from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def article(request):
    return HttpResponse("<h1>여기는 article앱</h1>")
def article_enroll(request):
    return HttpResponse("<h1>여기는 article앱 중 등록하기</h1>"
                        "<h2>게시물 = 사진 + 코멘트 + 태그</h2>")