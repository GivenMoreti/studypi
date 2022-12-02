from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('courses/',views.index,name='courses'),
    path('students/',views.student,name='students'),
    path('register-student/',views.registerStudent,name='register-student'),
]