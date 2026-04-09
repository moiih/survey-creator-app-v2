from django.urls import path
from quiz import views

# app_name  = 'quiz'

urlpatterns = [    
    path('set_quiz_title/', views.set_quiz_title, name='set_quiz_title'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),       
    path('show_quiz/<str:quiz_title>/', views.show_quiz, name='show_quiz'),   
    path('get_titles/', views.get_titles, name=''),
    path('delete_quiz/<str:quiz_title>/', views.delete_quiz, name='delete_quiz'),
    path('quiz_result/<str:quiz_title>/', views.quiz_result, name='quiz_result'),
    # path('WXCcaHszcx_share_rsfVsfvSf_quiz_JKsdoizb/<str:quiz_title>', views.share_quiz, name='share_quiz'),
    path('delete_user_response/<str:quiz_title>/<str:poller>', views.delete_response, name='delete_response'),
]