import pygame

blue = (0, 153, 255)
red = (255, 0, 0)
black = (0,0,0)
green = (0, 255, 0)
brown = (222,184,135)
screenWidth = 800
screenHeight = 600

## ============== ENEMY ==============
class enemy(object): 
    _SL1 = pygame.image.load('assets/SL1.png')
    SL1 = pygame.transform.scale(_SL1, (100,40))
    _SL2 = pygame.image.load('assets/SL2.png')
    SL2 = pygame.transform.scale(_SL2, (100,40))
    _SL3 = pygame.image.load('assets/SL3.png')
    SL3 = pygame.transform.scale(_SL3, (100,40))
    _SL4 = pygame.image.load('assets/SL4.png')
    SL4 = pygame.transform.scale(_SL4, (100,40))
    swimLeft = [SL1, SL2, SL3, SL4]
   
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end] #start and end of enemy path
        self.vel = 3
        self.swimCount = 0
        self.hitbox = (self.x, self.y, 100, 40 )
        self.health = 10
        self.visible = True # need this to delete enemy
    
    def draw(self, windowSurface):
      self.move() 
      if self.visible:
          if self.vel > 0: 
              windowSurface.blit(self.swimLeft[self.swimCount //3], (self.x, self.y))

          ## enemy loop: if enemy reaches left side of screen (x=0) bring them back to screenWidth (x=800)
          if self.x <= 0:
              self.health = 10
              self.x = screenWidth 

          ## HEALTBAR
          pygame.draw.rect(windowSurface, red, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
          pygame.draw.rect(windowSurface, green, (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

          ## MOVING HITBOX     
          self.hitbox = (self.x, self.y, 100, 40 )
          #pygame.draw.rect(windowSurface, red, self.hitbox, 2)

    def move(self):
        self.x -= self.vel # decrementing the count moves obj left, increment will move to right
        #print(self.health)
    
    def hit(self): #if enemy is hit, set visible to False
      if self.health > 0: 
          self.health -= 1
      else: 
        self.visible = False
        # print('hit')