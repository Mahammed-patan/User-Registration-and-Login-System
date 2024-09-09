from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Registerpage, name='registerpage'),
    path('register/',views.UserRegister, name='register'),
    path('loginpage/',views.Loginpage, name='loginpage'),
    path('loginuser/',views.UserLogin, name='login'),
]