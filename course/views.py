from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .models import Course
from .models import Student
# these are the user Messages that will be accessible upon login account
from .models import UserMessage
# model forms imports
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

from .forms import UserMessageForm

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
@login_required(login_url='/login')
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

@login_required(login_url='/login')
def student(request):
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

@login_required(login_url='/login')
# a user that is not registered cannot edit their profile
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

@login_required(login_url='/login')
def deleteProfile(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students')


    return render(request,'course/delete-profile.html')


@login_required(login_url='/login')
def addMessage(request):
    form = UserMessageForm()
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('messages')
    return render (request,'course/add-message.html',{"form":form})


@login_required(login_url='/login')
def user_messages(request):
    user_messages = UserMessage.objects.all()
    user_messages = UserMessage.objects.order_by('date_added')
    return render(request,'course/messages.html',{"user_messages":user_messages})
