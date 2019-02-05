import pygame

pygame.init()

screenWidth = 800
screenHeight = 600

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Octo Demo')

blue = (0, 153, 255)
red = (255, 0, 0)

x = 0
y = 400
y = 200
width = 10
height = 10
vel = 25

# load assets
octoImg = pygame.image.load('assets/octopic.png')
squidImg = pygame.image.load('assets/squid.png')
shellImg = pygame.image.load('assets/shell.png')

# transform assets
octo = pygame.transform.scale(octoImg, (60, 60))
squid = pygame.transform.scale(squidImg, (40, 60) )
shell = pygame.transform.scale(shellImg, (30, 30))

def redrawGameWindow(x, y, width, height):
    win.fill((blue))
    win.blit(octo, (x, y, width, height))
    win.blit(squid, (screenWidth-40, (screenHeight/2 -60), width, height))
    win.blit(shell, ((screenWidth/2), (screenHeight/2 -60), width, height))
    pygame.display.update() 

## main loop, check for collision, events 
run = True
while run:
    pygame.time.delay(100) # game clock
    for event in pygame.event.get(): # event handling game
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenWidth - width:
        y += vel

    redrawGameWindow(x, y, width, height)
    
pygame.quit()