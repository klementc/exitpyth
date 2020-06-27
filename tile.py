import pygame
import math
import random

from globals import *

class Tile(pygame.sprite.Sprite):
  
    def __init__(self, x=0, y=0):
      super(Tile, self).__init__()
      self.surf = pygame.Surface((25, 25))
      self.surf.fill((255, 255, 255))
      self.rect = self.surf.get_rect()

      self.tileSize = 25
      self.type = 1
      self.painted = False
      self.rotation = 0
      #TODO
      #x = round(self.rect.left)
      #y = round(self.rect.top)
      self.x = x
      self.y = y
      #####

      self.holdX = x
      self.holdY = y
      self.posX = math.floor(x/self.tileSize)
      self.posY = math.floor(y/self.tileSize)
      self.typeOf = 1

      self.name = "tile"+str(self.posX)+"x"+str(self.posY)

class TileOpaque(pygame.sprite.Sprite):
  
    def __init__(self):
      super(TileOpaque, self).__init__()