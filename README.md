# Weather App

A command-line weather app that fetches real-time weather data using the OpenWeather API, with support for Georgian translation.


## Features

- Live weather data by city
- Translates output to **Georgian** using the `translate` package
- Displays:
  - Temperature (actual and "feels like")
  - Humidity and wind speed
  - Visibility
  - Sunrise and sunset times
- Uses a CSV file to convert ISO country codes to full country names

---

## 📦 Requirements

- Python 3.8 or higher
- An OpenWeatherMap API key
- Internet connection

---

## 🛠️ How to Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/gugakipiani/weather-app.git
    cd weather-app
    ```

2. **Install required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**

    Create a `.env` file in the root folder and add your OpenWeatherMap API key:

    ```env
    OPENWEATHER_API_KEY=your_api_key_here
    ```

4. **Run the app:**

    ```bash
    python main.py
    ```


   **Example output:**

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

    




---

## Notes

- An **OpenWeatherMap API key** is required. Store it in a `.env` file as shown above.
- Translations are handled using the `translate` Python package.
- Country names are resolved from ISO codes using the `wikipedia-iso-country-codes.csv` file.
