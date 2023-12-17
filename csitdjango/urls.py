"""
URL configuration for csitdjango project.

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

from django.shortcuts import HttpResponse,render
from random import randint

def index(request):
    # return HttpResponse("This is from Django")
    username = request.GET.get('username') 
    password = request.GET.get('password') 
    checked = request.GET.get('checked')

    context = {
        'username_data':username,
        'password_data':password,
        'checked_data':checked
    }
    return render(request,'base.html',context)

def summer(request,a,b):
    return HttpResponse(f"The sum is {a+b}")

def multiplication(request):
    username = request.GET.get('user')
    address = request.GET.get('address')
    return HttpResponse(f"Username is {username} and he/she is from {address}")

def homePage(request):
    return render(request,'home.html')


def mypage(request):
    context = {
        'movie_list' :['ANIMAL','LEO','JAWAN','JAILER'],
        'favourite_movie':"LEO"
    }
    return render(request,'mypage.html',context)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mypage),
    path('sum/<str:a>/<str:b>/',summer,),
    path('queryparams/',multiplication),
    path('home/',homePage,)



]
