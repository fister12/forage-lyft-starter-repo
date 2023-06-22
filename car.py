from abc import ABC


class Car(ABC):
    def __init__(self,Engine,Battery):
        self.Engine = Engine
        self.Battery = Battery

    def needs_service(self):
        if(self.Engine.needs_service() or self.Batter.needs_service()):
            return True
        else:
            return False