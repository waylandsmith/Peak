#!/usr/bin/env python

import pygame
import pickle
import os
import random

#	path.os.join("

battle = False
turn = 0
menu = """Options:  fight | inventory | run
"""

class Wolf(object):
	beastHP = 50
	alive = True
	dmg = 5
	def death():
		if beastHP < 1:
			alive = False

class PC(object):
	hp = 50
	strength = 5
	axeDamage = 2
	dmg = strength + axeDamage

class Weapon(object):
	
	
#class PC(object):
#	def abilities():
#		atk = 10;

		

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
			Wolf.beastHP -= PC.dmg
		    	print "you did", PC.dmg,"damage! \n"
		    	turn += 1
	    	else:
			print "invalid"
	else:
        	PC.hp -= Wolf.dmg
		turn += 1
        	print "the wolf strikes!"
		print "the wolf did",Wolf.dmg,"damage"
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

Weapons:  axe, rope

"""
