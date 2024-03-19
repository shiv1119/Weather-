import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if 'main' in weather_data and 'temp' in weather_data['main']:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("Failed to retrieve weather information.")


api_key = '083f70bf5f2ec704e0318a5dd8196eac' 
city_name = input("Enter city name: ")
weather_data = get_weather(city_name, api_key)
display_weather(weather_data)
