import pygame

blue = (0, 153, 255)
red = (255, 0, 0)
black = (0,0,0)
green = (0, 255, 0)
brown = (222,184,135)

## ============== PLAYER ==============
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.hitbox = (self.x + 40, self.y, 40, 40) # square tuple
        
    def draw (self, windowSurface):
        octoImg = pygame.image.load('assets/octopic.png')
        octo = pygame.transform.scale(octoImg, (60, 60))
        windowSurface.blit(octo, (self.x, self.y)) #load octo img
        ## MOVING HITBOX  
        self.hitbox = (self.x, self.y, 60, 60)
        pygame.draw.rect(windowSurface, red, self.hitbox, 2)