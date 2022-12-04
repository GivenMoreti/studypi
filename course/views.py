from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .models import Course
from .models import Student
# these are the user Messages that will be accessible upon login account
from .models import Messages
# model forms imports
from .forms import StudentForm
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def loginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            
        except:
            messages.error(request,'User does not exit,try to register')
            return redirect('register-student')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('students')
        else:
            messages.error(request,'username or password does not exist')
    context = {}
    return render(request, 'course/login.html',context)
# logout a user
def logoutUser(request):
    logout(request)
    return redirect('courses')

def index(request):
    # form validation rules:
    try:
        courses = Course.objects.all()
        courses = Course.objects.order_by('date_added')
    except Course.DoesNotExist:
        raise Http404("course does not exist")
    return render (request,'course/courses.html',{"courses":courses})

def student(request):
     # form validation rules:
    # if request.method ==POST:
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('students')
    try:
        students= Student.objects.all()
        students = Student.objects.order_by('date_added')
        
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
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


def userMessage(request):
    userMessages = Messages.objects.all()
    context = {'userMessages':userMessages}
    return render(request,'course/user-message.html',context)