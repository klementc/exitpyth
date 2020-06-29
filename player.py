import pygame
import math
import random
from level import Level
from tile import *
from levelLoader import LevelLoader

from globals import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        # TODO fine the right hitbox and player size
        #self.surf = pygame.image.load("test.png")
        self.image = pygame.image.load("sprites/char_noFlow.png").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        #self.image = pygame.Surface((25, 25))
        #self.image.fill((255, 0, 0))
        #self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.image.convert()
        #print("size: "+str(self.image.get_size()))

        self.rect = pygame.Rect(self.image.get_rect().left + 9, self.image.get_rect().top+5, 8, self.image.get_rect().height-10)

        #self.rect = pygame.Rect(self.image.get_rect().left+5.6, self.image.get_rect().top, 13.8, 15)

        #self.rect = pygame.Rect(self.image.get_rect().left+6.9, self.image.get_rect().top, 13.8, 15)
        self.rect.center = (12.5,12.5)

        #self.rect = self.surf.get_rect()

        self.username = "klem"
        self.tileSize = 25
        self.thudThresh = 2
        self.xF = 1
        self.dXVel = 5
        self.xMax = 20
        self.yMax = 20
        self.modX = 0
        self.playerXMaxNorm = 8
        self.playerXMax = 8
        self.playerYMax = 20
        self.xAcc = 0.8
        self.normalXAcc = 0.8
        self.burningXAcc = 1.5
        self.holdUp = False
        self.jumpCounter = 0
        self.holdDown = False
        self.holdDownX = 0
        self.rotSpeed = 1
        self.scaleY = 0
        self.xVel = 0
        self.hitHalf = False
        self.burningFlow = False
        self.playerXBurningMax = 50
        self.xLove = 0
        self.jumpLevel = False
        self.jumping = False
        self.xGrav = 0
        self.playerJump = False
        self.hops = -8
        self.yLove = 3
        self.completedLevel = False
        self.playerSize = 0
        self.typeOf = "deadaphant"
        self.yVel = 0
        self.yGrav = 0.6
        self.bounce = -.3
        self.beltSpeed = 2
        self.yF = 1
        self.flowType = 2
        self.fullFlow = False
        self.flowPoints = 0
        self.curLevel = Level()

        ll = LevelLoader()
        self.curLevel = ll.load(LEVEL1)
        self.curLevel.generateLevel()
        self.rect.left = self.curLevel.startPoint.x
        self.rect.top = self.curLevel.startPoint.y

    def init_level(self, lcode):
        self.curLevel = LevelLoader().load(lcode)
        self.curLevel.generateLevel()
        self.rect.left = self.curLevel.startPoint.x
        self.rect.top = self.curLevel.startPoint.y

    def movePlayer(self, pressed_keys):
        x = self.rect.left
        y = self.rect.top
        #print(x, y)
        #print(pressed_keys)

        # JUMP KEY
        if pressed_keys[K_UP]:
            print("up")
            if(not self.holdUp):
                self.doTheJump()
                self.holdUp = True
        else:
            self.holdUp = False
            self.jumpCounter = 0

        # CROUCH KEY
        if pressed_keys[K_DOWN]:
            print("down")
            self.holdDown = True
            self.xF = 0.9
            self.scaleY = 0.5
        else:
            self.holdDown = False
            self.xF = .7
            self.scaleY = 1

        # LEFT KEY
        if pressed_keys[K_LEFT]:
            if(not self.holdDown):
                if(self.xVel > -self.playerXMax):
                    self.xVel -= self.xAcc

        # RIGHT KEY
        elif pressed_keys[K_RIGHT]:
            if(not self.holdDown):
                if(self.xVel < self.playerXMax):
                    self.xVel += self.xAcc

        # LEFT OR RIGHT
        if(pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]):
            self.xF = 1
            if(self.holdDown and not self.hitHalf):
                self.xVel = self.xVel * 0.95
        else:
            self.xF = .5

        # FLOW
        if(self.burningFlow):
            self.playerXMax = self.playerXBurningMax
            self.xAcc = self.burningXAcc
        else:
            self.playerXMax = self.playerXMaxNorm
            self.xAcc = self.normalXAcc
            # TODO
            # this.playerXMax = Anim.ease(this.playerXMax,this.playerXNormalMax,0.3);

        # TODO stick not working, wrong hitbox sizes...
        # resize when crouching
        if(self.holdDown):
            #self.image = pygame.Surface((25, 25))
            #self.image.fill((255, 255, 255))
            #self.image = pygame.image.load("sprites/char_noFlow.png").convert()
            #self.image.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect.height = .5
        else:
            #self.image = pygame.Surface((25, 25))
            #self.image.fill((255, 255, 255))
            #self.image = pygame.image.load("sprites/char_flow.png").convert()
            #self.image.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect.height = 15

        self.handleFlow(pressed_keys)
        print(str(self.burningFlow)+" "+str(self.xAcc)+" "+str(self.xVel))



    def doTheJump(self):
        self.holdUp = True
        self.jumpCounter += 1

        if(self.yLove == 0 and self.jumpLevel and not self.hitHalf):
            self.playerJump = True
            self.jumpLevel = False
            self.yVel = self.hops
            self.yLove = 1

    def handleFlow(self, keys):
        if(self.flowType == 1):
            return
        if(self.flowType == 2):
            if(self.burningFlow and not (keys[K_SPACE] or keys[K_LSHIFT])):
                print("stop flow")
                self.burningFlow = False
            else:
                print("burn flow")
                self.burningFlow = True
        if(self.burningFlow):
            self.flowPoints = 100  # TODO
            if(not (keys[K_SPACE] or keys[K_LSHIFT])):
                self.burningFlow = False
            elif(self.flowPoints <= 0):
                self.flowPoints = 0
                self.burningFlow = False
        else:
            if(abs(self.xVel) > 2):
                self.flowPoints += 2
            else:
                self.flowPoints -= 20
            if(self.flowPoints < 0):
                self.flowPoints = 0
            if(self.flowPoints > 400):
                self.flowPoints = 400
                self.fullFlow = True
            else:
                self.fullFlow = False

            if((keys[K_SPACE] or keys[K_LSHIFT]) and self.flowPoints >= 100):
                self.burningFlow = True
        
        if(self.burningFlow):
            if(not self.jumpLevel):
                self.image = pygame.image.load("sprites/char_flow.png").convert()
            else:
                self.image = pygame.image.load("sprites/char_flow_j.png").convert()
            self.image.set_colorkey((0, 0, 0), RLEACCEL)
            #self.image.fill((0, 255, 0))

        else:
            if(not self.jumpLevel):
                self.image = pygame.image.load("sprites/char_noFlow.png").convert()
            else:
                self.image = pygame.image.load("sprites/char_noFlow_j.png").convert()
            self.image.set_colorkey((0, 0, 0), RLEACCEL)
            #self.image.fill((255, 255, 255))



    def ping(self, pressed_keys):
        if(self.completedLevel):
            return

        self.playerSize = 1
        self.typeOf = "deadaphant"
        self.thudTresh = 10

        # TODO verify if in game blablabla
        self.movePlayer(pressed_keys)

        self.handleHalfTiles()
        self.updateTileInteraction()
        self.spikeInteraction()
        self.levelInteraction()
        self.checkPointInteraction()
        # TODO self.teleporterInteraction()

    def updateTileInteraction(self):
        x = self.rect.left
        y = self.rect.top
        self.lastX = x
        self.lastY = y

        self.normalVertical()

        # TODO
        # if(self.curLevel.arrayMode):
        #     self.bounding2();
        # else:
        #      self.bounding();
        self.bounding()

        y = self.rect.top
        y = math.floor(y)
        self.rect.top = y

    def touchBlock(self, p1):
        if(p1.typeOf == 5):
            self.xVel += -self.beltSpeed
        elif(p1.typeOf == 6):
            self.xVel += self.beltSpeed
        elif(self.xVel > self.playerXMax):
            self.xVel = self.playerXMax
        elif(self.xVel < -self.playerXMax):
            self.xVel = -self.playerXMax

    def normalVertical(self):
        self.yVel = self.yVel + self.yGrav
        if(self.yGrav > 0):
            if(self.yLove == 1):
                if(not self.holdUp):
                    self.yVel = self.yVel + 1
                if(self.yVel >= 0):
                    self.yLove = 2
                    self.yVel = 0

            if(self.yLove == 2 or self.yLove == 3):
                if(self.yVel > 0):
                    self.yLove = 3

            if(self.yLove == 3 and self.yVel == 0 and not self.holdUp):
                self.yLove = 0
                self.holdCounter = 0

            if(self.yLove == 0 and self.yVel > 1.5):
                self.yLove = 3

            if(self.yLove == 0):
                self.playerJump = False

        else:
            if(self.yLove == 1):
                if(not self.holdUp):
                    self.yVel = self.yVel - 1

                if(self.yVel <= 0):
                    self.yLove = 2
                    self.yVel = 0

            if(self.yLove == 2 or self.yLove == 3):
                if(self.yVel < 0):
                    self.yLove = 3

            if(self.yLove == 3 and self.yVel == 0 and (not self.holdUp)):
                self.yLove = 0
                self.holdCounter = 0

            if(self.yLove == 0 and self.yVel < 1.5):
                self.yLove = 3

            if(self.yLove == 0):
                self.playerJump = False

        if(self.yLove != 0):
            self.jumpLevel = False

    def bounding(self):
        x = self.rect.left
        y = self.rect.top

        _loc_1 = 1
        if(self.yVel < 0):
            if(self.checkTile(x, y + self.yVel, 0, self.curLevel)):
                y = y + self.yVel
                if(self.yGrav < 0):
                    y = math.ceil(y)
            else:
                self.xVel = self.xVel * self.xF
                self.yVel = self.yVel * self.bounce
                self.rotSpeed = self.rotSpeed * -1
                if(self.tr):
                    y = self.tr.y + self.tileSize + self.rect.height  # self.targetObject.height
                    self.hitBlock(self.tr)
                    self.touchBlock(self.tr)

                elif(self.tl):
                    y = self.tl.y + self.tileSize + self.rect.height  # self.targetObject.height
                    self.hitBlock(self.tl)
                    self.touchBlock(self.tl)

                if(self.yVel < self.thudTresh and self.yVel > -self.thudTresh):
                    self.yVel = 0

                if(self.yGrav < 0):
                    self.jumping = False

        elif(self.yVel > 0):
            if(self.checkTile(x, y + self.yVel, 1, self.curLevel)):
                y = y + self.yVel
            else:

                self.xVel = self.xVel * self.xF
                self.yVel = self.yVel * self.bounce
                if(self.yGrav > 0):
                    self.jumping = False

                if(self.bl):
                    y = self.bl.y
                    self.touchBlock(self.bl)

                elif(self.br):
                    y = self.br.y
                    self.touchBlock(self.br)

                elif(self.bm):
                    y = self.bm.y
                    self.touchBlock(self.bm)

                if(self.yVel < self.thudTresh and self.yVel > -self.thudTresh):
                    self.yVel = 0

                if(abs(self.yVel) > 6):
                    self.rotSpeed = self.rotSpeed * \
                        (math.floor(random.random()*8) - 4)
                else:
                    self.rotSpeed = self.rotSpeed * 0.5

        if(self.xVel < 0):
            if(self.checkTile(x + self.xVel + self.modX, y, 3, self.curLevel)):
                x = x + (self.xVel + self.modX)
            else:
                self.yVel = self.yVel * self.yF
                self.xVel = self.xVel * self.bounce
                #                if(self.xVel < self.bounceTolerance):
                if(self.bl):
                    # self.targetObject.width / 2 + self.tileSize
                    x = self.bl.x + self.rect.width/2 + self.tileSize
                    self.touchBlock(self.bl)

                elif(self.br):
                    # self.targetObject.width / 2 + self.tileSize
                    x = self.br.x - self.rect.width / 2 + self.tileSize
                    self.touchBlock(self.br)

                if(self.xVel < self.thudTresh and self.xVel > -self.thudTresh):
                    self.xVel = 0.0
        elif(self.xVel > 0):
            if(self.checkTile(x + self.xVel + self.modX, y, 2, self.curLevel)):
                x = x + (self.xVel + self.modX)

            else:
                self.yVel = self.yVel * self.yF
                self.xVel = self.xVel * self.bounce
               #               if(self.xVel > self.bounceTolerance):

                if(self.br):
                    x = self.br.x - self.rect.width/2  # self.targetObject.width / 2
                    self.touchBlock(self.br)
                elif(self.bl):
                    x = self.bl.x + self.rect.width/2  # self.targetObject.width / 2
                    self.touchBlock(self.bl)
                if(self.xVel < self.thudTresh and self.xVel > -self.thudTresh):
                    self.xVel = 0.0

        if(self.xVel > self.xMax):
            self.xVel = self.xMax
        if(self.xVel < -self.xMax):
            self.xVel = -self.xMax
        if(self.yVel > self.yMax):
            self.yVel = self.yMax
        if(self.yVel < -self.yMax):
            self.yVel = -self.yMax

        self.rect.left = x
        self.rect.top = y
        #print("xvel: "+str(self.xVel)+" xF:"+str(self.xF))

        # TODO there isn't this in the game, but otherwise, weird left slide, find out why
        if(abs(self.xVel) < 0.0001):
            self.xVel = 0.0

    def checkTile(self, param1, param2, param3, param4):
        self.guyTL = False
        self.guyTR = False
        self.guyBL = False
        self.guyBR = False
        self.guyBM = False
        self.guyTM = False
        self.guyLM = False
        self.guyRM = False
        _loc_5 = self.rect.width  # targetObject.width;
        _loc_6 = self.rect.height  # targetObject.height;
        print("player: "+str(_loc_5)+" "+str(_loc_6))
        self.ctlx = param1 - _loc_5 / 2 + 1
        self.ctly = param2 - _loc_6 + 1
        self.ctrx = param1 + _loc_5 / 2 - 1
        self.ctry = param2 - _loc_6 + 1
        self.cbrx = param1 + _loc_5 / 2 - 1
        self.cbry = param2 - 1
        self.cblx = param1 - _loc_5 / 2 + 1
        self.cbly = param2 - 1
        self.clmx = param1 - _loc_5 / 2 + 1
        self.clmy = param2 - _loc_6 / 2 + 1
        self.ctmx = param1 + 1
        self.ctmy = param2 - _loc_6 + 1
        self.crmx = param1 + _loc_5 / 2 - 1
        self.crmy = param2 - _loc_6 / 2 + 1
        self.cbmx = param1 + 1
        self.cbmy = param2 - 1
        self.cmx = self.ctmx
        self.cmy = self.clmy
        self.tl = self.curLevel.getChildByName("tile" + str(math.floor(
            self.ctlx / self.tileSize)) + "x" + str(math.floor(self.ctly / self.tileSize)))
        self.tr = self.curLevel.getChildByName("tile" + str(math.floor(
            self.ctrx / self.tileSize)) + "x" + str(math.floor(self.ctry / self.tileSize)))
        self.br = self.curLevel.getChildByName("tile" + str(math.floor(
            self.cbrx / self.tileSize)) + "x" + str(math.floor(self.cbry / self.tileSize)))
        self.bl = self.curLevel.getChildByName("tile" + str(math.floor(
            self.cblx / self.tileSize)) + "x" + str(math.floor(self.cbly / self.tileSize)))
        self.tm = self.curLevel.getChildByName("tile" + str(math.floor(
            self.ctmx / self.tileSize)) + "x" + str(math.floor(self.ctmy / self.tileSize)))
        self.lm = self.curLevel.getChildByName("tile" + str(math.floor(
            self.clmx / self.tileSize)) + "x" + str(math.floor(self.clmy / self.tileSize)))
        self.bm = self.curLevel.getChildByName("tile" + str(math.floor(
            self.cbmx / self.tileSize)) + "x" + str(math.floor(self.cbmy / self.tileSize)))
        self.rm = self.curLevel.getChildByName("tile" + str(math.floor(
            self.crmx / self.tileSize)) + "x" + str(math.floor(self.crmy / self.tileSize)))
        self.mb = self.curLevel.getChildByName("tile" + str(math.floor(
            self.cbmx / self.tileSize)) + "x" + str(math.floor(self.cbly / self.tileSize)))

        if(self.tl):
            if(self.tl.type == 1):
                self.guyTL = True
                _loc_7 = self.tl
                # TODO self.pass(self.tl);
            else:
                self.guyTL = False
        if(self.tr):
            if(self.tr.type == 1):
                self.guyTR = True
                _loc_7 = self.tr
                # TODO self.pass(self.tr);
            else:
                self.guyTR = False
        if(self.br):
            if(self.br.type == 1):
                self.guyBR = True
                _loc_7 = self.br
                # TODO self.pass(self.br);
            elif(self.br.type == 2 and self.yVel > 0):
                self.guyBR = True
                _loc_7 = self.br
            else:
                self.guyBR = False
        if(self.bl):
            if(self.bl.type == 1):
                self.guyBL = True
                _loc_7 = self.bl
                # TODO self.pass(self.bl);
            elif(self.bl.type == 2 and self.yVel > 0):
                self.guyBL = True
                _loc_7 = self.bl
            else:
                self.guyBL = False
        if(self.tm):
            if(self.tm.type == 1):
                self.guyTM = True
                _loc_7 = self.tm
                # TODO self.pass(self.tm);
            else:
                self.guyTM = False
        if(self.bm):
            if(self.bm.type == 1):
                self.guyBM = True
                _loc_7 = self.bm
                # TODO self.pass(self.bm);
            else:
                self.guyBM = False
        if(self.lm):
            if(self.lm.type == 1):
                self.guyLM = True
                _loc_7 = self.lm
                # TODO self.pass(self.lm);
            else:
                self.guyLM = False
        if(self.rm):
            if(self.rm.type == 1):
                self.guyRM = True
                _loc_7 = self.rm
                # TODO self.pass(self.rm);
            else:
                self.guyRM = False
        if(self.yGrav > 0):
            if(self.guyBM or self.guyBL or self.guyBR):
                self.yLove = 0
                self.holdCounter = 0
            if(self.playerSize == 0):
                if(self.guyBM and self.guyBL or self.guyBM and self.guyBR):
                    self.jumpLevel = True
                if(self.guyBL and not self.guyTL):
                    self.jumpLevel = True
                if(self.guyBR and not self.guyTR):
                    self.jumpLevel = True
            if(self.playerSize == 1):
                if(self.guyBR and self.guyBL):
                    self.jumpLevel = True
                if(self.guyBL and not self.guyTL):
                    self.jumpLevel = True
                if(self.guyBR and not self.guyTR):
                    self.jumpLevel = True
        else:
            if(self.guyTM or self.guyTL or self.guyTR):
                self.yLove = 0
                self.holdCounter = 0
            if(self.guyTM and self.guyTL or self.guyTM and self.guyTR):
                self.jumpLevel = True

        if(param3 == 0):
            if(self.guyTL or self.guyTR):
                return False
        elif(param3 == 1):
            if(self.guyBR or self.guyBL):
                return False
        elif(param3 == 2):
            if(self.guyTR or self.guyBR):
                return False
        elif(param3 == 3):
            if(self.guyTL or self.guyBL):
                return False
        else:
            if(self.guyTL or self.guyBL):
                return False
        return True

    def hitBlock(self, p1):
        pass

    def levelInteraction(self):
        y = self.rect.top
        if((self.curLevel.maxHeight <= 550 and y > 650) or (self.curLevel.maxHeight > 550 and y > self.curLevel.maxHeight+150)):
            self.kill()
        if(self.hitTestObject(self.curLevel.endPoint)):
            self.completedLevel = True

    def kill(self):
        self.rect.top = self.curLevel.startPoint.y
        self.rect.left = self.curLevel.startPoint.x
        # TODO checkpoints
        pass

    def hitTestObject(self, o):
        # TODO simple boundings verif (pas sur mdr)
        
        if(o == None):
            return False

        if(o.type == 5):
            r = o.hitA
        # if spike, TODO same for some others
        else:
            r = o.rect

        if(self.rect.left > r.left and self.rect.left < r.right and self.rect.top > r.top and self.rect.top < r.bottom):
            return True

        if(self.rect.right < r.right and self.rect.right > r.left and self.rect.bottom > r.top and self.rect.bottom < r.bottom):
            return True

        return False


    def handleHalfTiles(self):
        self.hitHalf = False
        for ht in self.curLevel.halfTiles:
            if(self.hitTestObject(ht)):
                self.hitHalf = True
                if(self.jumpLevel == False):
                    self.xVel = 0
                elif(not self.holdDown):
                    self.xVel = self.xVel*0.7
            print("HALFFFFFF: "+str(self.hitHalf))

    def spikeInteraction(self):
        for spike in self.curLevel.spikes:
            if(self.hitTestObject(spike)):
                self.kill()
                return

    def checkPointInteraction(self):
        for ch in self.curLevel.checkPoints:
            if(self.hitTestObject(ch)):
                if(self.curLevel.startPoint != ch):
                    # TODO verif on l'a pas deja
                    self.curLevel.startPoint = ch