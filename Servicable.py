from car import Car

class servicable(Car):
    def needs_service(self):
        return super().needs_service()