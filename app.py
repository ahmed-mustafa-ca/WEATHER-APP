import requests

api_key = "9a92f73bcd52b10554476b33bcbc0308"

user_input = input("Enter a city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")

if weather_data.json()["cod"] == "404":
    print("no city found")
else:

    weather = weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])

    print(f"The weather in {user_input} is: {weather}")
   
    temp_celcius = temp - 273.15
    print(f"The temperature in {user_input} is: {round(temp_celcius)}°C")

