from Shape import shape

class triangle(shape): # highlight that triangle inherits from shape
    
    def __init__(self, base, height, colour): # input params of base and height
        super().__init___(colour) = colour
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 1.5
    
