from django.contrib import admin

# Register your models here.
from .models import Course,Student,User,UserMessage

class CourseAdmin(admin.ModelAdmin):
    list_display= ('course_name','course_description','date_added','date_edited',)

class StudentAdmin(admin.ModelAdmin):
    list_display= ('study_level','date_added','date_edited',)

class UserMessageAdmin(admin.ModelAdmin):
    list_display= ('heading','text_message','user','date_added','date_edited',)


admin.site.register(UserMessage,UserMessageAdmin)
admin.site.register(Course,CourseAdmin) 
admin.site.register(Student,StudentAdmin) 