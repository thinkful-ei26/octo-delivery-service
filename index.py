import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Octo Demo')

# load assets
# octoImg = pygame.image.load('assets/octopic.png')
squidImg = pygame.image.load('assets/squid.png')
shellImg = pygame.image.load('assets/shell.png')

# transform assets
# octo = pygame.transform.scale(octoImg, (60, 60))
squid = pygame.transform.scale(squidImg, (40, 60) )
shell = pygame.transform.scale(shellImg, (30, 30))

blue = (0, 153, 255)
red = (255, 0, 0)
clock = pygame.time.Clock()

## ============== PLAYER ==============
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.hitbox = (self.x + 40, self.y, 40, 40) # square tuple
        
    
    def draw (self, win):
        octoImg = pygame.image.load('assets/octopic.png')
        octo = pygame.transform.scale(octoImg, (60, 60))
        win.blit(octo, (self.x, self.y)) #load octo img
        ## MOVING HITBOX  
        self.hitbox = (self.x, self.y, 60, 60)
        pygame.draw.rect(win, red, self.hitbox, 2)


## ============== PROJECTILE ==============
class projectile(object):
  def __init__(self, x, y, radius, color):
      self.x = x
      self.y = y
      self.radius = radius
      self.color = color
      self.vel = 8
      self.hitbox = (self.x-8, self.y-5, 15, 15)

  def draw(self, win):
      pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
      ## MOVING HITBOX   
      self.hitbox = (self.x-8, self.y-5, 15, 15)
      pygame.draw.rect(win, red, self.hitbox, 2)

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
    
    def draw(self, win):
      self.move() 
      if self.vel > 0: 
          win.blit(self.swimLeft[self.swimCount //3], (self.x, self.y))
       
      ## MOVING HITBOX     
      self.hitbox = (self.x, self.y, 100, 40 )
      pygame.draw.rect(win, red, self.hitbox, 2)

    def move(self):
        self.x -= self.vel # decrementing the count moves obj left, increment will move to right
    
    def hit(self):
        print('hit')
        pass


## ============== REDRAW GAME WINDOW ============== 
def redrawGameWindow(x, y, width, height):
    win.fill((blue))
    octopus.draw(win)
    shark.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    #win.blit(squid, (screenWidth-40, (screenHeight/2 -60), width, height))
    # win.blit(octo, (x, y, width, height))
    # win.blit(shell, ((screenWidth/2), (screenHeight/2 -60), width, height))
    # win.blit(shark, ((screenWidth/2 - 40), (screenHeight/2 -60 - 40), width, height))
    pygame.display.update() 

## ============== DEFINE GAME OBJECTS ==============
octopus = player(0, (screenHeight/2 - 60), 60, 60)
bullets = []  # container for our bullet
shark = enemy(screenWidth-100, (screenHeight/2 - 60), 60, 40, 800)
run = True

## ============== MAIN LOOP ==============
while run:
    clock.tick(27)
    # pygame.time.delay(100) # game clock

    for event in pygame.event.get(): # event handling game
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets: 
        if bullet.y - bullet.radius < shark.hitbox[1] + shark.hitbox[3] and bullet.y + bullet.radius > shark.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, y coord
            if bullet.x + bullet.radius > shark.hitbox[0] and bullet.x - bullet.radius < shark.hitbox[0] + shark.hitbox[2]: # left & right x coord of shark box
                shark.hit()
                bullet.pop(bullets.index(bullet))

        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel # bullet is going to move vel direction
        else: 
            bullets.pop(bullets.index(bullet)) # pop off the bullet or delete them 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 20:
            bullets.append(projectile(round(octopus.x + octopus.width //2), round(octopus.y + octopus.height//2), 6, (0,0,0)))

    if keys[pygame.K_LEFT] and octopus.x > octopus.vel:
        octopus.x -= octopus.vel
    if keys[pygame.K_RIGHT] and octopus.x < screenWidth - octopus.width:
        octopus.x += octopus.vel
    if keys[pygame.K_UP] and octopus.y > octopus.vel:
        octopus.y -= octopus.vel
    if keys[pygame.K_DOWN] and octopus.y < screenWidth - octopus.width:
        octopus.y += octopus.vel

    redrawGameWindow(octopus.x, octopus.y, octopus.width, octopus.height)

pygame.quit()

# detect collision:
'''
1. octo & squid => end game 
2. octo & shell => change octo sprite & delete shell
3. octo have projectile
4. add enemy shark
'''