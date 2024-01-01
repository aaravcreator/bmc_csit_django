from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        fields = ['name','address','gender','school','photo','phone']
        # fields = "__all__"
        model = Person

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",max_length=100)
    password = forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput)

