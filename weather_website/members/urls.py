from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('user_form/', views.user_form, name='user_form'),
    path('weather_info/', views.weather_info, name='weather_info'),
    path('colorado_springs/', views.colorado_springs, name='colorado_springs'),
    path('denver/', views.denver, name='denver'),
    path('winter_park_colorado/', views.winter_park_colorado, name='winter_park_colorado'),
    path('winter_park_florida/', views.winter_park_florida, name='winter_park_florida'),
]