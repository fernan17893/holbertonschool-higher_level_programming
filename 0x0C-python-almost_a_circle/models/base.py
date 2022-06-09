#!/usr/bin/python3
""" Class Base """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns Json representation of list_dictionaries """
        if(list_dictionaries is None):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of list_obj """
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as a_file:
            if list_objs is None:
                return a_file.write(cls.to_json_string(None))
            my_list = []
            for i in list_objs:
                my_list.append(i.to_dictionary())
            return a_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 3)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as a_file:
                pass
        except a_file.DoesNotExist:
            return []
        with open(cls.__name__ + ".json", "r", encoding="utf-8") as a_file:
            instanceList = cls.from_json_string(a_file.read())
            inst_list = []
            for dic in instanceList:
                inst_list.append(cls.create(**dic))
            return inst_list
