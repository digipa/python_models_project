from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete= models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Certificate_type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Student(models.Model):
    department = models.ForeignKey(Department, default="", on_delete = models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete= models.CASCADE)
    school = models.ForeignKey(School, on_delete= models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_type, on_delete= models.CASCADE)
    fullname = models.CharField(max_length=30)
    year_of_graduation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
