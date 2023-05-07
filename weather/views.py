import json
import urllib
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        encoded_city = urllib.parse.quote(city)
        api_url = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='+encoded_city+'&appid=abb15ac3fe3694d485c363e14c02aa0f&units=metric').read()
        api_url2 = json.loads(api_url)

        data = {
            'city': city,
            'weather_description': api_url2['weather'][0]['description'],
            'weather_temperature': api_url2['main']['temp'],
            'weather_pressure': api_url2['main']['pressure'],
            'weather_humidity': api_url2['main']['humidity'],
            'weather_icon': api_url2['weather'][0]['icon'],
        }
    else:
        data = {
            'city': None,
            'weather_description': None,
            'weather_temperature': None,
            'weather_pressure': None,
            'weather_humidity': None,
            'weather_icon': None
        }

    return render(request, 'index.html', {'data': data})
