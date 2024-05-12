"""
URL configuration for instaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as user_views
from article import views as article_views
from following import views as following_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.login),
    path('signUp/', user_views.signUp),
    path('addArticle/', article_views.addArticle),
    path('verifyArticle/', article_views.verifyArticle),
    path('requestFollo/', following_views.requestFollow),
    path('approveFollow/', following_views.approveFollow),
]
