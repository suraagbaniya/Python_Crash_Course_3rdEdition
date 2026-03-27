"""
9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three different instances from the class, and call describe_restaurant() for each instance .
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
        
first_restaurant = Restaurant("thakali", "nepali")
first_restaurant.describe_restaurant()

second_restaurant = Restaurant("biryani","indian")
second_restaurant.describe_restaurant()

three_restaurant = Restaurant("mcdonald", "fast food")
three_restaurant.describe_restaurant()

