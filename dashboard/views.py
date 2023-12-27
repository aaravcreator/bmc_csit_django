from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
# Create your views here.
def dashboard(request):

    
    '''
    We list the person in the dashboard
    '''
    person_list = Person.objects.all()
    context = {
        'person_list':person_list,
    }
    return render(request,'dashboard/dash.html',context)

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
