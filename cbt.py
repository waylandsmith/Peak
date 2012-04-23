#!/usr/bin/env python

import random
import pickle
# import player

item = 1 # if odd, Splitter; if even, Rifle
itemOut = "Splitter Axe"
weaponID = "axe"
turn = 0
menu = """Options:  fight | inventory | run
"""

class PC(object):
    def __init__(self, name, hp, physical, mental, status):
        self.name = name
        self.hp = hp
        self.physical = physical
        self.mental = mental
        self.status = status

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

def statDump():
    print PC.name
    print "Physical: ",PC.physical
    print "Mental: ",PC.mental

def switch():
    global item
    item += 1

def iTell():
    global itemOut
    global weaponID
    if item / 2 == item / 2.0:
        itemOut = "Hunting Rifle"
        weaponID = "rifle"
    else:
        itemOut = "Splitter Axe"
        weaponID = "axe"


def attack(): # the template function for all attack methods
	atk = random.randint(0,100)
	missBar = 80 + PC.physical # an Attack value above this misses.  The higher your missBar, the less likely you miss, because attack values are a random roll	PC.
	if atk <= missBar:
		Wolf.physical -= 2 * PC.physical
		print "you did", 2 * PC.physical,"damage! \n"
	else:
		print "you missed!"	

def rifle():
    atk = random.randint(0,100)
    missBar = 65 + PC.mental # attack values above this miss
    if atk <= missBar:
        Wolf.physical -= 5 * PC.mental
        print "you did", 5 * PC.mental,"damage! \n"
    else:
        print "you missed!"

def checkWin():
    global battle
    if Wolf.physical < 1:
        battle = False
        print "you killed the wolf!"
    if PC.physical < 1:
        battle = False
        print "you died!"


loadChar = open('save/pc/matt.creature', 'r+')

PC = pickle.load(loadChar)


battle = True

while battle == True:
    iTell()
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

