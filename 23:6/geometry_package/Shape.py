from abc import ABC, abstractmethod

class shape(ABC):

    def __init__(self, colour):
        self.colour = colour

    @abstractmethod
    def area(self):
        pass

    def area_cm(self):
        return self.area() * 100
    
