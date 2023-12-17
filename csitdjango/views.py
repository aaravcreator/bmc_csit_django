from django.shortcuts import HttpResponse,render
from random import randint


def niceadmin(request):
    return render(request,'nice_admin.html')
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


