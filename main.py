import datetime as dt
import requests
import os
from dotenv import load_dotenv
from translate import Translator
from scripts import *
from input_cities import *  # Includes city() and translated_city()

# Load environment variables from .env
load_dotenv()

# Retrieve API key from environment
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("No API key found. Please set the OPENWEATHER_API_KEY environment variable.")

# Get normalized user input
CITY = city()

# Build request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={API_KEY}"
weather = requests.get(url).json()

# Translate city name to Georgian
translator = Translator(to_lang="ka")
translated_city_name = translated_city(CITY)

# Check API response
if weather['cod'] != 200:
    print("შეცდომა დასახელებაში!")  # Invalid city
else:
    # Extract temperature
    temp_kelvin = weather['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_and_fahrenheit(temp_kelvin)

    # Feels like
    feels_like_kelvin = weather['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_and_fahrenheit(feels_like_kelvin)

    # Humidity and wind
    humidity = weather['main']['humidity']
    wind_speed_mps = weather['wind']['speed']
    wind_speed_kph = wind_speed_mps / 1000 * 3600

    # Visibility (optional)
    visibility = f"{(weather['visibility'] / 1000):.1f}" if 'visibility' in weather else "უცნობია"

    # Description translation
    original_description = weather['weather'][0]['description']
    translated_description = translator.translate(original_description)

    # Sunrise and sunset (converted to local time using timezone offset)
    sunrise = dt.datetime.utcfromtimestamp(weather['sys']['sunrise'] + weather['timezone'])
    sunset = dt.datetime.utcfromtimestamp(weather['sys']['sunset'] + weather['timezone'])

    # Country translation
    country_code = weather['sys']['country']
    country = country_name(country_code)
    translated_country = translator.translate(country)

    # Output results
    print()
    print(translated_city_name + ', ' + translated_country)
    print(translated_description)
    print(f'ტემპერატურა: {temp_celsius:.1f} °C')
    print(f'მგრძნობელობა: {feels_like_celsius:.1f} °C')
    print(f'ტენიანობა: {humidity}%')
    print(f'ქარის სიჩქარე: {wind_speed_kph:.1f} კმ/სთ')
    print(f'ხილვადობა: {visibility} კმ')
    print('აისი:', sunrise)
    print('დაისი:', sunset)
