#!/usr/bin/python3
'''
Implements BaseModel class
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''Defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''Instantiation of the attributes'''

        self.id = str(uuid.uuid4())

        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        '''prints class details'''

        name = self.__class__.__name__
        obj = self.id
        doc = self.__dict__
        return ("[{}] ({}) {}".format(name, obj, doc))

    def save(self):
        '''updates the public instance attribute updated_at'''

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__'''

        doc = self.__dict__.copy()
        doc["__class__"] = self.__class__.__name__
        doc["updated_at"] = self.updated_at.isoformat()
        doc["created_at"] = self.created_at.isoformat()
        return (doc)
