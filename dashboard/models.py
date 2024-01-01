from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

User = get_user_model()

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Person(models.Model):
    PERSON_CHOICES = [
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('N/A','N/A')  
    ]
    name = models.CharField(max_length=100,blank=False,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    gender = models.CharField(max_length=20,choices=PERSON_CHOICES,default="N/A")
    school = models.ForeignKey(School,on_delete=models.SET_NULL,null=True,related_name='persons')
    photo = models.ImageField(upload_to='person_photos',default='person_photos/avatar.png',blank=True)
    # position = models.CharField(max_length=20)
    # email= models.EmailField()
    phone = models.CharField(max_length=15,)
    # age = models.PositiveIntegerField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="persons_created")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.name}"
    

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name}"

    








