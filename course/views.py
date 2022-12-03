from django.shortcuts import render,redirect

# Create your views here.
from .models import Course
from .models import Student
# model forms imports
from .forms import StudentForm


def index(request):
    # form validation rules:
    courses = Course.objects.all()
    courses = Course.objects.order_by('date_added')
    return render (request,'course/courses.html',{"courses":courses})

def student(request):
     # form validation rules:
    # if request.method ==POST:
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('students')

    students= Student.objects.all()
    students = Student.objects.order_by('date_added')
    return render (request,'course/students.html',{"students":students})

# crud starts here

def registerStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        # print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')

    return render (request,'course/register.html',{"form":form})

def editStudent(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')




    context = {'form':form}
    return render(request,'course/register.html',context)

def deleteProfile(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students')


    return render(request,'course/delete-profile.html')