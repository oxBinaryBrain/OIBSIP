import requests

def get_weather(city):
    # Base URL for the OpenWeatherMap API
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "2ee160f54e5c795c83c43f81bc2708a3"  # Replace with your actual API key

    # Construct the complete URL
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"

    # Send a GET request to the API
    response = requests.get(URL)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        # Extracting relevant information
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        description = weather['description']

        # Displaying the weather information
        print(f"City: {city.capitalize()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather: {description.capitalize()}")
    else:
        print("Error: Unable to fetch weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)