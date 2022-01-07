from django.shortcuts import render
from django.core.mail import send_mail
from .models import input
import json  # import json to load json data to python dictionary
import urllib.request  # urllib.request to make a request to api


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        email = request.POST['email']
        name = request.POST['name']
        ins = input(name=name, email=email, city=city)
        ins.save()

        # source contain JSON data from API

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
            + city + '&units=metric&appid=c1fa08aadf5b95cc7eb1721e78661798').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "name": name,
            "temp": (list_of_data['main']['temp']),
            "mood": '😄',
        }
        if (data["temp"]) < 22:
            data["mood"] = '🥶'
        elif (data["temp"]) > 26:
            data["mood"] = '🥵'
        data["temp"] = str(data["temp"]) + ' °C'

        send_mail(
            "Hi " + name + ", interested in our services", # subject
            "The temperature of " + city + " is " + data["temp"] + " " + data["mood"],# message
            'abhijitprasadband@gmail.com', # from email
            [email], # To email
        )

    else:
        data = {}
    return render(request, "django_weather/home.html", data)
