from django.db import models
from django.contrib.auth.models import User


# Create your models here.
COURSE_LEVELS = (
    ("first","1"),
    ("second","2"),
    ("third","3"),
)



class Course(models.Model):
    course_name = models.CharField(max_length=30)
    course_url = models.CharField(max_length=8000,null=True)
    course_description = models.CharField(max_length=300,null=True)
    date_added = models.DateField(auto_now_add=True,null=True)
    date_edited = models.DateField(auto_now=True,null=True)
    
    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course,related_name="courses",editable=True,default=None,help_text="Select your courses",)
    study_level = models.CharField(max_length=30,default="1",choices=COURSE_LEVELS)
    username = models.CharField(max_length=30,null=True)
    date_added = models.DateField(auto_now_add=True,null=True)
    date_edited = models.DateField(auto_now=True,null=True)
    image_url=models.CharField(max_length=8000,null=True)
    # image_file = models.ImageField(upload_to='images',null=True)
 


    def __str__(self):
        return self.student_name    
    
class UserMessage(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    heading = models.CharField(max_length=300,null=True)
    text_message =models.TextField(max_length=3000, null=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True)
    date_edited = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.heading


