from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        # fields = ['name','address','gender','school']
        fields = "__all__"
        model = Person

class LoginForm(forms.Form):
    pass
