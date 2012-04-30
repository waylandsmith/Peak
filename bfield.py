#!/usr/bin/env python

### LEVEL
### SIMILAR TO level.py in a finished game, but for the combat minigame

import os
#import combat
# import w2

# THE PURPOSE OF THE BATTLEFIELD IS TO ROUTE ALL ATTACKS TO THEIR TARGETS
# THIS IS A KEY PROGRAM FILE

CURRENT_ENEMY = "Paul Renier" # reimplement the selector here
CURRENT_CHAR = "Default"

class Field(object):
    def __init__(self,phys,mental,speed):
        self.phys = phys
        self.mental = mental
        self.speed = speed
    def refresh(self): # resets target attribute values to zero
        self.phys *= 0
        self.mental *= 0
        self.speed *= 0
        return
        
pct = Field(0,0,0) # player target
nct = Field(0,0,0) # NPC target


class Level(object):
# stuff
    def __init__(self):
        pass
        
    def restart(self):
        pass
    


#######################################################
#          Copyright Matthew Meneghini 2012           #
#######################################################
