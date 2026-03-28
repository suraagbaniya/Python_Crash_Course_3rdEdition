''' A module that stores restaurant class'''

class Restaurant():
    ''' This class models a restaurant'''
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"The {self.name.title()} restaurant serves {self.cuisine_type.title()} cuisine.")
        
    def open_restaurant(self):
        print(f"The restaurant is open.")
        