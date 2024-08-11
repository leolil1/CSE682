import tkinter
from api import getWeather


# Function to update the weather display
def checkDisplay():
    weather_label.config(text=getWeather("38.89","-77.01","alerts"))

# Use Tk() function from tkinter to create a root window
# that serve as the frame that holds everything inside
rootWindow = tkinter.Tk()
rootWindow.title("Weather APP")  #configure a title
rootWindow.configure(bg='grey')  #configure the background color

# Create a text box to display the weather information
weather_label = tkinter.Label(rootWindow, text="Fetching weather data...", bg='grey', fg='white', font=("Arial", 14))  #we use Label() to add a text box. This value will be updated later in checkDisplay() function to reflect temp data
weather_label.pack(pady=20) #we use pack() to position the label. Right now it's 20pixles of padding above and below the text box. As we add more information, this is going to change. 

# Create a button which will be used to toggle current to 7-day forecast
toggle = tkinter.Button(rootWindow, text="7-day", command=checkDisplay, bg='white', fg='black')
toggle.pack(pady=10)

# Fetch and display the weather data
checkDisplay()

# Run the application
rootWindow.mainloop()  #mainloop() will actively listen for user event such as mouse click and so on. This function will keep the window open and make our program responsive to user actions. Window is only closed when we click on the "x" button top right.
