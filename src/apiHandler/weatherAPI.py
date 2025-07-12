import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def getWeather(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL,params = params)
        data = response.json()
        
        if response.status_code != 200:
            print("❌ Error:", data.get("message", "Unknown error"))
            return None
        
        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        return temp, condition
    except requests.exceptions.RequestException as e:
        print("❌ Network Error:", e)
        return None