import tkinter as tk
# A Button class used to create a button.
# User will enter x&y coordinates, so it
# will be positioned on the main frame
# accordingly  
class guiButton:
  def __init__(self, frame, x,y,text="default", command=None, bg="white",fg="black"):
    #Using lambda function to make the command parameter optional. In theory, a button can be created without having any actions. That's why we are making command optional.
    if command is None:
      command = lambda:None

    #Creating the button and attach it to the main frame
    self.button=tk.Button(frame, text=text, command=command, bg=bg, fg=fg)
    #Then use the place() function to position it
    self.button.place(x=x,y=y)