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

# Get the user form
def user_form(request):
    if request.method == 'POST':
        return render(request, 'user_form.html')
    else:
        return render(request, 'user_form.html')
    
# Get the weather information for the home page
def weather_info(request):
    # If the request is a POST, get the data from the form
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
    # If the request is a GET, get the data from the query parameters
    elif request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')
        
    # Construct the URL for the weather API
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={city}%20{state}%20{country}&apikey={apikey}'

    # Find all information regarding the city
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return HttpResponse('Error fetching weather data. Please try again later.')

    data = response.json()

    first_minute = data['timelines']['minutely'][0]['values']
    temperature_c = first_minute['temperature']
    temperature_f = round((temperature_c * 9/5) + 32, 2)
    precipitation = first_minute['precipitationProbability']
    humidity = first_minute['humidity']
    wind = first_minute['windSpeed']

    # Prepare the context for rendering the template
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

    # Render the template with the context
    return render(request, 'weather_info.html', context)

# Get the weather information for specific cities using the method above
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
        temperature_f = round((temperature_c * 9/5) + 32, 2)
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
        temperature_f = round((temperature_c * 9/5) + 32, 2)
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
        temperature_f = round((temperature_c * 9/5) + 32, 2)
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Winter Park',
            'state': 'Colorado',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'winter_park_colorado.html', context)

def winter_park_florida(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Winter%20Park%20Florida%20USA&apikey={apikey}'

        # Find all information regarding Colorado Springs
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = round((temperature_c * 9/5) + 32, 2)
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Winter Park',
            'state': 'Florida',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'winter_park_florida.html', context)

def seattle(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Seattle%20Washington%20USA&apikey={apikey}'

        # Find all information regarding Colorado Springs
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = round((temperature_c * 9/5) + 32, 2)
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Winter Park',
            'state': 'Florida',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'seattle.html', context)

def alexandria_virginia(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Alexandria%20Virginia%20USA&apikey={apikey}'

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9 / 5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Alexandria',
            'state': 'Virginia',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'alexandria_virginia.html', context)


def alexandria_ontario(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Alexandria%20Ontario%20Canada&apikey={apikey}'

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9 / 5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Alexandria',
            'state': 'Ontario',
            'country': 'Canada',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'alexandria_ontario.html', context)


def melbourne_florida(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Melbourne%20Florida%20USA&apikey={apikey}'

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9 / 5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Melbourne',
            'state': 'Florida',
            'country': 'USA',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'melbourne_florida.html', context)


def melbourne_victoria(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Melbourne%20Victoria%20Australia&apikey={apikey}'

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9 / 5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Melbourne',
            'state': 'Victoria',
            'country': 'Australia',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'melbourne_victoria.html', context)


def venice_italy(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Venice%20Italy&apikey={apikey}'

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9 / 5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Venice',
            'state': '',
            'country': 'Italy',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'venice_italy.html', context)


def mexico_city(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')

        # Construct the URL for the weather API
        url = f'https://api.tomorrow.io/v4/weather/forecast?location=Mexico%20City%20Mexico&apikey={apikey}'

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return HttpResponse('Error fetching weather data. Please try again later.')

        data = response.json()

        first_minute = data['timelines']['minutely'][0]['values']
        temperature_c = first_minute['temperature']
        temperature_f = (temperature_c * 9 / 5) + 32
        precipitation = first_minute['precipitationProbability']
        humidity = first_minute['humidity']
        wind = first_minute['windSpeed']

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'home_city': city,
            'home_state': state,
            'home_country': country,
            'city': 'Mexico City',
            'state': '',
            'country': 'Mexico',
            'temperature_f': temperature_f,
            'temperature_c': temperature_c,
            'precipitation': precipitation,
            'humidity': humidity,
            'wind_speed': wind
        }

    return render(request, 'mexico_city.html', context)