class Shape:

    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return self.height * self.base * 0.5
    
shapes = [Circle(3.5), Triangle(3, 5)]

for shape in shapes:
    print(shape.calculate_area())