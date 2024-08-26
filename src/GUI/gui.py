import tkinter as tk
from tkinter import END
from PIL import Image, ImageTk  #using PIL to convert JPG images to something Tkinter can use 
from API.api2 import getWeather
from GUI.SaveFavGui import openFavorite
from ImageSelector.ImageSelector import backgroundSelector,imageReturn

def createGUI():
    
    
    # Function to update the weather display
    def checkDisplay(location="Miami"):
        weather_data = getWeather(location)
        weather_label_city.config(text=weather_data[0])
        weather_label_temp.config(text=weather_data[1])
        weather_label_status.config(text=weather_data[2])

        path=backgroundSelector(weather_data[2])
        tmp_photo=imageReturn(path)
        
    
        #Loading images
        #Tkinter does not support JPG.
        #Since images are in JPG format, we have to first load it
        #then convert it using PhtoImage so tkinter can understand.
        photo = ImageTk.PhotoImage(tmp_photo)
        image_label=tk.Label(rootWindow,image=photo)
        image_label.pack()

        # Update the existing image label with the new image
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to prevent garbage collection

    # Use Tk() function from tkinter to create a root window
    # that serve as the frame that holds everything inside
    rootWindow = tk.Tk()
    rootWindow.title("Weather APP")  #configure a title
    rootWindow.configure(bg='grey')  #configure the background color

    # Create a text box to display the weather information
    #we use Label() to add a text box. This value will be updated later in checkDisplay() function to reflect temp data
    #we use pack() to position the label. Right now it's 20pixles of padding above and below the text box. As we add more #information, this is going to change.
    
    weather_label_city = tk.Label(rootWindow, text="Fetching weather data...", bg='grey', fg='white', font=("Arial", 14))
    weather_label_city.pack(pady=20)
    weather_label_temp = tk.Label(rootWindow, text="Fetching weather data...", bg='grey', fg='white', font=("Arial", 14))
    weather_label_temp.pack(pady=20)
    weather_label_status = tk.Label(rootWindow, text="Fetching weather data...", bg='grey', fg='white', font=("Arial", 14))
    weather_label_status.pack(pady=20)

    # Create a button which will be used to toggle current to 7-day forecast
    toggle = tk.Button(rootWindow, text="7-day", command=checkDisplay, bg='white', fg='black')
    toggle.pack(pady=10)

    # a button widget which will open a 
    # new window on button click
    fav = tk.Button(rootWindow, text ="Favorite", command = openFavorite, bg='white', fg='black')
    fav.pack(pady = 10)

    # TextBox Creation for searching different locations
    inputtxt = tk.Text(rootWindow, height=2, width=10)
    inputtxt.pack(pady=0, padx=0)

    def locationRetrival():
        location = inputtxt.get(1.0, "end-1c").strip()
        inputtxt.delete(1.0, END)  # Clear the input box
        checkDisplay(location)

    # Button Creation
    saveButton = tk.Button(rootWindow, text="Search", command=locationRetrival)
    saveButton.pack(pady=10, padx=10)

    # Fetch and display the weather data
    checkDisplay()

    # Run the application
    rootWindow.mainloop()  #mainloop() will actively listen for user event such as mouse click and so on. This function will keep the window open and make our program responsive to user actions. Window is only closed when we click on the "x" button top right.