import tkinter as tk

# A Label class inherited from the tkinter Label
# We wanted to customize this so we can have some
# our own unique initial values. Or more future
# customizations.    
class guiLabel(tk.Label):
    def __init__(self, frame, text="Fetching weather data...", bg='grey', fg='white', font=("Arial", 14), image=None, **kwargs):
        # Initialize the parent class
        super().__init__(frame, text=text, bg=bg, fg=fg, font=font, **kwargs)