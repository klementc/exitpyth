import pygame
import math
import random

from globals import *

class OnlineP(pygame.sprite.Sprite):
  
  def __init__(self, olPos):
    super(OnlineP, self).__init__()
    self.surf = pygame.Surface((25, 25))
    self.surf.fill((0, 255, 255))
    self.rect = self.surf.get_rect()
    self.rect.x = olPos[0]
    self.rect.y = olPos[1]