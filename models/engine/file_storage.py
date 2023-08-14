#!/usr/bin/python3
'''
Implements FileStorage class
'''
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''serializes and deserializes instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''

        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''

        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        '''serializes __objects to the JSON file'''

        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        '''deserializes the JSON file to __objects'''

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path) as f:
            objdict = json.load(f)
            for o in objdict.values():
                cls_name = o["__class__"]  # take the value of __class__ key
                del o["__class__"]  # delete the __class__ item (name)
                self.new(eval(cls_name)(**o))  # create new instance of clsname
