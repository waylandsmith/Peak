#!/usr/bin/env python

class Load_Enemy(object):
    def __init__(self,name):
        self.name = name
        
    def loadBitches(self, belli):
        pass
    
def enemyLoad(enemy): # now you need to provide an enemy.  Preferably a non-hardcoded one.
    if enemy == neighbor1:
        print "enemy is PAUL!"
    
    print "loading"


class NPC(object):
    def __init__(self,name,physical,mental,spd,status):
        self.name = name
        self.physical = physical
        self.mental = mental
        self.spd = spd
        self.status = status

    def checkSelf(self,physical,mental,spd):
        if self.physical < 0:
            self.status = "dead"
        elif self.mental < 0:
            self.status = "faint"
        elif self.spd < 0:
            self.status = "tko"
        return self.status
                        
    def statusUpdate(self):
        print self.name,":"
        print "Physical: ",self.physical
        print "Mental: ",self.mental
        print "Speed: ",self.spd

class Dog(object):
    def __init__(self,physical,mental,dmg,acc,spd,status):
        self.physical = physical
        self.mental = mental
        self.dmg = dmg
        self.acc = acc
        self.spd = spd
        self.status = status
    def statusUpdate():
        print "Dreadwolf"
        print "Physical: ",self.physical
        print "Mental: ",self.mental
    def atked():
        pass
    def death():
        if self.physical < 0:
            self.status = "dead"



"""     
    def die(self,status):
        self.status = 0
        self.status = str(self.status)
        return self.status
        
    def faint(self,status):
        self.status = 1
        self.status = str(self.status)
        return self.status
        
    def tko(self,status):
        self.status = 2
        self.status = str(self.status)
        return self.status
"""

neighbor1 = NPC("Paul Renier",15,17,11,"alive")
neighbor2 = NPC("Robert Renier",15,17,11,"alive")
neighbor3 = NPC("Marianne Renier",15,17,11,"alive")
neighbor4 = NPC("Desiree Renier",15,17,11,"alive")
neighbor5 = NPC("Mirabelle Renier",15,17,11,"alive")
