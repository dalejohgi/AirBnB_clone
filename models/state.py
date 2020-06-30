#!/usr/bin/python3
from models.base_model import BaseModel
import models

class State(BaseModel):
    """"""
    name = ""
    
    def __str__(self):
        return ("[State] ({}) {}".format(self.id, self.__dict__))
