#/usr/bin/env python

import os
import pickle

# This file defines and generates the character initially!
# Player stats:

class PC(object):
    def __init__(self, name, hp, physical, mental, status):
        self.name = name
        self.hp = hp
        self.physical = physical
        self.mental = mental
        self.status = status

def character_creation():
    nom = raw_input("Enter a player name: ")
    hip = raw_input("how many hit points? ")
    hip = int(hip)
    body = raw_input("How strong and fit: ")
    body = int(body)
    mind = raw_input("How clever and wise: ")
    mind = int(mind)
#    stat_list = [nom,hip,body,mind]
    return nom,hip,body,mind


nom, hip, body, mind = character_creation()
#inproperNoun = .lower()
# Lorem = PC(Lorem, 5, 5, 2, 'healthy')
Nom = PC(nom, hip, body, mind, 'healthy')

inproperNoun = Nom.name.lower()


savNom = "save/pc/"+inproperNoun+".creature"
print savNom

savChar = open(savNom, 'w')
pickle.dump(Nom, savChar)


"""
print Nom.name
print Nom.hp
print Nom.physical
print Nom.mental
print Nom.status
"""
