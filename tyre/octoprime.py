from car import Car
from abc import ABC

class octoprime(Car , ABC):
    def __init__(self , tyreStrength):
        self.tyreStrength[4] = tyreStrength[4]

    def needs_service(self):
        c = 0
        for i in 4:
            c = c + self.tyreStrength[i]
        if(c<3):
            return True
        else:
            return False