import requests
from dotenv import load_dotenv
import os


def fetch_weather(city):
    """Method to get the current temperature in a city using the weather API."""
    load_dotenv()
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temperature = data['current']['temp_c']
            return temperature
        else:
            print(f"Error: {data['message']}")
            return None
    except Exception as e:
        print(f"Error fetching weather data: {str(e)}")
        return None
