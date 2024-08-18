import requests

def getWeather():
    api_key = "2b203ba661da5209df1f2665830b8914"  # API keys go here
    city = "Miami"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
  
    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        desc = data['weather'][0]['description']
        temp_fahren = round((temp_kelvin-273.15) * 9/5 + 32)
        temp_fahren = f"Temperature: {temp_fahren}F\n"
        weather_info = [city, temp_fahren, desc]
        return weather_info
    else:
        return "Failed to return data"
