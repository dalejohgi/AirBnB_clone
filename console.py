#!/usr/bin/python3
"""[summary]"""


import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User'] 

    def emptyline(self):
        """Empty line"""
        pass

    def do_prueba(self, arg):

        print(models.classes)

    def do_create(self, class_name):
        """Creates a new instance of BaseModel\n"""
        if class_name == "":
            print("** class name missing **")

        elif class_name == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id"""
        if arg == "":
            print("** class name missing **")

        elif (arg.split())[0] not in self.classes:
            print("** class doesn't exist **")
        
        elif len(arg.split()) == 1:
            print("** instance id missing **")

        else:
            key_str = str(arg.replace(" ", "."))
            try:
                obj_dict = models.storage.all()
                print(obj_dict[key_str])
            except:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "":
            print("** class name missing **")

        elif (arg.split())[0] not in self.classes:
            print("** class doesn't exist **")
        
        elif len(arg.split()) == 1:
            print("** instance id missing **")

        else:
            key_str = str(arg.replace(" ", "."))
            try:
                obj_dict = models.storage.all()
                del obj_dict[key_str]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        if len(arg.split()) == 0  or (arg.split())[0] in self.classes:
            obj_dict = models.storage.all()
            list_str = []
            for key, value in obj_dict.items():
                list_str.append(str(value))
            print (list_str)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>" """
        
        arg_list = arg.split()
        if arg == "":
            print("** class name missing **")

        elif (arg_list[0] not in self.classes):
            print("** class doesn't exist **")
        
        elif len(arg_list) == 1:
            print("** instance id missing **")
        
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            arg_list = arg.split()
            key_str = arg_list[0] + "." + arg_list[1]
            obj_dict = models.storage.all()
            if key_str in obj_dict:
                atribute_name = arg_list[2]
                atribute_value = arg_list[3].replace('"', "")
                setattr(obj_dict[key_str], atribute_name, atribute_value)
                obj_dict[key_str].save()
            else:
                print("** no instance found **")

    def do_quit(self, *args):
        """Quit command to exit the program\n"""
        exit()
    
    def do_EOF(self, *args):
        """Quit command to exit the program\n"""
        print()
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
		
