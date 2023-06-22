from car import Car
from abc import ABC

class carriganTyre(Car,ABC):
    def __init__(self,tyreStrength):
        self.tyreStrength[4] = tyreStrength[4]

    def needs_service(self):
        #if or more more values is atleast always greater thn 1
        for i in 4:
            if (self.tyreStrength[i] >= 0.9):
                return False
            
        return True

