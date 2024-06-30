class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
class Circle:
    
    def __init__(self,radius):
        self.radius=radius

class AreaCalculator:
    def calculate_total_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.calculate_area()
            elif isinstance(shape, Circle):
                total_area += shape.calculate_area()
            # Add more shape types here
        return total_area
    

# In this example, the AreaCalculator class is not closed for modification. If you want to add a new shape type, you need to modify the calculate_total_area method by adding a new elif block to handle the new shape type. This violates the open closed principle.