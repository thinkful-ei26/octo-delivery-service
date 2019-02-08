import pygame as pg
from settings import *

## ============== PLAYER ==============
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 25
        self.hitbox = (self.x + 40, self.y, 40, 40) # square tuple
        self.health = 10
        self.visible = True # if false, then game over feedback
        self.collecting = False #octo won't have a package on load
        self.collectCount = 0
        self.delivered = False # switch True if all 8 packages collected
        self.deliveryCount = 0
        
    def draw (self, windowSurface):
        octoImg = pg.image.load('assets/octopic.png')
        octo = pg.transform.scale(octoImg, (60, 60))

        if self.visible:
            windowSurface.blit(octo, (self.x, self.y)) 

            ## OCTO HEALTBAR
            pg.draw.rect(windowSurface, red, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pg.draw.rect(windowSurface, green, (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            
            ## MOVING HITBOX  
            self.hitbox = (self.x, self.y, 60, 60)
            # pygame.draw.rect(windowSurface, red, self.hitbox, 2)
    
    def hit(self, windowSurface): 
        if self.health > 0: 
            self.health -= 1
        else: #if octo's hp 0, disappears
            self.visible = False
            font1 = pg.font.SysFont('helvetica', 100)
            text = font1.render('GAME OVER', 1, (255,0,0))
            windowSurface.blit(text, (250 - (text.get_width()/2),200))
            pg.display.update()

    # def victory(self, windowSurface):
    #     font2 = pg.font.SysFont('helvetica', 50)
    #     text = font2.render('You did it!', 1, (0,0,0))
    #     windowSurface.blit(text, (250 - (text.get_width()/2),200))
    #     pg.display.update()
            