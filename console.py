#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
import os
import json
import sys
from models.user import User
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """defines command interpreter"""
    prompt = '(hbnb) '
    classes = ['BaseModel']

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
        """Creates a new instance of User, saves it, and prints the id"""
        if not args:
            print("** class name missing **")
            return
        if args != "User":
            print("** class doesn't exist **")
            return
        user = User()
        user.save()
        print(user.id)

    def do_destroy(self, arg):
        """Deletes a User instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        if args.split()[0] != "User":
            print("** class doesn't exist **")
            return
        obj_id = args.split()[1]
        if not obj_id:
            print("** instance id missing **")
            return
        user = self.get_object_by_id(User, obj_id)
        if not user:
            print("** no instance found **")
            return
        user.delete()
        self.save()

    def do_show(self, arg):
        """Prints the string representation of a User instance"""
        if not args:
            print("** class name missing **")
            return
        if args.split()[0] != "User":
            print("** class doesn't exist **")
            return
        obj_id = args.split()[1]
        if not obj_id:
            print("** instance id missing **")
            return
        user = self.get_object_by_id(User, obj_id)
        if not user:
            print("** no instance found **")
            return
        print(user)

    def do_all(self, arg):
        """Prints all string representation of all instances based on the class name"""
        if not arg:
            print("** class name missing **")
            return

        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return

        instances = storage.all(cls)
        print([str(instance) for instance in instances.values()])

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
            instances = eval(args[0]).all()
            print(len(instances))
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
