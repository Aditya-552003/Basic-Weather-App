import requests

api_key = "c86432b6f88b243f1a9e5281514eb47b"
location = input("Enter a city or ZIP code: ")
api_url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": location, 
    "units": "metric",
    "appid": api_key
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    weather = {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
        'city': data['name'],
        'country': data['sys']['country']
    }
    print(f"Weather in {weather['city']}, {weather['country']}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Conditions: {weather['description']}")
else:
    print("Sorry, couldn't fetch the weather data. Please check the location and try again.")
