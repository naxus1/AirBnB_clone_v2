#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def delete(self, obj=None):
        """ delete a given object
        """
        if obj is not None:
            id_obj = obj.id
            delete = str(type(obj).__name__) + '.' + obj.id
            if delete in self.__objects.keys():
                del self.__objects[delete]
                self.save()

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """

        if cls:
            all_obj = {}
            clase = cls.__name__
            for key in self.__objects:
                keys = key.split('.')
                if keys[0] == clase:
                    all_obj[key] = self.__objects[key]
            return all_obj
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        '''
            call reload
        '''
        self.reload()
