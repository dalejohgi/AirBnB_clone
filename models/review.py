#!/usr/bin/python3
from models.base_model import BaseModel
import models

class Review(BaseModel):
    """"""
    place_id = ""
    user_id = ""
    text = ""
    
    def __str__(self):
        return ("[Review] ({}) {}".format(self.id, self.__dict__))
