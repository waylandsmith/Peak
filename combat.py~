#!/usr/bin/env python

# python modules
import os
import pickle
import random

# game modules
import player
from player import PC
import cg2
from cg2 import load_instance
from cg2 import loadThings
import enemies
from enemies import NPC
import w2
from w2 import *
import bfield
from bfield import *

baddie = NPC("Paul Renier",19,14,12,"alive") # loader for enemy.  Long-term, this will be defined by an outside loader function

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
        pct.refresh() # wipe the damage qeues clear
        nct.refresh()
        infoGraphic() # display stats
        checkWin2() # checks to see if fight is over
        fshell = raw_input("Your turn - Fight> ")
        fshell = str(fshell)
# in the end, this will include a loader function for known attacks.  At the moment, it will simply have hardcoded attacks
        if fshell.lower() in ['h','help']:
            print fl1
        elif fshell.lower() in ['l','list']:
            print "you have an axe"
            print "your enemy has a rifle"
            print fl2
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
        hurtBad() # deals damage to the bad guy
        turn += 1
        checkWin2() # checks to see if the fight is over
        flipCoin() # decides which attack enemy will use
        hurtMe() # deals damage to player character


######################################
# FIGHT LOOP END
######################################

def checkWin2(): # checkWin 2
    global fighting
    baddie.checkSelf(baddie.physical,baddie.mental,baddie.spd)
    if baddie.status.lower() in ['dead']:
        fighting = False
        print "you killed the enemy!"
    elif baddie.status.lower() in ['faint']:
        fighting = False
        print "you knocked out your enemy!"
    elif baddie.status.lower() in ['tko']:
        fighting = False
        print "you've incapacitated your enemy."

    pc.chkStatus(pc.physical,pc.mental,pc.spd)
    if pc.status.lower() in ['dead']:
        fighting = False
        print "you died!"
    elif pc.status.lower() in ['faint']:
        fighting = False
        print "you fained!"
    elif pc.status.lower() in ['tko']:
        fighting = False
        print "you're incapacitated and can not defend yourself"
    return fighting

def infoGraphic():
    print "Enemy health: ",baddie.physical
    print "Enemy Mental: ",baddie.mental
    print "Enemy Speed: ",baddie.spd
    print "your health: ",pc.physical
    print "your mental: ",pc.mental
    print "your speed: ",pc.spd

        
def hurtMe(): # this function transfers the damage from 'nct' to you, and invokes the nct.refresh() function
    pc.physical -= nct.phys
    pc.mental -= nct.mental
    pc.spd -= nct.speed

def hurtBad(): # this function transfers the damage from 'pct' to CURRENT_ENEMY
    baddie.physical -= pct.phys
    baddie.mental -= pct.mental
    baddie.spd -= pct.speed

############################################
# IMPORTANT COMBAT FUNCTIONS END
############################################

##############################
# ENEMY ATTACKS
##############################


def darkDmg(p_dmg,m_dmg,s_dmg): # needed until enemies have native attack functions
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

def ebShot(): # modified good guy attack function
    p_dmg = baddie.mental * 0.7 # body shot
    m_dmg = 0
    s_dmg = 0
    missBar = 70 + baddie.mental
    tgt = "you were shot with a rifle!"
    print tgt
    darkDmg(p_dmg,m_dmg,s_dmg)
    
def ehShot():
    p_dmg = baddie.mental * 1.2 
    m_dmg = 0
    s_dmg = 0
    missBar = 60 + baddie.mental
    tgt = "you were sniped with a rifle!"
    print tgt
    darkDmg(p_dmg,m_dmg,s_dmg)

def eclub():
    p_dmg = baddie.physical * 0.4 
    m_dmg = baddie.physical * 0.4
    s_dmg = 0
    missBar = 85 + baddie.physical
    tgt = "you got brained with a club!"
    print tgt
    darkDmg(p_dmg,m_dmg,s_dmg)

