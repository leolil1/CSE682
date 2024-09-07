import tkinter as tk
from tkinter import END
from PIL import Image, ImageTk  #using PIL to convert JPG images to something Tkinter can use 
from API.api import API
from GUI.SaveFavGui import SaveFavWindow
from GUI.Button import guiButton
from GUI.Textbox import guiTextbox
from GUI.Label import guiLabel
from ImageSelect.ImageSelect import ImageSelect
from DataAccess.DataAccess import DataAccess

class GUI:
    #constructor used to set the size of the window frame
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.size = f"{width}x{height}"
    
    def CreateGUI(self):
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
        
        self.weather_label_image.config(width=self.width, height=self.height)  # Set these dimensions as needed
        self.weather_label_image.pack(pady=10)

        # Using the button class Create a button which will be used to toggle current to 7-day forecast
        sevenDayButton = guiButton(rootWindow, x=700, y=30,text="7-day", command=None)

        # a button widget which will open a 
        # new window on button click.
        # We are using a lambda function to create
        # the SaveFavWindow class object inline. Saves 
        # a few lines of code since it's just gonne be
        # a time creation. We are also passing the
        # reference of the GUI class object to the
        # SavFavWindow. Reference SavFavWindow class
        # in SaveFavGui.py for more info.
        favButton = guiButton(rootWindow, x=600, y=30,text ="Favorite", command=lambda: SaveFavWindow(400,300,self))
        
        # TextBox Creation for searching different locations
        inputtxt= guiTextbox(rootWindow, x=50, y=30, width=10,height=2)

        # Search Location Button Creation.
        # It calls the __locationRetrieval() function
        # used to retrieve data from textbox then
        # perform the checkDisplay() function.
        searchButton = guiButton(rootWindow, x=150, y= 30, text="Search", command=lambda:self.CheckDisplay(inputtxt.TextRetrive()))
        
        # DataAccess creation. Use it to conduct file access
        # so we can retrieve the user default location from
        # default.txt
        default = DataAccess("default.txt")
        data=default.ReadData()
     
        # Fetch and display the weather data for the default location or if
        # no default is set, use the program default setting.
        if data:
            location = data[0].strip()
            self.CheckDisplay(location)
        else:
            self.CheckDisplay()

        # Run the application
        rootWindow.mainloop()  #mainloop() will actively listen for user event such as mouse click and so on. This function will keep the window open and make our program responsive to user actions. Window is only closed when we click on the "x" button top right.

    # Function to update the weather display
    def CheckDisplay(self,location="Miami"):
        api_client=API()   #creating the API object so we can use to retrieve weather info
        weather_data = api_client.GetWeather(location)
        self.weather_label_city.config(text=weather_data[0])
        self.weather_label_temp.config(text=weather_data[1])
        self.weather_label_status.config(text=weather_data[2])

        backgroundImage = ImageSelect()
        photo=backgroundImage.BackgroundSelector(weather_data[2])

        self.weather_label_image.config(image=photo)
        self.weather_label_image.image = photo