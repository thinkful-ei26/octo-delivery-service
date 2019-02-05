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

# transform assets
octo = pygame.transform.scale(octoImg, (60, 60))
squid = pygame.transform.scale(squidImg, (40, 60) )
shell = pygame.transform.scale(shellImg, (30, 30))

blue = (0, 153, 255)
clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5


def redrawGameWindow(x, y, width, height):
    win.fill((blue))
    win.blit(octo, (0, (screenHeight/2 - octopus.height), width, height))
    win.blit(squid, (screenWidth-40, (screenHeight/2 -60), width, height))
    win.blit(shell, ((screenWidth/2), (screenHeight/2 -60), width, height))
    pygame.display.update() 

## main loop, check for collision, events 
octopus = player(300, 200, 60, 60)
run = True
while run:
    clock.tick(27)
    pygame.time.delay(100) # game clock
    for event in pygame.event.get(): # event handling game
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
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
3. 
'''