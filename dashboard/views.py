from django.shortcuts import render,redirect
from .forms import PersonForm,LoginForm
from .models import Person
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.





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
    person_list = Person.objects.all()
    context = {
        'person_list':person_list,
    }
    return render(request,'dashboard/dash.html',context)

@login_required()
def createPerson(request):
    person_form = PersonForm()
    if request.method == "POST":

        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            print('form valid')
            person_form.save()
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
        person_form = PersonForm(request.POST,instance=person)
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
