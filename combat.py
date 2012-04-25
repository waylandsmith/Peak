#!/usr/bin/env python

import os
import pickle

import player
from player import *

import weapons
from weapons import Weapon
from weapons import Splitter

# axe = Splitter("physical","physical","physical",2)

loadChar = open('save/pc/matthew.creature', 'r+')

PC = pickle.load(loadChar)

def fight():    # this is the fight menu
    fighting = True
    while fighting:
        fshell = raw_input("Fight> ")
        if fshell.lower() in ['h','help']:
            pass
        elif fshell.lower() in ['q', 'quit']:
            fighting = False

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
    
