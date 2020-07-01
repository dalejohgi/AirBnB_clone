#!/usr/bin/python3
"""[File Storage Module]"""


import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class for HBnB"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary of objects"""
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """Serialize the dictionary and store it to a Json file"""

        obj_json = {}
        for key in FileStorage.__objects:
            obj_json[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_json, file)

    def reload(self):
        """Deserializes a json file, and recreate the objects in it"""

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_json = json.load(file)
            for key, value in obj_json.items():
                FileStorage.__objects[key] = (class_dict[
                                              obj_json[key]["__class__"]]
                                              (**value))
        except:
            pass
