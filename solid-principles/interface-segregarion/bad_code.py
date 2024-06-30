from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fly(self):
        pass
    
    @abstractmethod
    def swim(self):
        pass
    
