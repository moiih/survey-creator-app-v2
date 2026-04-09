from django.urls import path
from poll import views


urlpatterns = [    
    path('', views.user_login_index, name='login'),    
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),

    path('home/', views.home, name='home'),
    path('myhome/', views.my_home, name='myhome'),
    path('create/', views.create_poll, name='create'),
    path('vote/<int:poll_id>/', views.cast_vote, name='vote'),
    path('result/<int:poll_id>/', views.result, name='result'),

    path('delete/<int:poll_id>/', views.delete, name='delete'),
    path('mydelete/<int:poll_id>/', views.my_delete, name='mydelete'),
    path('edit/<int:poll_id>/', views.edit, name='edit'),
    path('search/', views.search, name='search'),
]