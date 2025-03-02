from django.urls import path
from . import views

urlpatterns = [
   
    path('dashboard',views.dashboard, name='dashboard'),  
    path('profile/', views.profile, name='profile'),
    path('add_student/', views.add_student, name='add_student'),
    path('students/',views.all_students, name='all_students'),
    path('departments/',views.departments, name='departments'),
    path('programs/',views.programs, name='programs'),
    path('logout/',views.logout, name='logout'),
    
      
  
]


