import tkinter as tk


def openFavorite():
     
    # Use Tk() function from tkinter to create a favorite window
    # that serve as the frame that holds everything inside
    rootWindow = tk.Tk()
    rootWindow.geometry("350x220")
    rootWindow.title("Favoraite Locations")  #configure a title
    rootWindow.configure(bg='grey')  #configure the background color

    # TextBox Creation 
    inputtxt = tk.Text(rootWindow, height = 2, width = 10) 
    inputtxt.pack()

    def writeData():
        location=inputtxt.get(1.0, "end-1c")
        location=location+"\n"
        file1 = open("MyFile.txt","a")
        file1.write(location)
        file1.close()

    # Button Creation
    saveButton = tk.Button(rootWindow, text = "Save",  command = writeData) 
    saveButton.pack() 

    
    
    
 


