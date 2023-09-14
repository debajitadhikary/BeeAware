from django.urls import path
from . import views


urlpatterns =[
    path('' , views.index, name='index'),
    path('register', views.register , name ='register'),
    path('login' , views.login , name = 'login'),
    path('logout', views.logout, name='logout'),
    path('home', views.logout, name='home'),
    path('right_to_edu', views.right_to_edu , name='right_to_edu')
]