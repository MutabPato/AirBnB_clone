#!/usr/bin/python3
"""
Command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.engine import file_storage
import shlex
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Set the command interpreter up
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Exits the command interpreter
        """
        return (True)

    def do_EOF(self, line):
        """
        Exits when end of file is reached
        """
        return (True)

    def help_quit(self):
        print('Quit command to exit the program\n')

    def help_EOF(self):
        print('Exits when end of file is reached')

    def emptyline(self):
        """
        Empty line + ENTER executes nothing
        """
        pass

    def do_create(self, line):
        """
        creates a new instance of BaseModel and print its id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints string representation of an instance based on class name and id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instance = models.storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = models.storage.all()
        instance = all_instances.get(key)
        if instance is None:
            print("** no instance found **")
            return
        del all_instances[key]
        models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = shlex.split(line)

        if args[0] not in globals():
            print("** class doesn't exist **")
            return

        all_instances = models.storage.all()
        list_instances = []
        for key in all_instances:
            list_instances.append(str(all_instances.get(key)))
        print(list_instances)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_instances = models.storage.all()
        instance = all_instances.get(key)
        if instance is None:
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")

        attibutes = instance.__dict__
        setattr(instance, args[2], args[3])
        instance.save

    def help_create(self):
        print("Creates a new instance of BaseModel, \
                saves it (to the JSON file) and prints the id")

    def help_show(self):
        print("Prints the string representation of an instance \
                based on the class name and id")

    def help_destroy(self):
        print("Deletes an instance based on the class name and id")

    def help_all(self):
        print("Prints all string representation of all instances \
                based or not on the class name")

    def help_update(self):
        print("Updates an instance based on the class name and \
                id by adding or updating attribute")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
