# weather_api.py
import requests
from config import API_KEY

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return None, data.get("message", "Error occurred")
        weather = {
            "city": data["name"],
            "description": data["weather"][0]["description"].title(),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }
        return weather, None
    except Exception as e:
        return None, str(e)
