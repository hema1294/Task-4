#Python program to create proper member variable inside the task if required and use them when necessary
# For example for this task create a class private variable named pi = 3.141

class Circle:
    __pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    def area (self):
        return Circle.__pi * self.radius * self.radius
    
result = Circle(5)   # Object for the class

# Example
print("Area of the circle: ", result.area())


