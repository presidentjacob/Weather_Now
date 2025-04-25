from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form, name='home'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('user_form/', views.user_form, name='user_form'),
    path('weather_info/', views.weather_info, name='weather_info'),
    path('colorado_springs/', views.colorado_springs, name='colorado_springs'),
    path('denver/', views.denver, name='denver'),
    path('winter_park_colorado/', views.winter_park_colorado, name='winter_park_colorado'),
    path('winter_park_florida/', views.winter_park_florida, name='winter_park_florida'),
    path('alexandria_ontario/', views.alexandria_ontario, name='alexandria_ontario'),
    path('melbourne_florida/', views.melbourne_florida, name='melbourne_florida'),
    path('melbourne_victoria/', views.melbourne_victoria, name='melbourne_victoria'),
    path('venice_italy/', views.venice_italy, name='venice_italy'),
    path('mexico_city/', views.mexico_city, name='mexico_city'),
    path('alexandria_virginia/', views.alexandria_virginia, name='alexandria_virginia'),
    path('seattle/', views.seattle, name='seattle'),
]