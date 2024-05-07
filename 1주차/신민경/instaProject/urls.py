"""
URL configuration for instaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from user import views as userView
from article import views as articleView
from following import views as followingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', userView.user_enroll),
    path('userselect/', userView.user_select),
    path('article/', articleView.article),
    path('articleenroll', articleView.article_enroll),
    path('following/',followingView.following),
    path('followingloading', followingView.following_loading),
]
