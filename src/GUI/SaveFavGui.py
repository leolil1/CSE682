import tkinter as tk
from tkinter import END, Entry, IntVar, Radiobutton
from GUI.Button import guiButton
from GUI.Textbox import guiTextbox
from DataAccess.DataAccess import DataAccess

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
        self.rootWindow.title("Add Favorites") # Add a title to the window
        self.rootWindow.configure(bg='grey')        # Make background color same as the main window
        
        self.__OpenFavorite()                       # Call the private openFavorite() function to create the button and textbox
        
    def __OpenFavorite(self):
        # Create a textbox allow user
        # to enter city location info
        self.inputtxt = guiTextbox(self.rootWindow, x=20, y=20, width=10,height=2)

        # Create a button when user click it'll save the entry
        # in the textbox to the fav.txt file. We allow 5 favs
        # so 5 entry is specified as the second parameter.
        self.saveButton = guiButton(self.rootWindow, x=150, y=20, text="Save To Favorites", command =lambda: self.__WriteData("fav.txt",5))
        
        # Create a button when user click it'll set the default
        # to the entry in the textbox. The default location info
        # is saved to default.txt. And only 1 entry is needed
        # for default.
        self.defaultButton = guiButton(self.rootWindow, x=300, y=20, text="Set As Default", command=self.__SaveDefault)
        
        # Initial Fav location list
        self.__genFavList()
    
    # Function to save data to a file and then call __genFavList to update the list with the new data
    def __WriteData(self,file,numOfLocations):
        # Use the textRetrieve() function from Textbox class to retrieve any data entered
        # at the textbox.
        location = self.inputtxt.TextRetrive()
        
        # DataAccess creation. Use it to conduct file access.
        # We are accessing the file that's specified from "file"
        # parameter
        # The data returned is all the content on the file. It 
        # should be in a list format.
        File = DataAccess(file)
        data=File.ReadData()
            
        # We then append the new location entered to the tail end of this
        # list.
        data.append(location + "\n")
        
        # Because we only allow 5 fav locations, so we will only keep the 
        # last 5 entered locations on the list.
        # So you enter 5 for that, or 1 for set default location.
        if len(data) > numOfLocations:
            data = data[-numOfLocations:]
        
        # At this point, we should have a new list of locations,
        # and it's ready to be written back to the file. Since 
        # it's the same file from what ReadData() operated
        # on, we can continue to use the same object and 
        # now call WriteData() function.
        File.WriteData("w",data)
        
        # Call the genFavListTable function which will generate a new list
        # with the new fav location entered. Will only call it if we are
        # working with the favoriate list instead of setting default.
        if file=="fav.txt":
            self.__genFavList()
    
    # Function to save one of the favorite to default.txt file
    def __SaveDefault(self):
        # Get the currently selected location from the radio buttons
        # and formatted it with a line break at the end.
        location = self.selected_location.get()+"\n"

        # DataAccess creation. Use it to access default.txt.
        # Then we write the one user selected location to
        # the file. Which will then later be read to set up
        # the default location for weather display.
        default = DataAccess("default.txt")
        default.WriteData("w", location)

    # Function to create/update the Favoraite location list
    def __UpdateTable(self):
        # In order to display new saved favorite data, 
        # the easiest way is to simply destroy the old list, 
        # and build a completely new one now including the new 
        # data entered.
        for widget in self.rootWindow.place_slaves():
            if widget.winfo_y() > 50:  # Consider any widget below y-axis<50 is the list
                widget.destroy()       # Then we use destroy() to clear it from memory,
                                       # make room to create a completely new one.

        # DataAccess creation. Use it to access fav.txt.
        # Then we read the content from the file.
        favorite = DataAccess("fav.txt")
        data=favorite.ReadData()
        
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
                deleteButton = guiButton(self.rootWindow, x=150, y=20,text ="x", command=lambda location=line: self.__RemoveLocation(location))
                # Because the buttonis inherited from tk button class, so we can then use 
                # .place() function inherited from parent class to place these buttons 
                # next to our radio buttons above.
                deleteButton.place(x=20, y=60 + i * 30)
    
    # Function to remove the favoriate locations.
    def __RemoveLocation(self, location):
        # DataAccess creation. Use it to access fav.txt.
        # Then we read the content from the file.
        favorite = DataAccess("fav.txt")
        data=favorite.ReadData()

        # Use a for loop, iterate every item on "data"
        # if it equals to location, then that's the one
        # we want to remove, then we skip it from being
        # added to this new list new_data.
        new_data = []
        for line in data:
            if line.strip() != location:
                new_data.append(line)

        # After we dont removing from the list, we write
        # the new_list back to the fav.txt file. Since 
        # it's the same file from what ReadData() operated
        # on, we can continue to use the same object and 
        # now call WriteData() function.
        favorite.WriteData("w", new_data)

        # Update the favorite locations list
        self.__UpdateTable()