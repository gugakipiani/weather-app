import datetime as dt
import requests
import os
from translate import Translator
from scripts import *
from input_cities import *


# Using API from weather website
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = city()
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={API_KEY}"
weather = requests.get(url).json()


translator = Translator(to_lang="ka")
translated_city = translated_city(CITY)


# 200 is success code
if weather['cod'] != 200:
    print("შეცდომა დასახელებაში!")
else:
    temp_kelvin = weather['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_and_fahrenheit(temp_kelvin)
    feels_like_kelvin = weather['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_and_fahrenheit(feels_like_kelvin)
    humidity = weather['main']['humidity']
    wind_speed_metres_per_seconds = weather['wind']['speed']
    wind_speed_kilometers_per_hour = wind_speed_metres_per_seconds / 1000 * 3600
    if 'visibility' in weather:
        visibility = f"{(weather['visibility'] / 1000):.1f}"
    else:
        visibility = "უცნობია"
    original_description = weather['weather'][0]['description']
    translated_description = translator.translate(original_description)
    sunrise_time = dt.datetime.utcfromtimestamp(weather['sys']['sunrise'] + weather['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(weather['sys']['sunset'] + weather['timezone'])
    country_code = weather['sys']['country']
    country = country_name(country_code)
    translated_country = translator.translate(country)

    print()

    print(translated_city + ', ' + translated_country)
    print(translated_description)
    print(f'ტემპერატურა: {temp_celsius:.1f} °C')
    print(f'მგრძნობელობა: {feels_like_celsius:.1f} °C')
    print(f'ტენიანობა: {humidity}%')
    print(f'ქარის სიჩქარე: {wind_speed_kilometers_per_hour:.1f} კმ/სთ')
    print(f'ხილვადობა: {visibility} კმ')
    print('აისი:', sunrise_time)
    print('დაისი:', sunset_time)
