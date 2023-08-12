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

    __classes = ["BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"]

    # By default it prints (Cmd)
    prompt = "(hbnb) "  # Prompts '(hbnb) ' on the console

    def emptyline(self):
        '''Overridden method for empty line handler'''

        pass

    def do_quit(self, line):
        '''Quit command to exit the program'''

        return True

    def do_EOF(self, arg):
        '''EOF command to exit the program (Ctrl+D)'''

        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class name doesn't exist **")
            return
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def do_all(self, arg):
        '''Prints all string representation of all instances'''

        args = arg.split()
        inst = storage.all()

        if len(args) == 0:
            for obj in inst.values():
                print(obj)
        else:
            if args[0] not in HBNBCommand.__classes:
                print("** class name doesn't exist **")
                return
            for obj in inst.values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)

    def do_show(self, arg):
        '''Prints a string rep of an instance based on class name and id'''

        args = arg.split()
        inst = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class name doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in inst:
            print("** no instance found **")
        else:
            print(inst["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''

        args = arg.split()
        inst = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class name doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in inst:
            print("** no instance found **")
        else:
            del(inst["{}.{}".format(args[0], args[1])])
            storage.save()

    def do_update(self, arg):
        '''Updates an instance based on the class name and id'''
        args = arg.split()
        inst = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class name doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in inst:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            pass

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
