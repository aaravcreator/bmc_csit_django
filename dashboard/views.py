from django.shortcuts import render,redirect
from .forms import PersonForm,LoginForm
from .models import Person
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import JsonResponse
import time
def productView(request):
    data = [
  {
    "name": "Widget A",
    "markedPrice": 25.0,
    "salePrice": 19.99,
    "shopName": "Tech Emporium"
  },
  {
    "name": "Gadget X",
    "markedPrice": 45.0,
    "salePrice": 39.99,
    "shopName": "Electro Depot"
  },
  {
    "name": "Super Gizmo",
    "markedPrice": 30.0,
    "salePrice": 24.99,
    "shopName": "Innovation Hub"
  },
  {
    "name": "Tech Marvel",
    "markedPrice": 60.0,
    "salePrice": 49.99,
    "shopName": "Digital Haven"
  }
]
    time.sleep(5)

    return JsonResponse(data,safe=False)

def loginPage(request):
    login_form = LoginForm()
    error = None
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            print(username)
            print(password)
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('dashboard:dashboardPage')
            else:
                error = "Username / Password Error"

    context = {
        'login_form':login_form,
        'error':error
    }
    return render(request,'dashboard/login.html',context)

def logoutPage(request):
    '''
    logs the user out of the system
    ''' 
    logout(request)
    return redirect('dashboard:login')

@login_required()
def dashboard(request):

    '''
    We list the person in the dashboard
    '''
    search_key = request.GET.get('searchkey')
    if search_key is not None and search_key is not "":
        person_list = Person.objects.filter(created_by = request.user,name__icontains=search_key).order_by("-updated")
    # person_list = Person.objects.all().order_by("-updated")
    else:
        person_list = Person.objects.filter(created_by = request.user).order_by("-updated")
    context = {
        'person_list':person_list,
    }
    return render(request,'dashboard/dash.html',context)

@login_required()
def createPerson(request):
    person_form = PersonForm()
    if request.method == "POST":

        person_form = PersonForm(request.POST,request.FILES)
        if person_form.is_valid():
            print('form valid')
            ''' We assign the user here who made 
            the request to create the person obj here'''
            person_obj = person_form.save(commit=False) 
            person_obj.created_by = request.user
            person_obj.save()
            print('now redirecting')
            return redirect('dashboard:dashboardPage')

    context = {
        'person_form':person_form
    }
    return render(request,'dashboard/createperson.html',context)
@login_required()
def updatePerson(request,person_id):
    person = Person.objects.get(id=person_id)
    person_form = PersonForm(instance=person)

    if request.method == 'POST':
        person_form = PersonForm(request.POST,request.FILES,instance=person)
        if person_form.is_valid():
            person_form.save()
            return redirect('dashboard:dashboardPage')
    context = {
        'person':person,
        'person_form':person_form
    }
    return render(request,'dashboard/personupdate.html',context)

def deletePerson(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect('dashboard:dashboardPage')
