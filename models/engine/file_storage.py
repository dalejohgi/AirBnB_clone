#!/usr/bin/python3
import json
import models
from models.base_model import BaseModel
"""[summary]"""

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["BaseModel." + obj.id] = obj
    
    def save(self):
        dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)
    
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except:
            pass
