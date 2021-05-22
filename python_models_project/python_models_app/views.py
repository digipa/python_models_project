from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    faculty = Faculty.objects.all()
    department = Department.objects.all()
    school = School.objects.all()
    certificate_type = Certificate_type.objects.all()
    grade = Grade.objects.all()
    student = Student.objects.all()

    context = {
        "facultys" : faculty,
        "departments" : department,
        "schools" : school,
        "certificate_types" : certificate_type,
        "grades" : grade,
        "students" : student
    }

    return render(request, 'python_models_app/index.html', context)
