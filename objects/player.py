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
        self.vel = 10
        self.hitbox = (self.x + 40, self.y, 40, 40) # square tuple
        self.health = 10
        self.visible = True # if false, then game over feedback
        
    def draw (self, windowSurface):
        octoImg = pygame.image.load('assets/octopic.png')
        octo = pygame.transform.scale(octoImg, (60, 60))

        if self.visible:
            windowSurface.blit(octo, (self.x, self.y)) 

            ## OCTO HEALTBAR
            pygame.draw.rect(windowSurface, red, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(windowSurface, green, (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            
            ## MOVING HITBOX  
            self.hitbox = (self.x, self.y, 60, 60)
            #pygame.draw.rect(windowSurface, red, self.hitbox, 2)
    
    def hit(self, windowSurface): 
        if self.health > 0: 
            self.health -= 1
        else: #if octo's hp 0, disappears
            self.visible = False
            font1 = pygame.font.SysFont('helvetica', 100)
            text = font1.render('GAME OVER', 1, (255,0,0))
            windowSurface.blit(text, (250 - (text.get_width()/2),200))
            pygame.display.update()
            