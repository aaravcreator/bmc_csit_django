from django.shortcuts import HttpResponse,render
from random import randint
from dashboard.models import Person,Partner

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
    partners = Partner.objects.all()
    if request.method == "GET":
        name = request.GET.get('name')
        # address = request.GET.get('address')
        gender = request.GET.get('gender')
        print(name)

        if (name is not None and name is not "" ) :
            if (gender is not None and gender is not ""):
                person_list = Person.objects.filter(name__icontains=name,gender=gender)
            else:
                person_list = Person.objects.filter(name__icontains=name)
        elif(gender is not None and gender is not ''):
            person_list = Person.objects.filter(gender=gender)
        else:
            person_list = Person.objects.all()

    context = {
        # 'movie_list' :['ANIMAL','LEO','JAWAN','JAILER'],
        'person_list':person_list,
        'partner_list':partners,
        'favourite_movie':"LEO"
    }
    return render(request,'mypage.html',context)


