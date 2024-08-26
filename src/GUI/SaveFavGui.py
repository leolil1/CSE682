import tkinter as tk
from tkinter import END, Entry

def openFavorite():
     # Use Tk() function from tkinter to create a favorite window that serve as the frame that holds everything inside
    rootWindow = tk.Toplevel()
    rootWindow.geometry("400x300")
    rootWindow.title("Favorite Locations")
    rootWindow.configure(bg='grey')

    # TextBox Creation
    inputtxt = tk.Text(rootWindow, height=2, width=10)
    # Using grid layout because to create a table we have to use grid layout, and tkinter doesn't allow mix and match. so keep everything grid
    inputtxt.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    # Function to save data ato a file and then call updateTable to update the table with the new data
    def writeData():
        location = inputtxt.get(1.0, "end-1c").strip()
        file1=open("fav.txt", "a")
        file1.write(location + "\n")
        file1.close()
        inputtxt.delete(1.0, END)  # Clear the input box
        updateTable()  # call the updateTable function which will refresh the table with new data entered.

    # Button Creation
    saveButton = tk.Button(rootWindow, text="Save", command=writeData)
    saveButton.grid(row=1, column=0, padx=10, pady=10, columnspan=1)

    # Function to create/update the table
    def updateTable():
        # In order to display new saved favorite data, the easiest way is to simply destroy the old table, and build a completely new one now including the new data entered.
        for widget in rootWindow.grid_slaves():
            # TextBox and Button should all be on row 1, so anything below them should just be table which we'll then destroy() to make room to generate a new one
            if int(widget.grid_info()["row"]) > 2:
                widget.destroy()

        # Read data from file and display in table format
        file1=open("fav.txt", "r")
        data = file1.readlines()
        file1.close()

        #for loop used to enumerate the data read from file
        for i, line in enumerate(data):
            line = line.strip()
            e1 = Entry(rootWindow, width=20, fg='blue', font=('Arial', 12, 'bold'))
            e1.grid(row=i + 2, column=0, padx=5, pady=5)
            e1.insert(END, str(i + 1))  # Display line number

            e2 = Entry(rootWindow, width=30, fg='blue', font=('Arial', 12, 'bold'))
            e2.grid(row=i + 2, column=1, padx=5, pady=5, columnspan=2)
            e2.insert(END, line)  # Display the content of the line

    # Initial table population
    updateTable()