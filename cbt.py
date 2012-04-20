#!/usr/bin/env python

import random
import pickle
# import player

item = 1 # if odd, Splitter; if even, Rifle
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

class Wolf(object):
	beastHP = 50
	alive = True
	physical = 8
	mental = 1
	dmg = 5
	acc = 95
	armor = 1
	def death():
		if beastHP < 1:
			alive = False


def switch():
    item += 1

def attack(): # the template function for all attack methods
	atk = random.randint(0,100)
	missBar = 80 + PC.physical # an Attack value above this misses.  The higher your missBar, the less likely you miss, because attack values are a random roll	PC.
	if atk <= missBar:
		Wolf.beastHP -= 2 * PC.physical
		print "you did", 2 * PC.physical,"damage! \n"
	else:
		print "you missed!"	

def rifle():
    atk = random.randint(0,100)
    missBar = 65 + PC.mental # attack values above this miss
    if atk <= missBar:
        Wolf.beastHP -= 5 * PC.mental
        print "you did", 5 * PC.mental,"damage! \n"
    else:
        print "you missed!"

loadChar = open('save/pc/matt.creature', 'r+')

PC = pickle.load(loadChar)

print PC.name
print PC.hp

battle = True

while battle == True:
	print "HP = ",PC.hp
	print "Wolf HP = ",Wolf.beastHP
	if turn/2 == turn / 2.0:
		print menu
		act = raw_input("what do you do? ")
	        if act.lower() in ['inventory']:
		    	print "You have a splitter and an axe,"
                        print "And you currently have","equipped."
                        iact = raw_input("Would you like to switch(Y/n) ")
                        if iact.lower() in ['y']:
                            switch()
                        else:
                            print "ok, but you still lost a turn"
	    		turn += 1
		elif act.lower() in ['axe','attack','hit','fight']:
                    if item/2 == item/2.0
			attack()
		    	turn += 1
	    	else:
			print "invalid"
	else:
        	wAtk = random.randint(0,100)
		missB2 = Wolf.acc
		if wAtk <= missB2:
			PC.hp -= Wolf.dmg
			print "the wolf strikes!"
			print "the wolf did",Wolf.dmg,"damage"
		else:
			print "the wolf missed!"
		turn += 1

	if Wolf.beastHP < 1:
#	if Wolf.alive == False:
		battle = False
		print "you killed the wolf!"
	if PC.hp < 1:
		battle = False
		print "you died!"
