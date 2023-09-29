import requests
from config import API_KEY

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        print('City not found. Please check the spelling and try again.')
        return None
    
    weather = {
        'description': data['weather'][0]['description'],
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }

    return weather

if __name__ == '__main__':
    city = input('Enter city name: ')
    weather = get_weather(city)

    if weather:
        print(f"Current weather in {city}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temp']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
