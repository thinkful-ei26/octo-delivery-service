import pygame, random
from settings import *

## ============== NEIGHBOR ==============
class Neighbor(object): 
    _S1 = pygame.image.load('assets/S1.png')
    S1 = pygame.transform.scale(_S1, (40, 50))
    _S2 = pygame.image.load('assets/S2.png')
    S2 = pygame.transform.scale(_S2, (20,40))
    _S3 = pygame.image.load('assets/S3.png')
    S3 = pygame.transform.scale(_S3, (20,40))
    _S4 = pygame.image.load('assets/S4.png')
    S4 = pygame.transform.scale(_S4, (20,40))
    _S5 = pygame.image.load('assets/S5.png')
    S5 = pygame.transform.scale(_S5, (20,40))
    swimUp = [S1, S2, S3, S4]
   
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end] #start and end of neighbor path
        self.vel = 5
        self.swimCount = 0
        self.hitbox = ( self.x, self.y, 40, 40 )
        self.visible = True 
    
    def draw(self, windowSurface):
      self.move() 
      if self.visible:
          if self.vel > 0: 
              windowSurface.blit(self.swimUp[self.swimCount //3], (self.x, self.y))

          ## neighborloop: if neighbor reaches top of screen (y=0) bring them back to screenHeight (y=600) and randomized x position
          if self.y <= 0:
              self.y = screenHeight
              self.x = random.randint(0, screenWidth - 60) 

          ## MOVING HITBOX     
          self.hitbox = (self.x+10, self.y+10, 20, 30 )
          #pygame.draw.rect(windowSurface, red, self.hitbox, 2)

    def move(self):
        self.y -= self.vel # decrementing the count moves obj from bottom to top