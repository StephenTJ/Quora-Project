from django.urls import path,include
from . import views

urlpatterns = [
    path('login', views.Login_Page,name='login'),
    path('logout', views.Logout_Page,name='logout'),
    path('signup', views.Signup_Page,name='signup'),
    path('dev/login', views.Login_Page,name='login'),
    path('dev/logout', views.Logout_Page,name='logout'),
    path('dev/signup', views.Signup_Page,name='signup'),
]