import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Octo Demo')

# load assets
octoImg = pygame.image.load('assets/octopic.png')
squidImg = pygame.image.load('assets/squid.png')
shellImg = pygame.image.load('assets/shell.png')
sharkImg = pygame.image.load('assets/shark.png')

# transform assets
octo = pygame.transform.scale(octoImg, (60, 60))
squid = pygame.transform.scale(squidImg, (40, 60) )
shell = pygame.transform.scale(shellImg, (30, 30))
shark = pygame.transform.scale(sharkImg, (60,30))

blue = (0, 153, 255)
clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8

class projectile(object):
  def __init__(self, x, y, radius, color):
      self.x = x
      self.y = y
      self.radius = radius
      self.color = color
      # self.facing = facing # this will determine direction of projectile 1 or -1
      self.vel = 8

  def draw(self, win):
      pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# class enemy(object):
#     def __init__(self, x, y, width, height, end):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.end = end
#         self.path = [self.x, self.end]
#         self.vel = 5
#         self.counter = 0
    
#     def draw(self, win):
#       self.move() # determine what the animation will do
 
#     def move(self):
#       if self.vel > 0: #moving right
#           if self.x + self.vel < self.path[1]:
#               self.x += self.vel
#           else: #if we are past this coordinate, change direction
#               self.vel = self.vel * -1
#       else: 
#           if self.x - self.vel > self.path[0]:
#               self.x += self.vel
#           else: 
#             self.vel = self.vel * -1

def redrawGameWindow(x, y, width, height):
    win.fill((blue))
    win.blit(octo, (x, y, width, height))
    win.blit(squid, (screenWidth-40, (screenHeight/2 -60), width, height))

    for bullet in bullets:
        bullet.draw(win)
    # win.blit(shell, ((screenWidth/2), (screenHeight/2 -60), width, height))
    # win.blit(shark, ((screenWidth/2 - 40), (screenHeight/2 -60 - 40), width, height))
    pygame.display.update() 

## main loop, check for collision, events 
octopus = player(0, (screenHeight/2 - 60), 60, 60)
bullets = []  # container for our bullet
# _shark = enemy(100, 410, 64, 64, 450)
run = True

## mainloop
while run:
    clock.tick(27)
    # pygame.time.delay(100) # game clock

    for event in pygame.event.get(): # event handling game
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets: 
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel # bullet is going to move vel direction
        else: 
            bullets.pop(bullets.index(bullet)) # pop off the bullet or delete them 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
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