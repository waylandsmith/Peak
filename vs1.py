#!/usr/bin/env python

import pygame
import pickle
import os
import random



battle = False
turn = 0
menu = """Options:  fight | inventory | run
"""


#def equipC():

# class Weapon(object):
	#def __init__(self, name, hitWith, dmgWith, dmg, dtype, spd, acc):
	#	self.name = name

	#def attack():
	#	pass

class Axe(object):
	hitWith = "physical"
	dmgWith = "physical"
	dmg = 2 # damage multiplier
	dtype = "slash"
	spd = 1 # higher values are faster
	acc = 80
#	def attack(self):
#		atk = random.randint(0,100)
#		missBar = Axe.acc + PC.physical - Wolf.dodge # an Attack value above this misses.  The higher your missBar, the less likely you miss, because attack values are a random roll	PC.
#		if atk <= missBar:
#			Wolf.beastHP -= Axe.dmg * PC.physical
#			print "you did", Axe.dmg * PC.physical,"damage! \n"
#		else:
#			print "you missed!"	

class Pitchfork(object):
	hitWith = "mental"
	dmgWih = "physical"
	damage = 1
	dtype = "pierce"
	spd = 2
	acc = 100

class Wolf(object):
	beastHP = 50
	alive = True
	physical = 8
	mental = 1
	dmg = 5
	acc = 95
	dodge = 10
	armor = 1
	def death():
		if beastHP < 1:
			alive = False
class PC(object):
	hp = 50
	physical = 5
	mental = 2
#	dmg = strength + axeDamage
#	acc = 80 # deprecated
	dodge = 5
	armor = 2
	equip = "Axe"

def attack(): # the template function for all attack methods
	atk = random.randint(0,100)
	missBar = Axe.acc + PC.physical - Wolf.dodge # an Attack value above this misses.  The higher your missBar, the less likely you miss, because attack values are a random roll	PC.
	if atk <= missBar:
		Wolf.beastHP -= Axe.dmg * PC.physical
		print "you did", Axe.dmg * PC.physical,"damage! \n"
	else:
		print "you missed!"	

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
			attack()
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
