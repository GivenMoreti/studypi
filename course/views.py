from django.shortcuts import render

# Create your views here.
from .models import Course
from .models import Student

def index(request):
    courses = Course.objects.all()
    return render (request,'course/courses.html',{"courses":courses})

def student(request):
    students= Student.objects.all()
    return render (request,'course/students.html',{"students":students})

