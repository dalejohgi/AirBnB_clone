#!/usr/bin/python3
from models.base_model import BaseModel
import models

class Amenity(BaseModel):
    """"""
    name = ""
    
    def __str__(self):
        return ("[City] ({}) {}".format(self.id, self.__dict__))
