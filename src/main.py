from src.apiHandler.weatherAPI import getWeather
from src.logic.logic import outfitRecommendation

def main():
    city = input("🌍 Enter your city: ").strip()
    result = getWeather(city)
    if result:
        temp, condition = result
        print(f"\n📍 City: {city.title()}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌦️ Condition: {condition}")
        print(f"👕 Recommendation: {outfitRecommendation(temp, condition)}")