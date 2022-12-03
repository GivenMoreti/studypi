from django.db import models

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
    private_code =models.IntergerField(max_length=6,null=True)



    def __str__(self):
        return self.student_name    