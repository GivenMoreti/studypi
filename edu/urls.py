
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include('course.urls')),
    path('admin/', admin.site.urls),
    path('items/',include('items.urls')),
]
# these are the core urls.