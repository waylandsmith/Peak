#!/usr/bin/env python

import pickle
import player
from player import PC

# This file defines and generates the character initially!

def charGen():
    nom = raw_input("what is your name? ")
    con = raw_input("How strong and fit? ")
    con = int(con)
    wis = raw_input("How smart and wise? ")
    wis = int(wis)
    spe = raw_input("How fleet of foot and mind? ")
    spe = int(spe)
    status = "healthy"

    Nom = PC(nom, con, wis, spe, status)

    inproperNoun = Nom.name.lower()

    savNom = "save/pc/"+inproperNoun+".creature"
    print savNom

    savChar = open(savNom, 'w')
    pickle.dump(Nom, savChar)

#    savIndex = open(save/saver.py, 'w')

    
class Loader(object):
    def __init__(self,name):
        self.name = name
#        self.loadFile = loadFile
        
    def loadGame(self):
        # eventually, use a for loop and an index 
        loading = True
        while loading:
            loaded = raw_input("what character do you want to load? ")
            if loaded.lower() in ['matthew']:
                person = "save/pc/matthew.creature"
                loading = False
            elif loaded.lower() in ['maria']:
                person = "save/pc/maria.creature"
                loading = False
            else:
                print "not a save file!"
        self.name = person
        return self.name
         
load_instance = Loader("default.creature")


def loadThings():
    loadTerm = "save/pc/" + str(load_instance.name)
    loadChar = open(loadTerm, 'r+')
    global pc
    pc = pickle.load(loadChar)
    return pc
