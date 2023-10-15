#!/usr/bin/python3
"""entry point of the command interpreter"""

import cmd
import os
import json
import sys
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """defines command interpreter"""
    prompt = '(hbnb) '
    instances = []
    classes = ['BaseModel']

    def __init__(self):
        """ init of the class"""
        self.__class__.instances.append(self)

        @classmethod
        def all(cls):
            return cls.instances

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        """Display help for the quit command"""
        print("Quit the program")

    def help_EOF(self):
        """Display help for the EOF command"""
        print("Exit the program")

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        classes = ["BaseModel", "city", "place", "state", "user"]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_destroy(self, arg):
        """Deletes a User instance based on the class name and id"""
        classes = ["BaseModel", "user", "place", "city", "state"]
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_show(self, arg):
        """Prints the string representation of a User instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "User":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_all(self, arg):
        """Print all instances"""
        classes = ["BaseModel", "User", "Place", "Review", "City"]
        if arg == "":
            objects = self.__objects.values()
        else:
            class_name = arg.split()[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """Update an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

    def do_count(self, arg):
        """Print the number of instances of a class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            instances = self.classes[class_name]
            print(len(instances))
        except NameError:
            i
        print("** class doesn't exist **")

    def do_help(self, arg):
        if arg == "":
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("help           - List available commands")
            print("quit           - Exit the program")
        else:
            if arg == "help":
                print("check help manual")
            elif arg == "quit":
                print("type quit")
            else:
                print("No help available for '{}'".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
