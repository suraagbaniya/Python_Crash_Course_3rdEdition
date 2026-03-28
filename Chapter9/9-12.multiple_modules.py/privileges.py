''' This module stores privileges class'''

class Privileges():
    
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "has root access"]
    
    def show_privileges(self):
        print("User privileges are as follows:")
        for everyPrivilege in self.privileges:
            print(everyPrivilege)