#!/usr/bin/python3
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""[summary]"""

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] =  obj #Maybe sea mejor hallar el nombre de la clase de una manera mas genérica

    def save(self):
        # Tenemos __objets un dic de obj tipo key = BaseModel.id value = __str__ representation
        # 1 - convertir objeto por objeto en diccionario para tener un dic de dicts de obj
        # 2 - usar dump para escribir en el archivo el json de cada objeto
        obj_json = {}
        for key in FileStorage.__objects:
            obj_json[key] = FileStorage.__objects[key].to_dict() # Dic de la forma BaseMode.id : dic representation
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_json, file)
        
    def reload(self):
        """[summary]"""
        class_dict ={
            "BaseModel" : BaseModel, 
            "User" : User, 
            "Place" : Place, 
            "State" : State, 
            "City" : City,
            "Amenity" : Amenity, 
            "Review" : Review
            }
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_json = json.load(file)
            for key, value in obj_json.items():
                FileStorage.__objects[key] = class_dict[obj_json[key]["__class__"]](**value)
        except:
            pass
