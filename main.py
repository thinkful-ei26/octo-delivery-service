import pygame as pg
import random, sys
from settings import *
from objects.player import Player
from objects.enemy import Enemy
from objects.projectile import Projectile
from objects.package import Package

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.display.set_caption(title)
        self.screen = pg.display.set_mode((screenWidth, screenHeight))
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
    
    def new(self):
        # Start a new game
        self.score = 0
        self.player = Player(0, (screenHeight/2 - 60), 60, 60)
        self.font = pg.font.SysFont('helvetica', 30, True)
        self.bullets = []  # container for our bullet
        self.packages = []
        self.shark = Enemy(screenWidth-100, (screenHeight/2 - 60), 60, 40, 800)
        self.shark2 = Enemy(screenWidth-200, (screenHeight/3 - 60), 60, 40, 800)
        self.shark3 = Enemy(screenWidth-300, (screenHeight/5 - 60), 60, 40, 800)
        self.shark4 = Enemy(screenWidth-200, (400 - 60), 60, 40, 800)
        self.shark5 = Enemy(screenWidth-300, (500 - 60), 60, 40, 800)
        self.inkLoop = 0
        self.run()
        self.music = pg.mixer.music.load('music.mp3')
        pg.mixer.music.play(-1)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        # Game Loop - Update
        #if player reaches ~3/4 of screen create whirlpool suction down
        if self.player.y >= screenHeight - 100:
            self.player.y += abs(self.player.vel)
            self.player.hit(self.screen)
               
    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            keys = pg.key.get_pressed()

            ## ============== INTERNAL GAME CONTROLS ==============
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running == False
              
            if keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()

            ## octopus movement
            if keys[pg.K_LEFT] and self.player.x > self.player.vel:
                self.player.x -= self.player.vel
            if keys[pg.K_RIGHT] and self.player.x < screenWidth - self.player.width:
                self.player.x += self.player.vel
            if keys[pg.K_UP] and self.player.y > self.player.vel:
                self.player.y -= self.player.vel
            if keys[pg.K_DOWN] and self.player.y < screenWidth - self.player.width:
                self.player.y += self.player.vel
            
                ## add more bullets to octopus
            if keys[pg.K_SPACE] and self.inkLoop == 0:
                # bulletSound.play()
                if len(self.bullets) < 30:
                    self.bullets.append(Projectile(round(self.player.x + self.player.width //2), round(self.player.y + self.player.height//2), 6, (0,0,0)))
                
                self.inkLoop = 1

            ## ============== OCTOPUS & SHARK COLLISION ==============
            self.playerCollision(self.player, self.shark, self.score)
            self.playerCollision(self.player, self.shark2, self.score)
            self.playerCollision(self.player, self.shark3, self.score)
            self.playerCollision(self.player, self.shark4, self.score)
            self.playerCollision(self.player, self.shark5, self.score)

            ## ============== BULLET COLLISION LOGIC ==============
            # shoots bullets one at a time by delaying
            if self.inkLoop > 0:
                self.inkLoop += 1
            if self.inkLoop > 3:
                self.inkLoop = 0

            for self.bullet in self.bullets: 

                ## BULLET & SHARK COLLISION
                self.enemyCollision(self.shark, self.score)
                self.enemyCollision(self.shark2, self.score)  
                self.enemyCollision(self.shark3, self.score) 
                self.enemyCollision(self.shark4, self.score)  
                self.enemyCollision(self.shark5, self.score)       
                if self.bullet.x < 800 and self.bullet.x > 0:
                    self.bullet.x += self.bullet.vel # bullet is going to move vel direction
                else: 
                    self.bullets.pop(self.bullets.index(self.bullet)) # pop off the bullet or delete them 

            ## ============== PACKAGE COLLISION LOGIC ==============
            for self.package in self.packages: 
            
                ## OCTOPUS & PACKAGE COLLISION  
                self.packageCollision(self.player)  
                if self.package.x < 800 and self.package.x > 0:
                    self.package.x += self.package.vel # package is going to move vel direction
                else: 
                    self.packages.pop(self.packages.index(self.package))
            
            ## add packages on load, will only reload if package disappears
            packageSize = 40
            pX = random.randint(0, screenWidth - packageSize)
            pY = random.randint(0, screenHeight - packageSize)
            if len(self.packages) <= 2:
                  self.packages.append(Package(pX, pY, packageSize, packageSize, brown))

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(blue)
        self.draw_text(str(self.score), 22, black, 10, 10)
        self.text = self.font.render('Packages: ' + str(self.player.collectCount), 1, black)
        self.screen.blit(self.text, (590, 0))
        self.player.draw(self.screen)
        self.shark.draw(self.screen)
        self.shark2.draw(self.screen)
        self.shark3.draw(self.screen)
        self.shark4.draw(self.screen)
        self.shark5.draw(self.screen)

        ## draw bullets
        for self.bullet in self.bullets:
            # hitSound.play()
            self.bullet.draw(self.screen)
            # print('bullet', self.bullet)

        ## draw packages
        for self.package in self.packages:
            self.package.draw(self.screen)

        if self.player.collectCount == 8:
            self.text2 = self.font.render('Collected all 8 packages!', 1, green)
            self.screen.blit(self.text2, (screenWidth/2, screenHeight/2))
        
        pg.display.update() 
    
    def show_start_screen(self):
        # game splash/start screen
        pass
    
    def show_go_screen(self):
        # game over/continue 
        pass
    
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def enemyCollision(self, enemyObj, score):
      if self.bullet.y - self.bullet.radius < enemyObj.hitbox[1] + enemyObj.hitbox[3] and self.bullet.y + self.bullet.radius > enemyObj.hitbox[1]: # phrase 1 checks to see if the bullet is in the bottom of our shark, phrase 2 checks the top
          if self.bullet.x + self.bullet.radius > enemyObj.hitbox[0] and self.bullet.x - self.bullet.radius < enemyObj.hitbox[0] + enemyObj.hitbox[2]: # check if bullet is within left & right x coord of shark hitbox
              enemyObj.hit()
              if enemyObj.visible == True:
                  self.score += 10
                  self.bullets.pop(self.bullets.index(self.bullet))
    
    def playerCollision(self, player, enemy, score):
        if enemy.visible == True: # octopus no longer sustains damage if enemy is not visible
            if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
                if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                    player.hit(self.screen)
                    self.score -= 5
      
    def packageCollision(self, player):
        if self.player.hitbox[1] < self.package.hitbox[1] + self.package.hitbox[3] and self.player.hitbox[1] + self.player.hitbox[3] > self.package.hitbox[1]:
            if self.player.hitbox[0] + self.player.hitbox[2] > self.package.hitbox[0] and self.player.hitbox[0] < self.package.hitbox[0] + self.package.hitbox[2]:
                  self.player.collect(self.screen)
                  if self.player.visible == True:
                      self.score += 100
                      print('score: ', self.score)
                      self.packages.pop(self.packages.index(self.package))

    

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen() #game over screen

pg.quit()