#!/usr/bin/python3
"""[BaseModel Module]
"""


import uuid
import models
import datetime


class BaseModel():
    """
    [Base Class]
    """

    def __init__(self, *args, **kwargs):
        """Initializer method"""

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.created_at = (datetime.datetime.strptime(
                                       (kwargs["created_at"]),
                                       "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "updated_at":
                    self.updated_at = (datetime.datetime.strptime(
                                       (kwargs["updated_at"]),
                                       "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)

    def __str__(self):
        """__str__ method"""

        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """Saves an object of BaseModel"""

        models.storage.save()
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """Return the dictionary representation of an object"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()

        return my_dict
