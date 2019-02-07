import pygame
from settings import *

## ============== PROJECTILE ==============
class Projectile(object):
  def __init__(self, x, y, radius, color):
      self.x = x
      self.y = y
      self.radius = radius
      self.color = color
      self.vel = 8
      self.hitbox = (self.x-8, self.y-5, 15, 15)

  def draw(self, windowSurface):
      pygame.draw.circle(windowSurface, self.color, (self.x, self.y), self.radius)
      ## MOVING HITBOX   
      self.hitbox = (self.x-8, self.y-5, 15, 15)
      # pygame.draw.rect(windowSurface, red, self.hitbox, 2)