#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

import dumbmenu as dm

PC_HP = 50
PC_STR = 5
AXE_STR = 2

WOLF_HP = 50
WOLF_STR = 5

def battle(font, text, pHP, wHP, pSTR, aSTR, wSTR):
    pc_alive = True
    wolf_alive = True
    pc_dmg = pSTR + aSTR
    wolf_dmg = wSTR
    wHP -= pc_dmg
    text = font.render("You did " + str(pc_dmg) + "damage!", True, (0,0,0))
    pygame.display.update()
    if wolf_alive:
        pHP -= wolf_dmg
        text = font.render("The Wolf did " + str(wolf_dmg) + "damage!", True, (0,0,0))
        pygame.display.update()
    elif pHP < 1:
        pc_alive = False
        pHP = 0
        text = font.render("You died!", True, (0,0,0))
        pygame.display.update()
        return pc_alive
    elif wHP < 1:
        wolf_alive = False
        wHP = 0
        text = font.render("You killed the Wolf!", True, (0,0,0))
        pygame.display.update()
        return wolf_alive

class Game(object):
    def __init__(self):
        self.screen_size = 800, 600
        self.screen = pygame.display.set_mode(self.screen_size)
        self.background = pygame.image.load("shed.png").convert()
        self.player = pygame.image.load("player.png").convert()
        self.enemy = pygame.image.load("wolf2.png").convert()
        self.menu = pygame.Rect((450, 375), (350, 325))
        self.textbox = pygame.Rect((0, 375), (450, 325))
        self.font = pygame.font.Font(None, 32)
        self.fps = 30

    def run(self):
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
            pygame.draw.rect(self.screen, (255,255,255),   self.textbox)
            pygame.draw.rect(self.screen, (0,0,0), self.textbox, 5)
            pcHealth = self.font.render("HP: " + str(PC_HP), True, (0,0,0))
            wolfHealth = self.font.render("Wolf: " + str(WOLF_HP), True, (0,0,0))
            text = self.font.render("What do you do?", True, (0,0,0))
            self.screen.blit(pcHealth, (25, 400))
            self.screen.blit(wolfHealth, (350, 400))
            self.screen.blit(text, (25, 500))

# Menu - Very buggy. Need to find a new one, but didn't realize it was a fatal flaw until very late. It doesn't return the values it's supposed to, so weird stuff happens when you select an option. Will get a working menu up ASAP.
            choose = dm.dumbmenu(self.screen, [
                                    "Fight",
                                    "Inventory",
                                    "Run"], 500, 400, None, 48, 1.4, (0,0,0), (0,0,0), False)
            pygame.display.flip()

            if choose == 1:
                battle(self.font, text, PC_HP, WOLF_HP, PC_STR, AXE_STR, WOLF_STR)
                if battle(self.font, text, PC_HP, WOLF_HP, PC_STR, AXE_STR, WOLF_STR) == False:
                    done = True
            elif choose == 2:
                text = self.font.render("You have an axe equipped  and no other items.", True, (0,0,0))
                pygame.display.update()
            elif choose == 3:
                text = self.font.render("You got away!", True, (0,0,0))
                pygame.display.update()
                done = True

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
