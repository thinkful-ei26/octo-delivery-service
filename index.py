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
width = 40
height = 40
vel = 25

octoImg = pygame.image.load('assets/octopic.png')

def redrawGameWindow(x, y, width, height):
    win.fill((blue))
    win.blit(octoImg, (x, y, width, height))
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