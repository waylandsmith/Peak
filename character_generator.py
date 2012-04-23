#!/usr/bin/env python

import pickle
import player
from player import PC

# This file defines and generates the character initially!
"""
class PC(object):
    def __init__(self, name, physical, mental, status):
        self.name = name
        self.physical = physical
        self.mental = mental
        self.status = status
"""

"""
def character_creation():
    nom = raw_input("Enter a player name: ")
    body = raw_input("How strong and fit: ")
    body = int(body)
    mind = raw_input("How clever and wise: ")
    mind = int(mind)
    status = "healthy"
#    stat_list = [nom,hip,body,mind]
    return nom,body,mind,status


nom, body, mind, status = character_creation()
#inproperNoun = .lower()
# Lorem = PC(Lorem, 5, 5, 2, 'healthy')
"""

nom = raw_input("Enter a character name: ")
con = raw_input("How strong and fit? ")
wis = raw_input("How smart and wise: ")
status = "healthy"


Nom = PC(nom, con, wis, status)

inproperNoun = Nom.name.lower()


savNom = "save/pc/"+inproperNoun+".creature"
print savNom

savChar = open(savNom, 'w')
pickle.dump(Nom, savChar)

