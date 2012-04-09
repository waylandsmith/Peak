#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from vs1 import Wolf,PC

import dumbmenu as dm

class Game(object):
    def __init__(self):
        self.screen_size = 800, 600
        self.screen = pygame.display.set_mode(self.screen_size)
        self.background = pygame.image.load("shed.png").convert()
        self.player = pygame.image.load("player.png").convert()
        self.enemy = pygame.image.load("wolf2.png").convert()
        self.menu = pygame.Rect((450, 375), (350, 325))
        self.textbox = pygame.Rect((0, 375), (450, 325))
        self.fps = 30

        clock = pygame.time.Clock()
        done = False
        while not done:
            clock.tick(self.fps)

            for evt in pygame.event.get():
                if evt.type == QUIT:
                    done = True
                elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                    done = True

            #Draw
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.player, (0,0))
            self.screen.blit(self.enemy, (500, 125))
            pygame.draw.rect(self.screen, (255,255,255), self.menu)
            pygame.draw.rect(self.screen, (0,0,0), self.menu, 5)
            pygame.draw.rect(self.screen, (255,255,255), self.textbox)
            pygame.draw.rect(self.screen, (0,0,0), self.textbox, 5)

# Menu - Kind of buggy. ESC has to be pressed to make the other images display, and won't quit without ctrl+c in terminal. Needs fixing.
            choose = dm.dumbmenu(self.screen, [
                                "Fight",
                                "Inventory",
                                "Run"], 500, 400, None, 48, 1.4, (0,0,0), (0,0,0), False)

            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.__init__()