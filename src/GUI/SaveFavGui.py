import tkinter as tk
from tkinter import END, Entry, IntVar, Radiobutton
from GUI.Button import guiButton
from GUI.Textbox import guiTextbox

class SaveFavWindow:
    #constructor used to set the size of the window frame and 
    #allow the GUI class reference to be passed in. This will
    #be useful later when we need to call functions in the
    #GUI class object.
    def __init__(self,width,height,guiReference):
        self.width=width
        self.height=height
        self.size = f"{width}x{height}"
        self.gui=guiReference
        
        # Use Tk() function from tkinter to create a favorite window that serve as the frame that holds everything inside
        self.rootWindow = tk.Toplevel()             # Use Toplevel() so the window appear on the top of the main window
        self.rootWindow.geometry(self.size)         # Use self.size to size the window to the values passed in from initialization
        self.rootWindow.title("Favorite Locations") # Add a title to the window
        self.rootWindow.configure(bg='grey')        # Make background color same as the main window
        
        self.__openFavorite()                       # Call the private openFavorite() function to create the button and textbox
        
    def __openFavorite(self):
        # Create a textbox allow user
        # to enter city location info
        self.inputtxt = guiTextbox(self.rootWindow, x=20, y=20, width=10,height=2)

        # Create a button when user click it'll save the entry
        # in the textbox to the fav.txt file. We allow 5 favs
        # so 5 entry is specified as the second parameter.
        self.saveButton = guiButton(self.rootWindow, x=150, y=20, text="Save To Favorites", command =lambda: self.__writeData("fav.txt",5))
        
        # Create a button when user click it'll set the default
        # to the entry in the textbox. The default location info
        # is saved to default.txt. And only 1 entry is needed
        # for default.
        self.defaultButton = guiButton(self.rootWindow, x=300, y=20, text="Set As Default", command=self.__saveDefault)
        
        # Initial Fav location list
        self.__genFavList()
    
    # Function to save data to a file and then call __genFavList to update the list with the new data
    def __writeData(self,file,numOfLocations):
        # Use the textRetrieve() function from Textbox class to retrieve any data entered
        # at the textbox.
        location = self.inputtxt.textRetrive()
        
        # Open the file and read all the data to a list.
        with open(file, "r") as file1:
            data = file1.readlines()
        file1.close()
            
        # We then append the new location entered to the tail end of this
        # list.
        data.append(location + "\n")
        
        # Because we only allow 5 fav locations, so we will only keep the 
        # last 5 entered locations on the list.
        # So you enter 5 for that, or 1 for set default location.
        if len(data) > numOfLocations:
            data = data[-numOfLocations:]
        
        # We then open the file and write all the entries stored in
        # the list back to the file which should only just be the 5 entries
        # for save favorite, and 1 for set default.
        with open(file, "w") as file1:
            file1.writelines(data)
        file1.close()
        
        # Call the genFavListTable function which will generate a new list
        # with the new fav location entered. Will only call it if we are
        # working with the favoriate list instead of setting default.
        if file=="fav.txt":
            self.__genFavList()
    
    # Function to save one of the favorite to default.txt file
    def __saveDefault(self):
        # Get the currently selected location from the radio buttons
        location = self.selected_location.get()

        # Write the selected location to the default.txt file
        with open("default.txt", "w") as file1:
            file1.write(location + "\n")
        file1.close()

    # Function to create the Favoraite location list
    def __genFavList(self):
        # In order to display new saved favorite data, 
        # the easiest way is to simply destroy the old list, 
        # and build a completely new one now including the new 
        # data entered.
        for widget in self.rootWindow.place_slaves():
            if widget.winfo_y() > 60:  # Consider any widget below y-axis<60 is the list
                widget.destroy()       # Then we use destroy() to clear it from memory,
                                       # make room to create a completely new one.

        # Read data from favoriate location file
        with open("fav.txt", "r") as file1:
            data = file1.readlines()
        
        # Use StringVar to keep track of the current values of the
        # selected button. This value will later be passed back to
        # the main gui.py which is then used to update weather info
        # to a new location
        self.selected_location = tk.StringVar(value="miami")
        
        # Display each location as a non-standard radio button
        for i, line in enumerate(data):
            line = line.strip()
            if line:  # Check if the line is not empty
                # Create radio buttons. text&value are all what was read from the file which should just be location info.
                # We then use selected_location to track of that value for the current selected button.
                # Indicatoron=0 means we are using a non-standard radiobutton.
                # Command is to call the checkDisplay() function from the GUI class. We pass the location info of the
                # current selected location to that function.
                radio_button = Radiobutton(self.rootWindow, text=line, value=line, variable=self.selected_location, indicatoron=0,background="light blue",command=lambda:self.gui.checkDisplay(self.selected_location.get()))
                # Position each radio button 30 pixels down
                radio_button.place(x=45, y=60 + i * 30)
                
                # Create a list of buttons that will be used to remove favoriates.
                deleteButton = guiButton(self.rootWindow, x=150, y=20,text ="x", command=lambda location=line: self.__removeLocation(location))
                # Because the buttonis inherited from tk button class, so we can then use 
                # .place() function inherited from parent class to place these buttons 
                # next to our radio buttons above.
                deleteButton.place(x=20, y=60 + i * 30)
    
    # Function to remove the favoriate locations.
    def __removeLocation(self, location):
        # Read data from favoriate location file
        with open("fav.txt", "r") as file1:
            data = file1.readlines()
        file1.close()

        # Remove the selected location from the list
        new_data = []
        for line in data:
            if line.strip() != location:
                new_data.append(line)
        data = new_data

        # Write the updated list back to the file
        with open("fav.txt", "w") as file1:
            file1.writelines(data)
        file1.close()

        # Update the favorite locations list
        self.__genFavList()