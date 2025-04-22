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
        
        # Construct the URL for the weather API
        url = f"https://www.google.com/search?q={city}+{state}+{country}+weather"
        
        # Use Selenium and BS4 to fetch the weather information
        # driver_options = webdriver.ChromeOptions()
        # driver_options.add_argument('--headless')
        driver = webdriver.Chrome()

        driver.get(url)
        # Wait for page to load
        time.sleep(30)

        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        driver.quit()
        temperature_f = soup.find('span', {'id': 'wob_tm'}).text
        temperature_c = soup.find('span', {'id': 'wob_ttm'}).text
        precipitation = soup.find('span', {'id': 'wob_pp'}).text
        humidity = soup.find('span', {'id': 'wob_hm'}).text
        wind = soup.find('span', {'id': 'wob_ws'}).text

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