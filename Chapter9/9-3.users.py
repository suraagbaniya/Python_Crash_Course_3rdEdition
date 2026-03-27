"""
9-3. Users: Make a class called User . Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile . Make a method called describe_user() that prints a summary of the user’s information . Make another method called greet_user() that prints a personalized greeting to the user .
Create several instances representing different users, and call both methods for each user .
"""

class Users():
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome back!")
        
    def describe_user(self):
        print(f"Following are the information about the user: ")
        print(f"User first name: {self.first_name}")
        print(f"User last name: {self.last_name}")
        print(f"User age: {self.age}")
        
user1 = Users("Sammy", "Jankins", 23)
user1.greet_user()
user1.describe_user()

user2 = Users("Tim", "Potter", 35)
user2.greet_user()
user2.describe_user()