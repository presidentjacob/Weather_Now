from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('user_form/', views.user_form, name='user_form'),
    path('weather_info/', views.weather_info, name='weather_info'),
]