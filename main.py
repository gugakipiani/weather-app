import datetime as dt
import requests
import os
from dotenv import load_dotenv
from translate import Translator
from scripts import *
from input_cities import *

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("No API key found. Please set the OPENWEATHER_API_KEY environment variable.")

# Ask user for city input
CITY = city()

# Create API request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={API_KEY}"

# Make the API request and get weather data
weather = requests.get(url).json()

# Translator to convert English text to Georgian
translator = Translator(to_lang="ka")

# Translate city name
translated_city = translated_city(CITY)

# Handle invalid city or error in API response
if weather['cod'] != 200:
    print("შეცდომა დასახელებაში!")  # Error message in Georgian
else:
    # Extract and convert temperature values
    temp_kelvin = weather['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_and_fahrenheit(temp_kelvin)

    feels_like_kelvin = weather['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_and_fahrenheit(feels_like_kelvin)

    # Extract humidity and wind speed
    humidity = weather['main']['humidity']
    wind_speed_metres_per_seconds = weather['wind']['speed']
    wind_speed_kilometers_per_hour = wind_speed_metres_per_seconds / 1000 * 3600

    # Handle optional visibility field
    if 'visibility' in weather:
        visibility = f"{(weather['visibility'] / 1000):.1f}"
    else:
        visibility = "უცნობია"  # "Unknown" in Georgian

    # Translate weather description
    original_description = weather['weather'][0]['description']
    translated_description = translator.translate(original_description)

    # Convert sunrise and sunset times from timestamps to readable format
    sunrise_time = dt.datetime.utcfromtimestamp(weather['sys']['sunrise'] + weather['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(weather['sys']['sunset'] + weather['timezone'])

    # Get full country name from country code
    country_code = weather['sys']['country']
    country = country_name(country_code)
    translated_country = translator.translate(country)

    # Print the translated weather report
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
