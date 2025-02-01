from django.urls import path
from .views import user_login,register_view
from . import views

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", user_login, name="login"),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
  
]
