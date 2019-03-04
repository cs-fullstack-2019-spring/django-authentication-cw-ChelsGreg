from django.urls import path
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('newTrack/', views.newTrack, name='newTrack'),
    path('loginhere/', views.loginhere, name='loginhere'),

]