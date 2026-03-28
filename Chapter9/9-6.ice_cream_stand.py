"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of
the class will work; just pick the one you like better . Add an attribute called flavors that stores a list of ice cream flavors . Write a method that displays these flavors . Create an instance of IceCreamStand, and call this method .
"""

class Restaurant():
    ''' This class models a restaurant'''
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"The {self.name.title()} restaurant serves {self.cuisine_type.title()} cuisine.")
        
    def open_restaurant(self):
        print(f"The restaurant is open.")
        
class IceCreamStand(Restaurant):
    ''' This child class tries to model a Ice cream Stand Restaurant'''
    
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ["Vanilla", "StrawBerry", "Chocolate"]
    
    def describe_flavors(self):
        for eachFlavor in self.flavors:
            print(eachFlavor)
            
restaurant1 = IceCreamStand("Best Icecreams", "Icecream")
restaurant1.describe_flavors()