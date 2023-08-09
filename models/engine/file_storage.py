#!/usr/bin/python3
"""This script is the file storage"""


import json
import os


class FileStorage:

    """class for storing data in a file"""
    __file_path = "file.jason"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        self.__objects = obj_dict



