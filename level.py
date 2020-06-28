import pygame
import math
import random

from globals import *
from tile import *


class Level():
    def __init__(self):
        self.tDict = {}
        self.arrayMode = False
        self.tMaxX = 100
        self.tMaxY = 50
        self.checkPoints = []
        self.halfTiles = []
        self.plates = []
        self.spikes = []
        self.levelName = "levelName"
        self.toPush = []
        self.obstacleColour = 13421772
        self.timeString = ""
        self.tArr = []
        self.createdArray = False
        self.teleporters = []
        self.swingingAxes = []
        self.lastX = 0
        self.lastY = 0
        self.tiles = []
        self.checkPointID = 0
        self.fallingSpikes = []
        self.timeRank = ""
        self.laserGuns = []
        self.levelWidth = 400
        self.maxWidth = 0
        self.laserCannons = []
        self.bouncers = []
        self.grinders = []
        self.levelHeigh = 800
        self.maxHeight = 0
        self.levelType = "SP"
        self.popSpikes = []
        self.flowType = 0
        self.allowSuicide = False
        self.endPoint = None
    
    def createLaserCannon(self, p1):
        # TODO
        pass
    
    def generateLevel(self):
        # TODO
        # this.preInitCheck(); ???
        self.maxWidth = 0
        self.maxHeight = 0
        self.image = pygame.Surface((3000,3000))
        loc1 = 0
        for l in self.toPush:
            #print("generate tile:"+str(l[0].x))
            loc2 = l[0]
            type = int(l[1])

            if(self.levelType=="SP"):
                if(loc2.type == 1):
                    tile = Block(round(loc2.x), round(loc2.y))
                else:
                    tile = Tile(round(loc2.x), round(loc2.y),loc2.type)
            else:
                tile = TileOpaque()
            # TODO set up this instead of the 3 next lines
            #if(loc2.rotation%90 == 0):
            #    tX = round(tile.rect.left)
            #    tY = round(tile.rect.top)
                
            #else:
            #    tX = round(loc2.x)
            #    tY = round(loc2.y)
            #    tile.rotation = loc2.rotation

            tX = round(loc2.x)
            tY = round(loc2.y)
            tile.rotation = loc2.rotation

            tile.x = tX
            tile.y = tY
            
            #print("tile pos: "+str(tX)+" "+str(tY)+" type:"+str(tile.typeOf))
            #if(tile.type == 1):
            #    pygame.draw.rect(self.image, (128,128,128), pygame.Rect(tile.x+12.5, tile.y+25, tile.tileSize, tile.tileSize),1)
            #elif(tile.type == 2):
            #    pygame.draw.rect(self.image, (255,0,0), pygame.Rect(tile.x+12.5, tile.y+25, tile.tileSize, tile.tileSize),1)


            if(tile.x > self.maxWidth):
                self.maxWidth = tile.x
            if(tile.y > self.maxHeight):
                self.maxHeight = tile.y
            tile.typeOf = type

            if(tile.typeOf != 3 and loc2.rotation%90 == 0 and (tile.typeOf != 99 or loc2.name[:1] != "t")):
                self.tiles.append(tile)
            
            elif(tile.typeof == 3):
                self.halfTiles.append(tile)
            
            # TODO addChild(_tile);
            if(type != 4):
                if(self.levelType == "SP"):
                    # Anim.colourMe(_tile,this.levelColour)
                    pass
            # TODO _tile.gotoAndStop(_tile.typeOf);   
            if(type == 2):
                self.startPoint = tile
            if(type == 4):
                self.endPoint = tile 
            if(type == 1 or type==99):
                # TODO
                if(tile.x < 3000):
                    # TODO addChild(_tile);
                    if(type == 1):
                        # TODO ADD rotation
                        #pygame.draw.rect(self.image, (255,0,0),pygame.Rect(tile.x+25, tile.y+50, tile.tileSize, tile.tileSize))
                        tile.visible = False
            if(self.arrayMode):
                self.tArr[round(loc2.y/25)][round(loc2.x/25)] = type
                if(type == 1 or type == 99):
                    if(tile.x < 3000):
                        pygame.draw.rect(self.image, pygame.Rect(tile.x, tile.y, tile.tileSize, tile.tileSize))
                        tile = None
            if(type != 00):
                loc2 = None

            loc1 = int(loc1+1)
        #TODO self.toPush =[]

        if(self.arrayMode):
            #TODO self.tiles = []
            pass
        loc1 = 0
        while(loc1 < len(self.teleporters)):
            self.teleporters[loc1].init()
            loc1 += 1
        self.uniqueLevelInit()

        print("generated level")

    
    def uniqueLevelInit(self):
        pass

    def init(self, game):
        # TODO
        pass

    def addCheckpoint(self, p1):
        # TODO
        pass    

    def repaint(self):
        # TODO
        pass

    def createTreadmillBlock(self, p1, p2):
        # TODO
        pass

    def createGrinder(self, p1):
        # TODO
        pass

    def createTeleporter(self, p1):
        # TODO
        pass

    def createSpikeAt(self, p1):
        # TODO
        pass

    def createPopSpikes(self, p1):
        # TODO
        pass

    def createBouncer(self, p1):
        # TODO
        pass

    def createSpike(self, p1):
        # TODO
        pass

    def createStartPoint(self, p1):
        self.createTileAt(p1, 2)

    def createPlate(self, p1):
        # TODO
        pass

    def createHalfBlock(self, p1):
        # TODO
        pass

    def createEndPoint(self, p1):
        # TODO
        pass

    def getTileArray(self):
        # TODO
        pass

    def createLaserGun(self,p1):
        # TODO
        pass

    def createTileAt(self, p1, p2=1):
        self.tDict[p1.name]=p1
        self.toPush.append([p1, p2])

    def createSwingingAxe(self, p1):
        # TODO
        pass

    def createArray(self):
        # TODO
        pass

    def killTiles(self):
        # TODO
        pass

    def createTile(self, p1):
        self.createTileAt(p1, 1)

    def createFallingSpike(self, p1):
        # TODO
        pass

    def setPlayer(self, p1):
        # TODO
        pass

    def createInvisibleBlock(self, p1):
        # TODO
        pass

    def getChildByName(self, name):
        #print(str(self.tDict))
        #print("child: "+str(self.tDict.get(name)))
        return self.tDict.get(name)