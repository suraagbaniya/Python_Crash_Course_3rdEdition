"""
9-1. Restaurant: Make a class called Restaurant . The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type . Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indi- cating that the restaurant is open .
Make an instance called restaurant from your class . Print the two attri- butes individually, and then call both methods .
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
        
my_restaurant = Restaurant("thakali", "nepali")
print(my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
