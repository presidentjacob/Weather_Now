from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import lxml

apikey = 'nzV0HFfFgr7MvrhbRJ1akgjgReTzuabu'

headers = {
    'accept': 'application/json',
    'accept-encoding': 'deflate, gzip, br'
}

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def user_form(request):
    if request.method == 'POST':
        return render(request, 'user_form.html')
    else:
        return render(request, 'user_form.html')
    
def weather_info(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
    elif request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')
        
        # Construct the URL for the weather API
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={city}%20{state}%20{country}&apikey={apikey}'

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return HttpResponse('Error fetching weather data. Please try again later.')

    data = response.json()

    first_minute = data['timelines']['minutely'][0]['values']
    temperature_c = first_minute['temperature']
    temperature_f = (temperature_c * 9/5) + 32
    precipitation = first_minute['precipitationProbability']
    humidity = first_minute['humidity']
    wind = first_minute['windSpeed']

    context = {
        'firstname': firstname,
        'lastname': lastname,
        'city': city,
        'state': state,
        'country': country,
        'temperature_f': temperature_f,
        'temperature_c': temperature_c,
        'precipitation': precipitation,
        'humidity': humidity,
        'wind_speed': wind
    }

    return render(request, 'weather_info.html', context)

def colorado_springs(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Colorado%20Springs%20Colorado%20USA&apikey={apikey}'

        # Find all information regarding Colorado Springs
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9/5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Colorado Springs',
            'state': 'Colorado',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'colorado_springs.html', context)

def denver(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Denver%20Colorado%20USA&apikey={apikey}'

        # Find all information regarding Colorado Springs
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9/5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Denver',
            'state': 'Colorado',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'denver.html', context)

def winter_park_colorado(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Winter%20Park%20Colorado%20USA&apikey={apikey}'

        # Find all information regarding Colorado Springs
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9/5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Denver',
            'state': 'Colorado',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'winter_park_colorado.html', context)