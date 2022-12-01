from django.contrib import admin

# Register your models here.
from .models import Course,Student

class CourseAdmin(admin.ModelAdmin):
    list_display= ('course_name','course_description','date_added','date_edited',)

class StudentAdmin(admin.ModelAdmin):
    list_display= ('student_name','course_name','username','study_level','date_added','date_edited',)


admin.site.register(Course,CourseAdmin) 
admin.site.register(Student,StudentAdmin) 