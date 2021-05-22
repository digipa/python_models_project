from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.sites import site
from .models import *

# Register your models here.

myModels = [Faculty, Department, School, Certificate_type, Grade, Student]

admin.site.register(myModels)
