#!/usr/bin/env python

import random

# Combat system version 2:  An attack has both Attack and Damage attributes, where Attack is countered by Defense, a 'counter-attack'.

class Weapon(object):
    def __init__(self,atkStat,dmgStat,target,multiplier):
        self.atkStat = atkStat
        self.dmgStat = dmgStat
        self.target = target
        self.muliplier = multiplier
    damage = 0

class Splitter(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2
    def hack():
        global damage
        tgt = "physical"
        damage = PC.physical * 1.5
        atk = random.randint(0,100)
        missBar = 85 + PC.mental
    def swipe():
        pass
    def sweep():
        pass
    def crush():
        pass
    def cSlash():
        pass # this is a more advanced technique.  Advanced slash and withdrawal.
    
class Hatchet(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2

class Rifle(Weapon):
    atkStat = "mental"
    dmgStat = "mental"
    target = "physical"
    multiplier = 2
    def bodyShot():
        pass
    def headShot():
        pass
    def bayonet():
        pass
    def club():
        pass


class Shotgun(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2

class Mace(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2

class Pitchfork(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2

class Dagger(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2
    
class Fists(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2

class Bow(Weapon):
    atkStat = "physical"
    dmgStat = "physical"
    target = "physical"
    multiplier = 2


example = Splitter("physical","physical","physical",2)
print example.multiplier
