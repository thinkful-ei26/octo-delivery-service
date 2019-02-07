import pygame

red = (255, 0, 0)
brown = (222,184,135)

## ============== PACKAGE ==============
class Package(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 1
        self.hitbox = (self.x, self.y, 40, 40)
        self.visiblem = True

    def draw(self, windowSurface):
    #   pygame.draw.rect(windowSurface, self.color, (self.x, self.y), 2)
      pygame.draw.rect(windowSurface, brown, (self.x+5, self.y+5, 20, 20), 2)
      ## MOVING HITBOX   
      self.hitbox = (self.x, self.y, 30, 30)
      pygame.draw.rect(windowSurface, red, self.hitbox, 2)