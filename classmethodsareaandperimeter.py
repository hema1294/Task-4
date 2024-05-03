#Python program to create two class methods area and perimeter which will calculate the area and perimeter

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.141
        return pi * self.radius * self.radius
    
    def perimeter(self):
        pi = 3.141
        return 2 * pi * self.radius
    
result = Circle(5)  # Object for the class

# Example
print("Area of the circle: ", result.area())
print("Perimeter of the circle: ", result.perimeter())


