#!/usr/bin/python3
"""[State Module]"""
from models.base_model import BaseModel
import models


class State(BaseModel):
    """State class for HBnB"""
    name = ""

    def __str__(self):
        """String representation of State instance"""
        return ("[State] ({}) {}".format(self.id, self.__dict__))
