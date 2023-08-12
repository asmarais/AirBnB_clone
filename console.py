#!/usr/bin/python3                                                                                                                                                      
"""This script is he cmd model"""


import cmd
from models import storage


class HBNBCommand(cmd.Cmd):


    """a program called console.py that contains the entry point of the command interpreter"""


    prompt = "(hbnb) "
    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def do_empty(self, line):
        pass

    def do_create(self, line):
        if line is None or line == "":
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            cl = storage.classes()[line]()
            cl.save()
            print(cl.id)

    def do_show(self, line):
        if line is None or line == "":
            print("** class name missing **")
        else:
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        if line is None or line == "":
            print("** class name missing **")
        else:
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        list1 = []
        if line != "":
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                for key, item in storage.all().items():
                    if item.__class__.__name__ == word[0]:
                        list1.append(str(obj))
        else:
            for key, item in storage.all().items():
                list1.append(str(obj))

    def do_update(self, line):
        if line is None or line == "":
            print("** class name missing **")
        else:
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                elif len(word) < 3:
                    print("** attribute name missing **")
                elif len(word) < 4:
                    print("** value missing **")
                elif len(word) == 4:
                    pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
