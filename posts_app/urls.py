from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.Home_Page),
    path('home', views.Home_Page,name='home'),
    path('questions', views.Questions_Page,name='questions'),
]