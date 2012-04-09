#!/usr/bin/env python

import pygame
import pickle
import os
import random



battle = False
turn = 0
menu = """Options:  fight | inventory | run
"""


class Wolf(object):
	beastHP = 50
	alive = True
	dmg = 5
	acc = 95
	dodge = 10
	armor = 1
	def death():
		if beastHP < 1:
			alive = False


class PC(object):
	hp = 50
	strength = 5
	axeDamage = 2
	dmg = strength + axeDamage
	acc = 80
	dodge = 5
	armor = 2


initiative = raw_input("an injured wolf appeared!  what do you do? ")

# options:  attack, run
if initiative.lower() in ['attack','fight']:
	battle = True
else:
	print "you got away!"

while battle == True:
	print "HP = ",PC.hp
	print "Wolf HP = ",Wolf.beastHP
	if turn/2 == turn / 2.0:
		print menu
		act = raw_input("what do you do? ")
	        if act.lower() in ['inventory']:
		    	print "you have an axe equipped and no other items \n"
	    		turn += 1
		elif act.lower() in ['axe','attack','hit','fight']:
			atk = random.randint(0,100)
			missBar = PC.acc - Wolf.dodge # an Attack value above this misses.  The higher your missBar, the less likely you miss, because attack values are a random roll
			if atk <= missBar:
				Wolf.beastHP -= PC.dmg
				print "you did", PC.dmg,"damage! \n"
			else:
				print "you missed!"
		    	turn += 1
	    	else:
			print "invalid"
	else:
        	wAtk = random.randint(0,100)
		missB2 = Wolf.acc - PC.dodge
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

## PC class
#class PC(object):





pseudocode = """
Classes that the game should load:  PC, Enemy, Background, GUI

Weapons:  axe, r
	face = 
------------------------------
------------------------------
------- ------------ ---------
------   ----------   --------
-----     --------     -------
-----      ------       ------
-----      ------       ------
-----


"""
