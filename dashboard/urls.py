from django.urls import path
from .views import *


app_name = 'dashboard'


urlpatterns = [
    path('dashboard/',dashboard,name='dashboardPage'),
    path('createPerson/',createPerson,name='create_person'),
    path('updatePerson/<int:person_id>/',updatePerson,name="updatePerson"),
     path('deletePerson/<int:person_id>/',deletePerson,name="deletePerson")
]