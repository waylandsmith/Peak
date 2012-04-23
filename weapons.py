#!/usr/bin/env python

# Combat system version 2:  An attack has both Attack and Damage attributes, where Attack is countered by Defense, a 'counter-attack'.

class Weapon(object):
    def __init__(self,atkStat,dmgStat,target,multiplier):
        self.atkStat = atkStat
        self.dmgStat = dmgStat
        self.target = target
        self.muliplier = multiplier
    

"""
class Axe(object):
    def __init__(self)
# GENERIC ATTRIBUTES
    hitWith = "physical"
	dmgWith = "physical"
	dmg = 2 # damage multiplier
	dtype = "slash"
	spd = 1 # higher values are faster
	acc = 80
	
	def Slash(self):
	def Hammer(self):
"""	

class Splitter(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2
    


example = Splitter("physical","physical","physical",2)
print example.multiplier
