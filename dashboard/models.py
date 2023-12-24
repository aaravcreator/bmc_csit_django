from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    gender = models.CharField(max_length=20,default="N/A")
    # position = models.CharField(max_length=20)
    # email= models.EmailField()
    # phone = models.CharField(max_length=15)
    # age = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name}"

    








