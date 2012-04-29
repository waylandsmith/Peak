#!/usr/bin/env python

import os
import pickle

import player
from player import *

import cg2
from cg2 import load_instance
from cg2 import loadThings

import enemies
from enemies import NPC

import weapons
from weapons import Weapon
from weapons import Splitter

# axe = Splitter("physical","physical","physical",2)

# loadChar = open(load_instance.name, 'r+')

# PC = pickle.load(loadChar)

baddie = NPC("test",9,8,2,"alive")

loadThings() # opens and loads relevant save file

#####################################
# FIGHTING SHELL
#####################################

fl1 = """
this is the fighting shell
h   | help
q   | quit
"""

def fight():    # this is the fight menu
    global fighting
    fighting = True
    while fighting:
        fshell = raw_input("Your turn - Fight> ")
        fshell = str(fshell)
# in the end, this will include a loader function for known attacks.  At the moment, it will simply have hardcoded attacks
        if fshell.lower() in ['h','help']:
            print fl1
        elif fshell.lower() in ['l','list','a','attack']:
            baddie.physical -= 5
#            print baddie.physical
        elif fshell.lower() in ['q', 'quit','b','back']:
            fighting = False
        else:
            print "invalid!"
        checkWin() # checks to see if you've won

######################################
# END
######################################


def checkWin(): # checks to see if you've won
    baddie.checkSelf(baddie.physical,baddie.mental,baddie.spd)
    if baddie.status.lower() in ['alive']:
        print "baddie health: ",baddie.physical
    else:
        print "you win!"
        global fighting
        fighting = False
        return fighting

def hack():
    damage = PC.physical * 1.5
#    atk = random.randint(0,100)
    missBar = 85 + PC.physical
    tgt = "physical"

    
def sweep():
    pass
    
def stab():
    pass

def swipe():
    pass
    
def stun():
    pass
        
def spray():
    pass
    
def jet():
    pass
    
def explode():
    pass
    
def whack():
    pass
    
def roundhouse():
    pass
    
def bShot():
    pass
    
def hShot():
    pass
    
def club():
    pass
    
def slash():
    pass
    
def pin():
    pass
    
def dismember():
    pass
    
def hammer():
    pass
    
