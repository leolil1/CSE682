from PIL import Image

def imageReturn(imagePath):
  photo=Image.open(imagePath)
  return photo

def backgroundSelector(weather):
    if weather.find("clear")!=-1:
      return "Images\\Sunny.jpg"
    elif weather.find("rain")!=-1:
      return "Images\\Rainy.jpg"
    elif weather.find("scattered")!=-1 or weather.find("broken")!=-1 or weather.find("few")!=-1:
      return "Images\\PartlyCloudy.jpg"
    elif weather.find("overcast")!=-1:
      return "Images\\Cloudy.jpg"
    elif weather.find("snow")!=-1:
      return "Images\\Snowy.jpg"
    else:
      return "No Matching Weather Found"