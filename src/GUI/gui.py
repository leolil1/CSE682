import tkinter as tk
from tkinter import END
from PIL import Image, ImageTk  #using PIL to convert JPG images to something Tkinter can use 
from API.api2 import API
from GUI.SaveFavGui import openFavorite
from GUI.Button import guiButton
from GUI.Textbox import guiTextbox
from GUI.Label import guiLabel
from ImageSelect.ImageSelect import ImageSelect

class GUI:
    #constructor used to set the size of the window frame
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.size = f"{width}x{height}"
    
    def createGUI(self):
        # Use Tk() function from tkinter to create a root window
        # that serve as the frame that holds everything inside
        rootWindow = tk.Tk()
        rootWindow.title("Weather APP")  #configure a title
        rootWindow.configure(bg='grey')  #configure the background color
        rootWindow.geometry(self.size)

        # Create 4 Labels thru guiLabel class objects. They will each
        # display relevant weather info. The 4th label will be used 
        # to display background images. They will be stacked on top
        # of each other
        self.weather_label_city = guiLabel(rootWindow)
        self.weather_label_city.pack(pady=10)
        self.weather_label_temp = guiLabel(rootWindow)
        self.weather_label_temp.pack(pady=10)
        self.weather_label_status = guiLabel(rootWindow)
        self.weather_label_status.pack(pady=10)
        self.weather_label_image = guiLabel(rootWindow)
        
        self.weather_label_image.config(width=500, height=500)  # Set these dimensions as needed
        self.weather_label_image.pack(pady=10)

        # Using the button class Create a button which will be used to toggle current to 7-day forecast
        toggle_button = guiButton(rootWindow, x=700, y=30,text="7-day", command=self.__checkDisplay)

        # a button widget which will open a 
        # new window on button click
        fav = guiButton(rootWindow, x=150, y=150,text ="Favorite", command = openFavorite)
        
        # TextBox Creation for searching different locations
        inputtxt= guiTextbox(rootWindow, x=50, y=30, width=10,height=2)
        
        # This function serves to link the functioanlity from button to textbox.
        # When the button is clicked, it'll retrieve the content from the textbox
        # and call __checkDisplay() to update weather info on the screen.
        def __locationRetrival():
            location = inputtxt.textRetrive()
            self.__checkDisplay(location)

        # Search Location Button Creation
        saveButton = guiButton(rootWindow, x=150, y= 30, text="Search", command=__locationRetrival)

        # Fetch and display the weather data
        self.__checkDisplay()

        # Run the application
        rootWindow.mainloop()  #mainloop() will actively listen for user event such as mouse click and so on. This function will keep the window open and make our program responsive to user actions. Window is only closed when we click on the "x" button top right.

    # Function to update the weather display
    def __checkDisplay(self,location="Miami"):
        api_client=API()   #creating the API object so we can use to retrieve weather info
        weather_data = api_client.getWeather(location)
        self.weather_label_city.config(text=weather_data[0])
        self.weather_label_temp.config(text=weather_data[1])
        self.weather_label_status.config(text=weather_data[2])

        backgroundImage = ImageSelect()
        photo=backgroundImage.backgroundSelector(weather_data[2])

        self.weather_label_image.config(image=photo)
        self.weather_label_image.image = photo

        
        

