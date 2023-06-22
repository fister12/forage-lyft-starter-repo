from datetime import date
from car import Car

import Engine
import Battery
class carFactory:
    def  create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        car1 = Car()
        car1.Engine = Engine.capuletEngine()
        car1.Battery = Battery.splinderBattery()
        car1.Engine.current_mileage = current_mileage
        car1.last_service_mileage = last_service_mileage
        car1.Battery.last_service_date = last_service_date
        car1.Battery.current_date = current_date

        return car1
    def  create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        car1 = Car()
        car1.Engine = Engine.willoughbyEngine()
        car1.Battery = Battery.splinderBattery()
        car1.Engine.current_mileage = current_mileage
        car1.last_service_mileage = last_service_mileage
        car1.Battery.last_service_date = last_service_date
        car1.Battery.current_date = current_date

        return car1
    
    def  create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        car1 = Car()
        car1.Engine = Engine.willoughbytEngine()
        car1.Battery = Battery.nubbinBattery()
        car1.Engine.current_mileage = current_mileage
        car1.last_service_mileage = last_service_mileage
        car1.Battery.last_service_date = last_service_date
        car1.Battery.current_date = current_date

        return car1        

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        car1 = Car()
        car1.Engine = Engine.capuletEngine()
        car1.Battery = Battery.nubbinBattery()
        car1.Engine.current_mileage = current_mileage
        car1.last_service_mileage = last_service_mileage
        car1.Battery.last_service_date = last_service_date
        car1.Battery.current_date = current_date

        return car1        
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        car1 = Car()
        car1.Engine = Engine.sternmanEngine()
        car1.Battery = Battery.splindlerBattery();
        car1.Engine. warning_light_is_on = warning_light_on
        car1.Battery.last_service_date = last_service_date
        car1.Battery.current_date = current_date

        return car1 