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
        # Set up pygame
        pg.init()
        pg.display.set_caption(title)
        self.screen = pg.display.set_mode((screenWidth, screenHeight))
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # Start a new game
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
            self.clock.tick(27)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        # Game Loop - Update
        pass
               
    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running == False
            
            keys = pg.key.get_pressed()

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

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(blue)
        self.text = self.font.render('Packages: ' + str(self.player.collectCount), 1, black)
        self.screen.blit(self.text, (590, 0))
        self.player.draw(self.screen)
        self.shark.draw(self.screen)
        self.shark2.draw(self.screen)
        self.shark3.draw(self.screen)
        self.shark4.draw(self.screen)
        self.shark5.draw(self.screen)
        pg.display.update() 
    
    def show_start_screen(self):
        # game splash/start screen
        pass
    
    def show_go_screen(self):
        # game over/continue 
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen() #game over screen

pg.quit()