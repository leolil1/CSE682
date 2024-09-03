import requests

def getWeather(lat,lon,exclusion):
    latitude = lat
    longitude = lon
    part = exclusion  # Specify the exclusions
    api_key = "2b203ba661da5209df1f2665830b8914"  # API keys go here
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&exclude={part}&appid={api_key}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_fahren = (temp_kelvin-273.15) * 9/5 + 32
        temp_fahren = f"Temperature: {temp_fahren}F\n"
        return temp_fahren
    else:
        return "Failed to return data"
