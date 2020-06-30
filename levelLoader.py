import math
import random

from globals import *
from tile import *
from level import Level


class LevelLoader:
  def __init__(self):
    pass

  def load(self, stri):
    level = Level()

    for tDesc in stri.split(";"):
      type,x,y = tDesc.split(",")
      #print(x, y, type)
      if(type == "1"):
        t = Tile(int(x), int(y),1)
        #print("t.type: "+str(t.type))
        level.createTile(t)
      elif(type == "2"):
        t = Tile(int(x), int(y),2)
        level.createStartPoint(t)
      elif(type == "3"):
        t = Tile(int(x), int(y), 3)
        level.createHalfBlock(t)
      elif(type == "5"):
        t = Spike(int(x), int(y))
        level.createSpike(t)
      elif(type == "6"):
        t = Checkpoint(int(x), int(y))
        level.addCheckpoint(t)
      elif(type == "7"):
        t = HiddenBlock(int(x), int(y))
        level.createInvisibleBlock(t)
      else:
        t = Tile(int(x), int(y), 5)
        level.createTile(t)

    return level

l = LevelLoader()
print(l.load("0,0,1;25,0,1"))