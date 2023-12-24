from django.contrib import admin

# Register your models here.
from .models import Partner,Person

admin.site.register(Partner)
admin.site.register(Person)

