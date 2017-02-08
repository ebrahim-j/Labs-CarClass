class Car(object):
  
  #setting default values incase no input provided
  def __init__(self, name='General', model='GM', vehicle_type=None, speed = 0):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type
    self.speed = speed

    #adjustment of wheels depending on car type
    if self.vehicle_type != 'trailer':
      self.num_of_wheels = 4
    else:
      self.num_of_wheels = 8
      
    #considering different doors specifications
    if self.name =='Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
      
  #check car type
  def is_saloon(self):
    if self.vehicle_type != 'trailer':
      self.vehicle_type == 'saloon'
      return True
    else:
      return False
        
        

  def drive(self, drive_speed):
    if drive_speed == 3:
      self.speed = 1000
    elif drive_speed == 7:
      self.speed = 77
      
    return self
