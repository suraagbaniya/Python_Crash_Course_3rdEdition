"""
9-8. Privileges: Write a separate Privileges class . The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7 . Move the show_privileges() method to this class . Make a Privileges instance as an attribute in the Admin class . Create a new instance of Admin and use your method to show its privileges .
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

class Admin(Users):
    
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.admin_privileges = Privileges()
        

class Privileges():
    
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "has root access"]
    
    def show_privileges(self):
        print("User privileges are as follows:")
        for everyPrivilege in self.privileges:
            print(everyPrivilege)

user1 = Admin("Jhon", "Doe", 25)
user1.admin_privileges.show_privileges()