from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Circle (Shape):

  def __init__(self,radius:float)->None:
    self.__radius=radius

  def area(self)->float:
    return 3.14*self.__radius*self.__radius
  
  def perimeter(self)->float:
    return 2*3.14*self.__radius
  
class Reactange(Shape):

  def __init__(self,height:float,width:float):
    self.__height=height
    self.__width=width

  def area(self)->float:
    return self.__height*self.__width
  
  def perimeter(self)->float:
    return 2*(self.__height+self.__width)
  
class ShapeParametersComputaion:

  def __init__(self,shapes):
    self.__shapes=shapes

  def calculate_total_area(self)->float:
    total_area=0
    for shape in self.__shapes:
      total_area+=shape.area()
    return total_area

  def calculate_total_perimeter(self)->float:
    total_perimeter=0
    for shape in self.__shapes:
      total_perimeter+=shape.perimeter()
    return total_perimeter
    

class Xyz:
  def __init__(self:Xyz):
    pass