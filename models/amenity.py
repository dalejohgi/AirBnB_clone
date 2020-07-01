#!/usr/bin/python3
"""Amenity Module"""
from models.base_model import BaseModel
import models


class Amenity(BaseModel):
    """Amenities of the place"""
    name = ""

    def __str__(self):
        return ("[City] ({}) {}".format(self.id, self.__dict__))
