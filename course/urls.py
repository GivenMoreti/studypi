from django.urls import path

from . import views

urlpatterns=[
    path('',views.index),
    path('courses/',views.index),
    path('students/',views.student),
]