#!/usr/bin/env python

import pickle
import player
from player import *
import weapons
from weapons import *
import combat
from combat import *
import enemies
from enemies import *

class Post(object):
    def __init__(self,name,physical,mental):
        self.name = name
        self.physical = physical
        self.mental = mental

te = Post("Pole", 33, 1)

"""
class Dog(object):
    def __init__(self,physical,mental,dmg,acc):
        self.physical = physical
        self.mental = mental
        self.dmg = dmg
        self.acc = acc
    def statusUpdate():
        print "Wolf Status:"
        print "Physical: ",self.physical
        print "Mental: ",self.mental
    def death():
        if beastHP < 1:
            alive = False

Wolf = Dog(8,1,3,95)
"""

def statDump():
    print PC.name
    print "Physical: ",PC.physical
    print "Mental: ",PC.mental
"""
def checkWin():
    global battle
    if Wolf.physical < 1:
        battle = False
        print "you killed the wolf!"
    if PC.physical < 1:
        battle = False
        print "you died!"
"""

# loadChar = open('save/pc/matt.creature', 'r+')

# PC = pickle.load(loadChar)

menu = """
+--------------+
|$  | COMMANDS |
+--------------+
|e  | LOAD ENEMY
|f  | FIGHT
|q  | QUIT
"""

battle = True
bcount = 0

while battle == True:
    act = raw_input("Your turn> ")
    if act.lower() in ['f']:
        fight()
#        hack()
#        print te.tgt
    elif act.lower() in ['q']:
        battle = False
#        print bcount
    elif act.lower() in ['e']:
        enemyLoad(neighbor1)
    else:
        print menu
#    bcount +=1

"""
while battle == True:
#    iTell()
    statDump()
    if turn/2 == turn / 2.0:
        print menu
        act = raw_input("what do you do? ")
        if act.lower() in ['inventory']:
            print "You have a splitter and an axe,"
            print "And you currently have",itemOut,"equipped."
            iact = raw_input("Would you like to switch(Y/n) ")
            if iact.lower() in ['y']:
                switch()
            else:
                print "ok, but you still lost a turn"
            turn += 1
        elif act.lower() in ['axe','attack','hit','fight']:
            if weaponID.lower in ['axe']:
                attack()
            else:
                rifle()
            checkWin()
            turn += 1
        else:
            print "invalid"
    else:
        wAtk = random.randint(0,100)
        missB2 = Wolf.acc
        if wAtk <= missB2:
            PC.physical -= Wolf.dmg
            print "the wolf strikes!"
            print "the wolf did",Wolf.dmg,"damage"
        else:
            print "the wolf missed!"
        checkWin()
        turn += 1

"""
