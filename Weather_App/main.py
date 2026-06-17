import requests
import json
from config import api_key



def get_city():
    city_name=input("Give a name of a city: ")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"
    return url


def save_data(weather_url):
    response=requests.get(weather_url)
    data=response.json()
    with open("weather.json", "w") as file:
        json.dump(data, file)
    return data

def main():
    url_=get_city()
    data=save_data(url_)
    
    print(f"Weather for {data['name']}")
    print(f"Temperature: {data['main']['temp']}°F")
    print(f"Feels like: {data['main']['feels_like']}°F")
    print(f"Condition: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} mph")




main()
