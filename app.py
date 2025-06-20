from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)


API_KEY = "9f1b34664516bd606cd9e100ee2a36f2"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    location = None
    error = None
    
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            weather_data = get_weather(location)
            if not weather_data:
                error = "Couldn't fetch weather data. Please try another location."

    return render_template('index.html', weather=weather_data, location=location, error=error)

def get_weather(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather_types = {
            'Clear': 'sunny',
            'Clouds': 'cloudy',
            'Rain': 'rainy',
            'Thunderstorm': 'stormy',
            'Snow': 'snowy',
            'Mist': 'foggy'
        }
        
        return {
            'city': data['name'],
            'temp': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'weather_type': weather_types.get(data['weather'][0]['main'], 'default')
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)