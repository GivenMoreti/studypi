from django.shortcuts import render,redirect

# Create your views here.
from .models import Course
from .models import Student
# model forms imports
from .forms import StudentForm


def index(request):
    # form validation rules:
    courses = Course.objects.all()
    return render (request,'course/courses.html',{"courses":courses})

def student(request):
     # form validation rules:
    # if request.method ==POST:
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('students')

    students= Student.objects.all()
    return render (request,'course/students.html',{"students":students})

# crud starts here

def registerStudent(request):
    form = StudentForm()

    return render (request,'course/register.html',{"form":form})
