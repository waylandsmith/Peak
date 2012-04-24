#!/usr/bin/env python

#####################
"""
THIS IS AN EARLY SAVEGAME AND LOADER
"""
#####################
import pickle
import player # player class definitions
import cg2 # character generator script v2

from cg2 import *
from player import PC
#####################

############## CREDITS

title_msg = """
From the Hampshire College Press
a survival roleplaying game called

PEAK

Copyright Matthew Meneghini and Matthew Pink 2012
"""
print title_msg
######################

# THIS IS THE BACKGROUND STORY
msg ="""
It is January 13, 2014.  
You are out of oil.  It is cold....very cold.
You wake up and see a face in the mirror.
Your face.
""" 

##
# LOADER
h_msg ="""
Letter  | Command
l       | Load Game
n       | New Game
q       | Quit
h       | Help
"""
print h_msg

done = False
while not done:
    tprompt = raw_input("input a command: ")
    if tprompt.lower() in ['l','load','save']:
        pass
    elif tprompt.lower() in ['n','new','new game']:
        print msg
        charGen() # CHARACTER CREATION
        done = True
    elif tprompt.lower() in ['q','quit']:
        print "goodbye!"
        done = True
    else:
        print h_msg

######################

"""
Loader script must do the following:  set the game to run 

"""
# IN-GAME MOVEMENT
# FROM NEW GAME
print "you are attacked by a wolf!  Time for battle!"

# FROM SAVED GAME

# COMBAT ENCOUNTER


#### AMBUSH!!!!
