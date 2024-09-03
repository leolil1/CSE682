from PIL import Image, ImageTk

# ImageSelect class will be used to select appropriate
# images for background display
class ImageSelect:
  # Constructor, when object is created, we will
  # initialize the imagePath variable to have no
  # value for now.
  def __init__(self):
    self.imagePath=None

  #Function to load the image then return it
  def imageReturn(self, imagePath):
      # Check if the image is valid, if so return it
      if imagePath != "No Matching Weather Found":
          # Tkinter does not support JPG.
          # Since images are in JPG format, we have to first load it
          # then convert it using PhtoImage so tkinter can understand.
          tmp_photo = Image.open(imagePath)
          tmp_photo = tmp_photo.resize((500, 500), Image.LANCZOS)
          photo = ImageTk.PhotoImage(tmp_photo)
          return photo
      else:
        return None
  
  #Function to select the photo based on weather condition
  def backgroundSelector(self, weather):
      # Assign the correct image path based on the weather
      if "clear" in weather:
          self.imagePath = "Images\\Sunny.jpg"
      elif "rain" in weather:
          self.imagePath = "Images\\Rainy.jpg"
      elif any(word in weather for word in ["scattered", "broken", "few"]):
          self.imagePath = "Images\\PartlyCloudy.jpg"
      elif "overcast" in weather:
          self.imagePath = "Images\\Cloudy.jpg"
      elif "snow" in weather:
          self.imagePath = "Images\\Snowy.jpg"
      else:
          self.imagePath = "No Matching Weather Found"
      
      # Return the image
      return self.imageReturn(self.imagePath)
