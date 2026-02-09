import requests
import csv
import os

url = "https://api.open-meteo.com/v1/forecast?latitude=17.385&longitude=78.4867&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]

    print("✅ Current Weather in Hyderabad:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Windspeed: {weather['windspeed']} km/h")
    print(f"Time: {weather['time']}")

    filename = "weather_data.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Temperature (°C)", "Windspeed (km/h)", "Time"])
        writer.writerow([weather["temperature"], weather["windspeed"], weather["time"]])

    print("📂 Data saved to:", os.path.abspath(filename))
    print("File exists?", os.path.exists(filename))

else:
    print("Error fetching data:", response.status_code)
