from django.urls import path

from . import views

urlpatterns=[
    
    path('',views.index,name='index'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('courses/',views.index,name='courses'),
    path('students/',views.student,name='students'),
    path('register-student/',views.registerStudent,name='register-student'),
    path('edit-student/<str:pk>/',views.editStudent,name='edit-student'),
    path('delete-profile/<str:pk>/',views.deleteProfile,name='delete-profile'),
    path('messages/',views.userMessage,name='userMessages'),
]