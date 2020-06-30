#!/usr/bin/python3
from models.base_model import BaseModel
import models

class City(BaseModel):
    """"""
    state_id = ""
    name = ""
    
    def __str__(self):
        return ("[City] ({}) {}".format(self.id, self.__dict__))
