#!/usr/bin/env python


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


