import pygame, sys, random
from pygame.locals import *
from objects.player import player
from objects.enemy import enemy
from objects.projectile import projectile
from objects.package import Package

# Set up pygame
pygame.init()

# Set up the window
screenWidth = 800
screenHeight = 600
windowSurface = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('OctoGun: Delivery Service')

# load assets
squidImg = pygame.image.load('assets/squid.png')
shellImg = pygame.image.load('assets/shell.png')

# transform assets
squid = pygame.transform.scale(squidImg, (40, 60) )
shell = pygame.transform.scale(shellImg, (30, 30))

# Set up colors
blue = (0, 153, 255)
red = (255, 0, 0)
black = (0,0,0)
green = (0, 255, 0)
brown = (222,184,135)

# Set up internal game controls
clock = pygame.time.Clock()

# bulletSound = pygame.mixer.Sound('bullet.wav')
# hitSound = pygame.mixer.Sound('hit.wav')
# music = pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)

score = 0

## ============== REDRAW GAME WINDOW ============== 
def redrawGameWindow():
    windowSurface.fill((blue))
    text = font.render('Score: ' + str(score), 1, black)
    windowSurface.blit(text, (590, 0))
    octopus.draw(windowSurface)
    shark.draw(windowSurface)
    shark2.draw(windowSurface)
    shark3.draw(windowSurface)
  
    ## draw bullets
    for bullet in bullets:
        #print('bullet: ',bullet)
        # hitSound.play()
        bullet.draw(windowSurface)

    ## draw packages in range of 8
    for package in packages:
        pygame.draw.rect(windowSurface, brown, packages[i])
        #packages.draw(windowSurface, package, packages)
        

    pygame.display.update() 

## ============== DEFINE GAME OBJECTS ==============
font = pygame.font.SysFont('helvetica', 30, True)
octopus = player(0, (screenHeight/2 - 60), 60, 60)
bullets = []  # container for our bullet
shark = enemy(screenWidth-100, (screenHeight/2 - 60), 60, 40, 800)
shark2 = enemy(screenWidth-200, (screenHeight/3 - 60), 60, 40, 800)
shark3 = enemy(screenWidth-300, (screenHeight/5 - 60), 60, 40, 800)
inkLoop = 0

# Set up packages
packageCounter = 40
NEWPACKAGE = 0
PACKAGESIZE = 20
packages = []

for i in range(8):
      packages.append(pygame.Rect(random.randint(0, screenWidth - PACKAGESIZE), random.randint(0, screenHeight - PACKAGESIZE), PACKAGESIZE, PACKAGESIZE))

def enemyCollision(enemyObj, scoreObj):
    if bullet.y - bullet.radius < enemyObj.hitbox[1] + enemyObj.hitbox[3] and bullet.y + bullet.radius > enemyObj.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
        if bullet.x + bullet.radius > enemyObj.hitbox[0] and bullet.x - bullet.radius < enemyObj.hitbox[0] + enemyObj.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
            enemyObj.hit()
            if enemyObj.visible == True:
                scoreObj += 1
                bullets.pop(bullets.index(bullet))

## ============== MAIN LOOP ==============
while True:  
# Check for events:
    clock.tick(27) # game clock

    if octopus.hitbox[1] < shark.hitbox[1] + shark.hitbox[3] and octopus.hitbox[1] + octopus.hitbox[3] > shark.hitbox[1]:
        if octopus.hitbox[0] + octopus.hitbox[2] > shark.hitbox[0] and octopus.hitbox[0] < shark.hitbox[0] + shark.hitbox[2]:
            octopus.hit(windowSurface)
            score -= 5

    # shoots bullets one at a time by delaying
    if inkLoop > 0:
        inkLoop += 1
    if inkLoop > 3:
        inkLoop = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ## ============== BULLET COLLISION LOGIC ==============
    for bullet in bullets: 

        ## BULLET & SHARK COLLISION
        enemyCollision(shark, score)
        enemyCollision(shark2, score)  
        enemyCollision(shark3, score)    

        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel # bullet is going to move vel direction
        else: 
            bullets.pop(bullets.index(bullet)) # pop off the bullet or delete them 

    ## ============== PACKAGE COLLISION LOGIC ==============

    # for i in range(8):
    #   packages.append(pygame.Rect(random.randint(0, screenWidth - PACKAGESIZE), random.randint(0, screenHeight - PACKAGESIZE), PACKAGESIZE, PACKAGESIZE))
    # for package in packages[:]:
    #     if player.colliderect(package):
    #         packages.remove(package)

    if event.type == MOUSEBUTTONUP:
        packages.append(pygame.Rect(event.pos[0], event.pos[1], PACKAGESIZE, PACKAGESIZE))

    packageCounter += 1
    if packageCounter >= NEWPACKAGE:
         ## Add new package:
         packageCounter = 0
         packages.append(pygame.Rect(random.randint(0, screenWidth - PACKAGESIZE), random.randint(0, screenHeight - PACKAGESIZE), PACKAGESIZE, PACKAGESIZE))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    ## add more bullets to octopus
    if keys[pygame.K_SPACE] and inkLoop == 0:
        # bulletSound.play()
        if len(bullets) < 30:
            bullets.append(projectile(round(octopus.x + octopus.width //2), round(octopus.y + octopus.height//2), 6, (0,0,0)))
        
        inkLoop = 1

    ## octopus movement
    if keys[pygame.K_LEFT] and octopus.x > octopus.vel:
        octopus.x -= octopus.vel
    if keys[pygame.K_RIGHT] and octopus.x < screenWidth - octopus.width:
        octopus.x += octopus.vel
    if keys[pygame.K_UP] and octopus.y > octopus.vel:
        octopus.y -= octopus.vel
    if keys[pygame.K_DOWN] and octopus.y < screenWidth - octopus.width:
        octopus.y += octopus.vel
    
    redrawGameWindow()

pygame.quit()

# detect collision:
'''
[] octo & package collision logic
[] add package score when octo collides
[] octo health render, decrease when touching shark
[] next scene => octo & squid => end game 
[DONE] render octo & octo moving
[DONE] octo has projectiles
[DONE] add enemy shark: has health bar, is moving correct direction
[DONE] add packages: 1. create package class, 2. render 
[DONE] fix bug on shark collision
[DONE] add more sharks
'''