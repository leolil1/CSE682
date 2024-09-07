import tkinter as tk
  
# A Button class used to create a button.
# User will enter x&y coordinates, so it
# will be positioned on the main frame
# accordingly 
class guiButton(tk.Button):
    # Constructo used to instantiate an object.
    # We have a few default settings that we'd
    # like our Button to have. Keep the appearance
    # the same.
    def __init__(self, frame, x, y, text="default", command=None, bg="white", fg="black",relief="raised",bd=4):
        #Using lambda function to make the command parameter optional. In theory, a button can be created without having any actions. That's why we are making command optional.
        if command is None:
            command = lambda: None
        
        # Call the parent class (tk.Button) constructor
        super().__init__(frame, text=text, command=command, bg=bg, fg=fg,relief=relief,bd=bd)
        
        # Position the button using the place geometry manager
        self.place(x=x, y=y)