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
        ## could have velocity to make it interesting
        self.hitbox = (self.x, self.y, 40, 40)
    
    def draw(self, windowSurface):
      pygame.draw.rect(windowSurface, self.color, (self.x, self.y))
      ## MOVING HITBOX   
      self.hitbox = (self.x, self.y, 40, 40)
      pygame.draw.rect(windowSurface, red, self.hitbox, 2)