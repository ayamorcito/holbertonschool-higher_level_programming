#!/usr/bin/python3
""" base.py """

class Base:
    """ base class of project """
    
    __nb_objects = 0

    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base__nb_objects += 1
            self.id = self.__nb_objects
