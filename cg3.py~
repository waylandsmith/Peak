#!/usr/bin/env python

import pickle
import player
from player import PC

# THIS IS THE FINAL CHARACTER GENERATOR
def charGen():
    nom = raw_input("what is your name? ")
    con = 20
    wis = 20
    age = raw_input("how old are you? ")
    if age.lower() in ['old']:
        age = "OLD"
        con -= 3
        wis += 2
    elif age.lower() in ['30s']:
        age = "PRIME"
        wis += 1
    elif age.lower() in ['20s']:
        age = "YOUNG"
        con += 1
    elif age.lower() in ['teen']:
        age = "TEEN"
        con += 2
        wis -= 2
    
    unemployed = True
    while unemployed:
        job = raw_input("what is your profession? ")
        if job.lower() in ['farmer']:
            unemployed = False
            con += 3
        elif job.lower() in ['hunter']:
            unemployed = False
            wis += 2
            con += 1
        elif job.lower() in ['scholar']:
            unemployed = False
        elif job.lower() in ['hunter']:
            unemployed = False
        else:
            print "not a real job!"
   
    
    
    
charGen()

def charGenOld():
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


# AGE CATEGORIES
# OLD:  +2 to Mental, -3 to Physical
# PRIME:  +1 to Mental, +0 to Physical
# 20Something: +0 to Mental, +1 to Physical
# Teen: -1 to Mental, +2 to Physical
