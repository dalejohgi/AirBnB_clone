#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        BaseModel.__init__(self)
    
    def __str__(self):
        return ("[User] ({}) {}".format(self.id, self.__dict__))
