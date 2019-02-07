import pygame
from settings import *

## ============== PACKAGE ==============
class Package(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 2
        self.hitbox = (self.x, self.y, 40, 40)
        self.visiblem = True

    def draw(self, windowSurface):
      pygame.draw.rect(windowSurface, brown, (self.x+5, self.y+5, 20, 20), 0)
      ## MOVING HITBOX   
      self.hitbox = (self.x, self.y, 30, 30)
      #pygame.draw.rect(windowSurface, red, self.hitbox, 2)