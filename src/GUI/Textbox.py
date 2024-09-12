import tkinter as tk
from tkinter import END

# A Textbox class used to create a Textbox.
# User will enter x&y coordinates, so it
# will be positioned on the main frame
# accordingly  
class guiTextbox:
  # Constructo used to instantiate an object.
  # We have a few default settings that we'd
  # like our TextBox to have. Keep the appearance
  # the same.
  def __init__(self, frame, x,y,width=10,height=10,relief="sunken",bd=3):
    
    #Creating the Textbox and attach it to the main frame
    #User can also speicfy width & height to size it.
    self.inputtext=tk.Text(frame,width=width,height=height,bd=bd, relief=relief)
    self.inputtext.place(x=x,y=y)
  
  #Function used to validate user input. Since user
  #should only be entering city names, then this
  #should check user input isalpha() that's it.
  def __UserInputValidation(self, text):
        if all(part.isalpha() for part in text.split()):
            return True
          
  #Function that can be called to retrieve the content
  #entered on the textbox
  def TextRetrive(self):
    text=self.inputtext.get(1.0, "end-1c").strip()
    self.inputtext.delete(1.0, END)  # Clear the input box
    #Only return user input if it pass the input check
    if self.__UserInputValidation(text):
      return text
    else:
      return None