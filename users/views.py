from datetime import datetime

# for api
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# for weather
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def index(request):
    return HttpResponse('The Index View')
# HttpResponse will return a certain response to the user. In this case, it will return the text that has been passed to it.



def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

@login_required()
def showweatherapp(request):
    return render(request, 'weatherupdates/home.html')

# the index() will handle all the app's logic
def index(request):
    # if there are no errors the code inside try will execute
    try:
    # checking if the method is POST
        if request.method == 'POST':
            API_KEY = 'ca97ccd6acec82932c7129bc6602642a'
            # getting the city name from the form input   
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY   
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json   
            response = requests.get(url).json()
            # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            # bundling the weather information in one dictionary
            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'weatherupdates/home.html', context)
    except Exception:
        return render(request, 'weatherupdates/404.html')