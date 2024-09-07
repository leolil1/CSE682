import requests

# API class will be used to make API calls to
# OpenWeather API.
class API:
    #Constructor that has a valid key to use to make API calls.
    #User can also supply their own.
    def __init__(self,api_key="2b203ba661da5209df1f2665830b8914"):
        self.api_key=api_key # API keys go here

    #Function to make the API call leveging the requests library
    def GetWeather(self,location="Miami"):
        city = location  # Location we'll search weather for
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"  # the URL for the API call

        response = requests.get(url)  # Leverage requests library to make the API call

        # If call is success, then we'll extract the temp, and weather description.
        # We'll then convert the temp from kelvin to Farenhei.
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
