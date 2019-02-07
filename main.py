import pygame as pg
import random
from settings import *

class Game:
    def __init__(self):
        # initialize game window, etc
        # Set up pygame
        pg.init()
        pg.display.set_caption(title)
        self.windowSurface = self.screen =pg.display.set_mode((screenWidth, screenHeight))
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # Start a new game
        self.run()

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

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(blue)
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