from django.contrib import admin
from django.urls import path
from . import views  # Assuming 'views.py' is in the same directory
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include('login.urls')), 
   
]