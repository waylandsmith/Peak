#!/usr/bin/env python

import random
import pickle
import player

"""
class PC(object):
    def __init__(self, name, hp, physical, mental, status):
        self.name = name
        self.hp = hp
        self.physical = physical
        self.mental = mental
        self.status = status
"""

loadChar = open('save/pc/matt.creature', 'r+')

pc = pickle.load(loadChar)

# print pc.hp
