from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
COURSE_LEVELS = (
    ("first","1"),
    ("second","2"),
    ("third","3"),
)

COURSES =(
    ("IT","information Technology"),
    ("Azure","Azure"),
    ("AWS","AWS"),
    ("Artificial Intelligence","Artificial Intelligence"),
    ("Ethical hacking","Ethical hacking"),
    
)

class Course(models.Model):
    course_name = models.CharField(max_length=30,default=None,choices=COURSES)
    course_url = models.CharField(max_length=8000,null=True)
    course_description = models.CharField(max_length=300,null=True)
    date_added = models.DateField(auto_now_add=True,null=True)
    date_edited = models.DateField(auto_now=True,null=True)
    
    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    study_level = models.CharField(max_length=30,default="1",choices=COURSE_LEVELS)
    username = models.CharField(max_length=30,null=True)
    date_added = models.DateField(auto_now_add=True,null=True)
    date_edited = models.DateField(auto_now=True,null=True)
    image_url=models.CharField(max_length=8000,null=True)
    # image_file = models.ImageField(upload_to='images',null=True)
    private_code =models.IntegerField(null=True,unique=True)
    # the private code is for authenticating profile deletion
    # but not yet activated
    # ideally every profile must have a student number and private code to log in


    def __str__(self):
        return self.student_name    
    
class UserMessage(models.Model):
    heading = models.CharField(max_length=300,null=True)
    text_message =models.TextField(max_length=3000, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True,null=True)
    date_edited = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.heading


