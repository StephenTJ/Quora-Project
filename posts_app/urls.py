from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.Home_Page),
    path('home', views.Home_Page,name='home'),
    path('questions', views.Questions_Page,name='questions'),
    path('askquestion',views.Ask_Question_Page,name='askquestion'),
    path('answerquestion/<int:question_id>',views.Answer_Question_Page,name='answerquestion'),
    path('addlike/<int:answer_id>/<int:answered_by_user_id>',views.Add_Like_Page,name='addlike'),
    path('dev/',views.Home_Page),
    path('dev/home', views.Home_Page,name='home'),
    path('dev/questions', views.Questions_Page,name='questions'),
    path('dev/askquestion',views.Ask_Question_Page,name='askquestion'),
    path('dev/answerquestion/<int:question_id>',views.Answer_Question_Page,name='answerquestion'),
    path('dev/addlike/<int:answer_id>/<int:answered_by_user_id>',views.Add_Like_Page,name='addlike'),
]