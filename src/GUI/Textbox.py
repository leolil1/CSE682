import tkinter as tk
from tkinter import END

# A Textbox class used to create a Textbox.
# User will enter x&y coordinates, so it
# will be positioned on the main frame
# accordingly  
class guiTextbox:
  def __init__(self, frame, x,y,width=10,height=10):
    
    #Creating the Textbox and attach it to the main frame
    #User can also speicfy width & height to size it.
    self.inputtext=tk.Text(frame,width=width,height=height)
    self.inputtext.place(x=x,y=y)

  #Function that can be called to retrieve the content
  #entered on the textbox
  def textRetrive(self):
    text=self.inputtext.get(1.0, "end-1c").strip()
    self.inputtext.delete(1.0, END)  # Clear the input box
    return text