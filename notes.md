# General Information 

1. If any of the sql queries is wromng then connection object will automatically close in psycopg2.

2. use draw.io for drawing before coding the actual things (i.e for design purpose)

# Python Foundations

# Object Oriented Programming

1. class Xyz:
def __init__(self:Xyz):
pass
What is mistake in this code
Answer
The mistake in the provided code is the use of the self:Xyz syntax in the __init__ method.
In Python, the self parameter is a convention used to refer to the instance of the class within the class methods. It is not a part of the method signature and should not be explicitly typed.
The correct way to define the __init__ method in a Python class is:
python
class Xyz:
    def __init__(self):
        pass

The self parameter is automatically passed by the Python interpreter when the method is called on an instance of the class. It is not necessary to explicitly specify the type of the self parameter.
The incorrect usage self:Xyz is not valid Python syntax and will result in a syntax error when trying to run the code.
The correct way to define the class is:
python
class Xyz:
    def __init__(self):
        pass

This way, the __init__ method is defined correctly, and the self parameter is used to refer to the instance of the Xyz class within the method.

2. In this class what are the abstractmethods define:
from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def eat(self):
        pass

    def move(self):
        pass

    def fly(self):
        pass

    def swim(self):
        pass
Answer
In the provided code, the abstractmethod decorator is used to define the abstract methods in the Animal class.
The abstract methods in this class are:
eat(self):
This method is marked as an abstract method using the @abstractmethod decorator.
Any concrete subclass of Animal must implement this method.
The other methods in the Animal class:
move(self):
This method is not marked as abstract, so it is a concrete method.
Subclasses of Animal can either inherit this implementation or override it.
fly(self):
This method is not marked as abstract, so it is a concrete method.
Subclasses of Animal can either inherit this implementation or override it.
swim(self):
This method is not marked as abstract, so it is a concrete method.
Subclasses of Animal can either inherit this implementation or override it.
The purpose of defining the eat method as an abstract method is to ensure that any concrete subclass of Animal must provide an implementation for this method. This is a way to enforce the Liskov Substitution Principle (LSP) of the SOLID principles, as subclasses must be substitutable for their base classes.
By making the eat method abstract, you are defining a contract that all Animal subclasses must follow. This helps maintain the consistency and correctness of the Animal hierarchy.

3. 

# Solid principles

1. S(Single responsibility):- Whatever class you create that should have only one responsibility.
To check if a class obeys single responsibility , ask the question : What does this class do? Any if in answer you get AND that means rule is violated. A class should have only one reason to change.
If a class has more than one responsibility, it becomes coupled. Changes to one responsibility can adversely impact the other responsibilities.

2. O(Open for extension , closed for modification):- Whatever class or inteface you create no one should be able to add any method or property to it. But others can extend and add properties and methods to it.

3. L(Liskov Substitution):- The liskov substitution principle states that object of a super class should be replacable with the objects of a subclass without affecting the correctness of the program.

4. I(Interfaqce segregation): We should keep only those methods in inteface which is required. We should not force the client to implement unnecessarily methods that is does not require.

5. D(Dependency Inversion): Higher level modules should not depend on low level modules . Instead both should depend on abstraction.


# Design Patterns:-


