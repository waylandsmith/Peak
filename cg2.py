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


