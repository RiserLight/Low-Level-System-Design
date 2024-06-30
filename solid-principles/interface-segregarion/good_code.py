from abc import ABC,abstractmethod

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Movable(ABC):
    @abstractmethod
    def move(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Fish(Eatable, Movable, Swimmable):
    pass

class Bird(Eatable, Movable, Flyable):
    pass