'''This module stores admin class'''

from user import Users
from privileges import Privileges

class Admin(Users):
    
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.admin_privileges = Privileges()