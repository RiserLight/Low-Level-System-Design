class Bird:

  def __init__(self):
    pass

  def move(self):
    return 'The bird is moving'
  

class Penguin(Bird):

  def __init__(self):
    super().__init__()

  def move(self):
    return 
  
class FlyingBird(Bird):

  def __init__(self):
    super().__init__()

  def fly(self):
    return 'Bird is flying'