#!/usr/bin/python3
'''Console Class
'''
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import cmd


class HBNBCommand(cmd.Cmd):
  '''the entry point of the command interpreter'''
  


if __name__ == '__main__':
    HBNBCommand().cmdloop()
