from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_enroll(request):
    return HttpResponse("<h1>여기는 유저앱 중 등록하기</h1>"
                        "<h2>이름:  이메일:  전화번호: ...</h2>")
def user_select(request):
    return HttpResponse("<h1>여기는 유저앱 중 조회하기</h1>"
                        "<h2>신민경1  신민경2  신민경3  ... </h2>")
