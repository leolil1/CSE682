class DataAccess:
  # Constructor, during object creation, we will specify the file
  # we'll be working on.
  def __init__(self,FileName):
    self.FileName=FileName
    self.ReturnData=None
  
  # Function used to simply read data from a file (for now)
  # then return that data
  def ReadData(self):
    #Open the file to read, then read all the data and
    #store it to our private variable which will then
    #be returned back to the caller
    with open(self.FileName, "r") as file1:
            self.ReadData = file1.readlines()
    file1.close()
    #Once file reading is finished. The data is returned
    return self.ReadData
  
  # Function used to write data to a file (for now)
  # We gonne specify the name of the file to write to,
  # how we gonne write to it (overwrite completely, or just append),
  # and the data.
  def WriteData(self, WriteType, Data):
    # Use this if WriteType is w meaning just overwrite
    # everything on file.
    if WriteType=="w":
      with open(self.FileName, "w") as file1:
          file1.writelines(Data)
      file1.close()
    
    # Use this if WriteType is a meaning we are appending
    # to existing data on file.
    if WriteType=="a":
      with open(self.FileName, "a") as file1:
          file1.writelines(Data)
      file1.close()