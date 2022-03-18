
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="Trang Chu"),
    path('login/', views.login, name="Login"),
    path('logout/', views.logout, name='LogOut'),
    path('SignUp/', views.signup, name='SignUp'),
]
