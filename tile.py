import pygame
import math
import random

from globals import *

class Tile(pygame.sprite.Sprite):
  
    def __init__(self, x=0, y=0, type=1):
      super(Tile, self).__init__()
      self.surf = pygame.Surface((25, 25))
      self.surf.fill((0, 255, 255))
      self.rect = self.surf.get_rect()

      self.tileSize = 25
      self.type = type
      self.painted = False
      self.rotation = 0
      #TODO
      #x = round(self.rect.left)
      #y = round(self.rect.top)
      self.rect.x = x+12.5
      self.rect.y = y+25
      self.x = x
      self.y = y
      #####

      self.holdX = x
      self.holdY = y
      self.posX = math.floor(x/self.tileSize)
      self.posY = math.floor(y/self.tileSize)
      self.typeOf = type

      self.name = "tile"+str(self.posX)+"x"+str(self.posY)

class TileOpaque(pygame.sprite.Sprite):
  
    def __init__(self):
      super(TileOpaque, self).__init__()

class Block(Tile):
  def __init__(self, x=0, y=0):
      super(Block, self).__init__(x,y,type = 1)
      #self.surf = pygame.Surface((25, 25))
      self.surf = pygame.image.load("sprites/block.png").convert()
      self.surf.set_colorkey((255, 255, 255), RLEACCEL)
      #self.rect = self.surf.get_rect()
      #self.surf.fill((200, 200, 200))
      #self.surf.fill((128,128,128), self.surf.get_rect().inflate(-2, -2))

class StartBlock(Tile):
  def __init__(self, x=0, y=0):
      super(StartBlock, self).__init__(x,y,type = 2)
      #self.surf = pygame.Surface((25, 25))
      self.surf = pygame.image.load("sprites/start.png").convert()
      self.surf.set_colorkey((0, 0, 0), RLEACCEL)