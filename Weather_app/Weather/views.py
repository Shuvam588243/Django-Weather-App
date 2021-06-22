from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
	if request.method == 'POST':
		location = request.POST['location']
		api_key = '6201d1f3e4aa03cd619c561871d094f2'


		complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+location+"&appid="+api_key

		api_link = requests.get(complete_api_link)
		r = api_link.json()


		weather = { 
		'city' : location,
		'Temperature' : r['main']['temp'],
		'Humidity' : r['main']['humidity'],
		'Wind_Speed' : r['wind']['speed'],
		'Pressure' : r['main']['pressure'],
		'Description' : r['weather'][0]['description'],
		'Icon' : r['weather'][0]['icon'],
		}

		context = { 'city_weather' : weather}
		return render(request,"weather_cards.html",context)


	return render(request,"weather_cards.html")
