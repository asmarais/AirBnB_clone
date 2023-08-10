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

    # By default it prints (Cmd)
    prompt = "(hbnb) "  # Prompts '(hbnb) ' on the console

    def emptyline(self):
        '''Overridden method for empty line handler'''

        pass

    def do_quit(self, line):
        '''Quit command to exit the program'''

        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program'''

        return True

    def execute(self, *args, **kwargs):
        '''command interpreter handler'''

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
