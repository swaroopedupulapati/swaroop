import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] != 200:
        print("Error:", weather_data["message"])
        return

    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")

def main():
    api_key = "9f8dfa3a1576d1cb0f93cd680aa88a4d"
    location = input("Enter city name or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()