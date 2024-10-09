# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:08:23 2024

@author: LCardenas
"""

import itertools

class InstanceCounterMeta(type):
    """ Metaclass to make instance counter not share count with descendants
    """
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._ids = itertools.count(1)

class InstanceCounter(object, metaclass=InstanceCounterMeta):
    """ Mixin to add automatic ID generation
    """
    def __init__(self):
        self.id = next(self.__class__._ids)