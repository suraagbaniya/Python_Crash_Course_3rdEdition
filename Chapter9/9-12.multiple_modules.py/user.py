''' This modules stores Users class'''

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