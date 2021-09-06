'''A class that can be used to represent a car'''

class Car:
    '''A simple attempt represent a car'''
    def __init__(self,make,model,year):
        '''Attributes in Car class'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.mileage = 0
        
    def decribe_car(self):
        '''print neatly formatted car's informations'''
        print(f"{self.make.title()} {self.model.title()} {self.year}")
        
    def show_odometer(self):
        '''Print a statement showing car's mileage'''
        print(f"This car has {self.odometer} miles on it.")
        
    def update_odometer(self,mileage = 0):
        '''
        Set the odometer to the given value,
        Reject the change if it attempts to roll
        it back
        '''
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles = 0):
        """Add the given amount to the odometer reading"""
        self.odometer += miles
        
        
class ElectricCar(Car):
    '''Inheriting from car to make electric car'''
    
    def __init__(self,name,model,year):
        '''inheriting attributes'''
        super().__init__(name,model,year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print("This car does'nt have a gas tank.")
        


class Battery:
    '''A simple attempt to model electric car battery'''
    def __init__(self,battery_size = 65):
        self.battery_size = battery_size
        
    def my_battery(self):
        '''A statement to see battery size'''
        print(f"The battery of this car is of {self.battery_size}-KwH.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 'N/A'
        if self.battery_size == 65:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car provide {range}-Kms on full charge.")
        
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print('Battery Upgraded, Now enjoy even longer Range.')


        
