import csv


# Get country name from country code
def country_name(code):
    dic = {}
    with open("wikipedia-iso-country-codes.csv") as f:
        file = csv.DictReader(f, delimiter=',')
        for line in file:
            dic[line['Alpha-2 code']] = line['English short name lower case']

    country_short = code

    return dic[country_short]


# To convert temperature units from kelvin to celsius
def kelvin_to_celsius_and_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 1.8) + 32
    return celsius, fahrenheit
