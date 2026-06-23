from Shape import shape

class circle(shape):

    def __init__(self, radius, colour):
        super().__init__(colour) = colour
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

