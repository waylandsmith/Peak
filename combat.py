#!/usr/bin/env python

import os
import pickle
import random

import player
from player import *
import cg2
from cg2 import load_instance
from cg2 import loadThings
import enemies
from enemies import NPC
import w2
from w2 import *
import bfield
from bfield import *
# axe = Splitter("physical","physical","physical",2)

# loadChar = open(load_instance.name, 'r+')

# PC = pickle.load(loadChar)

global xp

baddie = NPC("Paul Renier",19,14,12,"alive")

loadThings() # opens and loads relevant save file

#####################################
# FIGHTING SHELL
#####################################

fl1 = """
this is the fighting shell
h   | help
l   | list weapons
a   | attack
q   | quit
"""

fl2 = """
Available Attacks:
-------------------
1   | Hack  | basic attack
2   | Sweep | lowers speed
3   | Slash | moderate attack
4   | Stun  | lowers mental
"""

def fight():    # this is the fight menu
    global fighting
    fighting = True
    turn = 1
    while fighting:
        pct.refresh()
        nct.refresh()
        fshell = raw_input("Your turn - Fight> ")
        fshell = str(fshell)
# in the end, this will include a loader function for known attacks.  At the moment, it will simply have hardcoded attacks
        if fshell.lower() in ['h','help']:
            print fl1
        elif fshell.lower() in ['l','list']:
            print "you have an axe"
            print baddie.physical
        elif fshell.lower() in ['q', 'quit','b','back']:
            fighting = False
        elif fshell.lower() in ['a']:
            atk_cmd = raw_input("Your turn - Fight - Attack> ")
            atk_cmd = int(atk_cmd)
            if atk_cmd == 1:
                hack()
            elif atk_cmd == 2:
                sweep()
            elif atk_cmd == 3:
                slash()
            elif atk_cmd == 4:
                stun()
            else:
                print fl2
        else:
             print fl1
        hurtBad()
        turn += 1
#        flipCoin()
#        hurtMe()
#            turn += 1
        checkWin() # checks to see if you've won

######################################
# END
######################################


def checkWin(): # checks to see if you've won
    baddie.checkSelf(baddie.physical,baddie.mental,baddie.spd)
    if baddie.status.lower() in ['alive']:
        print "Enemy health: ",baddie.physical
    else:
        print "you win!"
        global fighting
        fighting = False
        return fighting
        
def hurtMe(): # this function transfers the damage from 'nct' to you, and invokes the nct.refresh() function
    pc.physical -= nct.phys
    pc.mental -= nct.mental
    pc.spd -= nct.speed

def hurtBad(): # this function transfers the damage from 'pct' to CURRENT_ENEMY
    baddie.physical -= pct.phys
    baddie.mental -= pct.mental
    baddie.spd -= pct.speed

##############################
# ENEMY ATTACKS

def darkDmg(p_dmg,m_dmg,s_dmg):
    nct.phys += p_dmg
    nct.mental += m_dmg
    nct.speed += s_dmg

def flipCoin():
    choice = random.randint(1,3)
    if choice == 1:
        ebShot()
    elif choice == 2:
        ehShot()
    else:
        eclub()

def ebShot():
    p_dmg = baddie.mental * 0.7 # body shot
    m_dmg = 0
    s_dmg = 0
    missBar = 70 + baddie.mental
    tgt = "shot!"
    darkDmg(p_dmg,m_dmg,s_dmg)
    
def ehShot():
    p_dmg = baddie.mental * 1.2 # Dad, would you put Mum on the phone...
    m_dmg = 0
    s_dmg = 0
    missBar = 60 + baddie.mental
    tgt = "sniped"
    darkDmg(p_dmg,m_dmg,s_dmg)

def eclub():
    p_dmg = baddie.physical * 0.4 # no dancing here, but it is skeevy.
    m_dmg = baddie.physical * 0.4
    s_dmg = 0
    missBar = 85 + baddie.physical
    tgt = "brained"
    darkDmg(p_dmg,m_dmg,s_dmg)

