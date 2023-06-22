from abc import ABC 

#This class is only used to find the last service date and current date and check if the specific battery needs servicing
class subbinBattery(ABC):
    def __init__(self,last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date 
    def needs_service(self):
        if(self.current_date-self.last_service_date > 3):
            return True
        else:
            return False