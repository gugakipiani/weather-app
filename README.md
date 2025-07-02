# Weather App

A command-line weather app that fetches real-time weather data using the OpenWeather API, with support for Georgian translation.

## Features
- Live weather data by city
- Translates output to Georgian using the `translate` library
- Temperature, wind, humidity, visibility, sunrise & sunset
- CSV lookup for country names using ISO codes

## How to Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/gugakipiani/weather-app.git
    cd weather-app
    ```

2. **Install required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app:**

    ```bash
    python main.py
    ```

4. **Example output:**

    ```
    თბილისი, საქართველო
    მოწმენდილი ცა
    ტემპერატურა: 22.4 °C
    მგრძნობელობა: 21.3 °C
    ტენიანობა: 45%
    ქარის სიჩქარე: 12.4 კმ/სთ
    ხილვადობა: 10.0 კმ
    აისი: 06:08:00
    დაისი: 20:43:00
    ```



Notes
- Requires an OpenWeather API key. You can replace the placeholder in main.py.
- Output is translated into Georgian using the `translate` package.
- The app uses a CSV file (`wikipedia-iso-country-codes.csv`) to convert country codes to full names.
