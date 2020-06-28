import math


class TileObject:

    def __init__(self):
        self.thudThresh = 2
        self.holdDown = False
        self.guyTL = False
        self.guyTM = False
        self.xVel = 0
        self.guyTR = False
        self.xLove = 0
        self.guyLM = False
        self.yMax = 20
        self.cblx = 0
        self.cbly = 0
        self.holdCounter = 0
        self.yAcc = 1
        self.hops = -8
        self.cbmy = 0
        self.cmx = 0
        self.cbmx = 0
        self.crmx = 0
        self.crmy = 0
        self.yVel = 0
        self.bounceTorelance = 0
        self.cmy = 0
        self.ctrx = 0
        self.ctry = 0
        self.yGrav = 0.6
        self.playerSize = 0
        self.lastY = 0
        self.bounce = -0.3
        self.dXVel = 9
        self.yLove = 3
        self.lastX = 0
        self.modX = 0
        self.playerJump = False
        self.rotSpeed = 1
        self.typeOf = "none"
        self.holdUp = False
        self.ctlx = 0
        self.ctly = 0
        self.guyRM = False
        self.xMax = 30
        self.xF = 0
        self.tileSize = 25
        self.clmx = 0
        self.clmy = 0
        self.guyBM = False
        self.guyBR = False
        self.guyBL = False
        self.ctmy = 0
        self.cbrx = 0
        self.cbry = 0
        self.dYVel = 0
        self.xAcc = 1
        self.ctmx = 0
        self.yF = 1
        self.jumpCounter = 0
        self.jumping = False
        self.jumpLevel = False

        self.curLevel = new Level();


        # TODOOOOOOOOOOO
    def bounding2():
        if(self.yVel < 0):
            if(self.checkArray(x,y + self.yVel,0,self.curLevel)):
                y = y + self.yVel;
                if(self.yGrav < 0):
                    y = math.ceil(y);
            
            else:
                self.xVel = self.xVel * self.xF;
                self.yVel = self.yVel * self.bounce;
                self.rotSpeed = self.rotSpeed * -1;
                if(self.tr):
                    y = self.tr.y + self.tileSize + self.targetObject.height;
                    self.hitBlock(self.tr);
                    self.touchBlock(self.tr);
               
                elif(self.tl):
                    y = self.tl.y + self.tileSize + self.targetObject.height;
                    self.hitBlock(self.tl);
                    self.touchBlock(self.tl);
               
                if(self.yVel < self.thudTresh and self.yVel > -self.thudTresh):
                    self.yVel = 0;
               
                if(self.yGrav < 0):
                    self.jumping = false;
         
        elif(self.yVel > 0):
            if(self.checkArray(x,y + self.yVel,1,self.curLevel)):
                y = y + self.yVel;
            
            else:
                if(self.yVel <= self.bounceTolerance):
                    if(self.yVel > self.bounceTolerance):
                        pass;
               
                self.xVel = self.xVel * self.xF;
                self.yVel = self.yVel * self.bounce;
                if(self.yGrav > 0):
                    self.jumping = false;
               
                if(self.bl):
                    y = self.bl.y;
                    self.touchBlock(self.bl);
               
                elif(self.br):
                    y = self.br.y;
                    self.touchBlock(self.br);
               
                elif(self.bm):
                    y = self.bm.y;
                    self.touchBlock(self.bm);
               
                if(self.yVel < self.thudTresh and self.yVel > -self.thudTresh):
                    self.yVel = 0;
               
                if(math.abs(self.yVel) > 6):
                    self.rotSpeed = self.rotSpeed * (math2.random(8) - 4);
               
                else:
                    self.rotSpeed = self.rotSpeed * 0.5;
            
         
        if(self.xVel < 0):
            if(self.checkArray(x + self.xVel,y,3,self.curLevel)):
                x = x + self.xVel;
            
            else:
                self.yVel = self.yVel * self.yF;
                self.xVel = self.xVel * self.bounce;
                if(self.xVel < self.bounceTolerance):
                    pass;
                if(self.bl):
                    x = self.bl.x + self.targetObject.width / 2 + self.tileSize;
                    self.touchBlock(self.bl);
               
                elif(self.br):
                    x = self.br.x - self.targetObject.width / 2 + self.tileSize;
                    self.touchBlock(self.br);
               
                if(self.xVel < self.thudTresh and self.xVel > -self.thudTresh):
                    self.xVel = 0;
         
        elif(self.xVel > 0):
            if(self.checkArray(x + self.xVel,y,2,self.curLevel)):
                x = x + self.xVel;
            
            else:
                self.yVel = self.yVel * self.yF;
                self.xVel = self.xVel * self.bounce;
                if(self.xVel > self.bounceTolerance):
                    pass;
                if(self.br):
                    x = self.br.x - self.targetObject.width / 2;
                    self.touchBlock(self.br);
               
                if(self.bl):
                    x = self.bl.x + self.targetObject.width / 2;
                    self.touchBlock(self.bl);
               
                if(self.xVel < self.thudTresh and self.xVel > -self.thudTresh):
                    self.xVel = 0;
         
        if(self.xVel > self.xMax):
            self.xVel = self.xMax;
         
        if(self.xVel < -self.xMax):
            self.xVel = -self.xMax;
         
        if(self.yVel > self.yMax):
            self.yVel = self.yMax;
         
        if(self.yVel < -self.yMax):
             self.yVel = -self.yMax;
         

    def bounding2(self):
        if(self.yVel < 0):

    def checkArray(self, p1, p2, p3, p4):
        self.guyTL = False;
        self.guyTR = False;
        self.guyBL = False;
        self.guyBR = False;
        self.guyBM = False;
        self.guyTM = False;
        self.guyLM = False;
        self.guyRM = False;
        _loc_5 = self.targetObject.width;
        _loc_6 = self.targetObject.height;
        self.ctlx = p1 - _loc_5 / 2 + 1;
        self.ctly = p2 - _loc_6 + 1;
        self.ctrx = p1 + _loc_5 / 2 - 1;
        self.ctry = p2 - _loc_6 + 1;
        self.cbrx = p1 + _loc_5 / 2 - 1;
        self.cbry = p2 - 1;
        self.cblx = p1 - _loc_5 / 2 + 1;
        self.cbly = p2 - 1;
        self.clmx = p1 - _loc_5 / 2 + 1;
        self.clmy = p2 - _loc_6 / 2 + 1;
        self.ctmx = p1 + 1;
        self.ctmy = p2 - _loc_6 + 1;
        self.crmx = p1 + _loc_5 / 2 - 1;
        self.crmy = p2 - _loc_6 / 2 + 1;
        self.cbmx = p1 + 1;
        self.cbmy = p2 - 1;
        self.cmx = self.ctmx;
        self.cmy = self.clmy;

        _loc_7 = self.curLevel.tArr[math.floor(self.ctly / self.tileSize)][math.floor(self.ctlx / self.tileSize)];
        _loc_8 = self.curLevel.tArr[math.floor(self.ctry / self.tileSize)][math.floor(self.ctrx / self.tileSize)];
        _loc_9 = self.curLevel.tArr[math.floor(self.cbry / self.tileSize)][math.floor(self.cbrx / self.tileSize)];
        _loc_10 = self.curLevel.tArr[math.floor(self.cbly / self.tileSize)][math.floor(self.cblx / self.tileSize)];
        _loc_11 = self.curLevel.tArr[math.floor(self.ctmy / self.tileSize)][math.floor(self.ctmx / self.tileSize)];
        _loc_12 = self.curLevel.tArr[math.floor(self.clmy / self.tileSize)][math.floor(self.clmx / self.tileSize)];
        _loc_13 = self.curLevel.tArr[math.floor(self.cbmy / self.tileSize)][math.floor(self.cbmx / self.tileSize)];
        _loc_14 = self.curLevel.tArr[math.floor(self.crmy / self.tileSize)][math.floor(self.crmx / self.tileSize)];
        _loc_15 = self.curLevel.tArr[math.floor(self.cbly / self.tileSize)][math.floor(self.cbmx / self.tileSize)];


        if(_loc_7 > 0):
            if(_loc_7 == 1):
                self.guyTL = True;
            else:
                self.guyTL = False;
        if(_loc_8 > 0):
            if(_loc_8 == 1):
                self.guyTR = True;
            else:
                self.guyTR = False;
                     
        if(_loc_9 > 0):
            if(_loc_9 == 1):
                self.guyBR = True;
            elif(_loc_9 == 2 and self.yVel > 0):
                self.guyBR = True;
            else:
                self.guyBR = False;
                
        if(_loc_10 > 0):
            if(_loc_10 == 1):
                self.guyBL = True;
            elif(_loc_10 == 2 and self.yVel > 0):
                self.guyBL = True;
            else:
                self.guyBL = False;
                
        if(_loc_11 > 0):
            if(_loc_11 == 1):
                self.guyTM = True;
            else:
                self.guyTM = False;
                
        if(_loc_13 > 0):
            if(_loc_13 == 1):
                self.guyBM = True;
            else:
                self.guyBM = False;
                
        if(_loc_12 > 0):
            if(_loc_12 == 1):
                self.guyLM = True;
            else:
                self.guyLM = False;
                
        if(_loc_14 > 0):
            if(_loc_14 == 1):
                self.guyRM = True;
            else:
                self.guyRM = False;
                
        if(self.yGrav > 0):
            if(self.guyBM or self.guyBL or self.guyBR):
                self.yLove = 0;
                self.holdCounter = 0;
            if(self.playerSize == 0):
               if(self.guyBM and self.guyBL or self.guyBM and self.guyBR):
                   self.jumpLevel = True;
                   
            if(self.playerSize == 1):
               if(self.guyBR and self.guyBL):
                   self.jumpLevel = True;
                   
        else:
            if(self.guyTM or self.guyTL or self.guyTR):
                self.yLove = 0;
                self.holdCounter = 0;
            if(self.guyTM and self.guyTL or self.guyTM and self.guyTR):
                self.jumpLevel = True;
        if(p3>=0 and p3 <=3):
            
            if(p3==0):
                if(self.guyTL or self.guyTR):
                    return False;
                
            if(p3==1):
                if(self.guyBR or self.guyBL):
                    return False;
                
            if(p3==2):
                if(self.guyTR or self.guyBR):
                    return False;
            if(p3==3):
                if(self.guyTL or self.guyBL):
                    return False;

        else:
            if(self.guyTL or self.guyBL):
                return False;
            
        return True;

    def normalHorizontal(self):
      
        self.xVel = self.xVel + self.xGrav;
        if(self.xGrav > 0):
            if(self.xLove == 1):
                if(not self.holdUp):
                    self.xVel = self.xVel + 1;
               
                if(self.xVel >= 0):
                    self.xLove = 2;
                    self.xVel = 0;
               
            if(self.xLove == 2 or self.xLove == 3):
                if(self.xVel > 0):
                    self.xLove = 3;
            
            if(self.xLove == 3 and self.xLove == 0 and not self.holdUp):
               self.xLove = 0;
               self.holdCounter = 0;
            
            if(self.xLove == 0 and self.xVel > 1.5):
               self.xVel = 3;
            
            if(self.xLove == 0):
               self.playerJump = False;
         
        else:
            if(self.xLove == 1):
                if(not self.holdUp):
                    self.xVel = self.xVel - 1;
                if(self.yVel <= 0):
                    self.xLove = 2;
                    self.xVel = 0;
            if(self.xLove == 2 or self.xLove == 3):
                if(self.xVel < 0):
                    self.xLove = 3;
            if(self.xLove == 3 and self.xVel == 0 and not self.holdUp):            
                self.xLove = 0;
                self.holdCounter = 0;
            if(self.xLove == 0 and self.yVel < 1.5):
                self.xLove = 3;
            if(self.xLove == 0):
                self.playerJump = False;
      
      
    def updateTileInteraction(self):
        self.lastX = x;
        self.lastY = y;
        self.normalVertical();
        if(self.curLevel.arrayMode):
         
             self.bounding2();
         
         else
         
             self.bounding();
         
         if(self.typeOf == "egg")
         
             y = math.floor(y);
         
         if(self.typeOf == "deadaphant")
         
             y = math.floor(y);
         
      
      
    def normalVertical(self):
        self.yVel = self.yVel + self.yGrav;
        if(self.yGrav > 0):
            if(self.yLove == 1):
                if(!self.holdUp):
                    self.yVel = self.yVel + 1;
                if(self.yVel >= 0):
                    self.yLove = 2;
                    self.yVel = 0;
                      
            if(self.yLove == 2 or self.yLove == 3):
                if(self.yVel > 0):
                    self.yLove = 3;
            
            if(self.yLove == 3 and self.yVel == 0 and !self.holdUp):
                self.yLove = 0;
                self.holdCounter = 0;
            
            if(self.yLove == 0 and self.yVel > 1.5):
                self.yLove = 3;
            
            if(self.yLove == 0):
                self.playerJump = false;
            
        else:
            if(self.yLove == 1):
                if(!self.holdUp):
                    self.yVel = self.yVel - 1;
               
                if(self.yVel <= 0):
                    self.yLove = 2;
                    self.yVel = 0;

            if(self.yLove == 2 or self.yLove == 3):
                if(self.yVel < 0):
                    self.yLove = 3;
            
            if(self.yLove == 3 and self.yVel == 0 and !self.holdUp):
                self.yLove = 0;
                self.holdCounter = 0;
            
            if(self.yLove == 0 and self.yVel < 1.5):
                self.yLove = 3;
            
            if(self.yLove == 0):
                self.playerJump = false;
            
        if(self.yLove != 0)
            self.jumpLevel = false;
         
      
      
    def touchBlock(self, p1):
        pass
      
    def bounding(self):
        _loc_1 = 1;
        if(self.yVel < 0):
            if(self.checkTile(x,y + self.yVel,0,self.curLevel)):
                y = y + self.yVel;
                if(self.yGrav < 0):
                    y = math.ceil(y);
            else:
                self.xVel = self.xVel * self.xF;
                self.yVel = self.yVel * self.bounce;
                self.rotSpeed = self.rotSpeed * -1;
                if(self.tr):   
                    y = self.tr.y + self.tileSize + self.targetObject.height;
                    self.hitBlock(self.tr);
                    self.touchBlock(self.tr);
                   
                elif(self.tl):
                    y = self.tl.y + self.tileSize + self.targetObject.height;
                    self.hitBlock(self.tl);
                    self.touchBlock(self.tl);

                if(self.yVel < self.thudTresh and self.yVel > -self.thudTresh):
                    self.yVel = 0;
                   
                if(self.yGrav < 0):
                    self.jumping = false;
                   
            
         
        elif(self.yVel > 0):
            if(self.checkTile(x,y + self.yVel,1,self.curLevel)):
                y = y + self.yVel;
            else:
#                if(self.yVel <= self.bounceTolerance):
               
#                   if(self.yVel > self.bounceTolerance):
                self.xVel = self.xVel * self.xF;
                self.yVel = self.yVel * self.bounce;
                if(self.yGrav > 0):
                    self.jumping = false;
                  
                if(self.bl):
                    y = self.bl.y;
                    self.touchBlock(self.bl);
                  
                elif(self.br):
                    y = self.br.y;
                    self.touchBlock(self.br);
                  
                elif(self.bm):
                    y = self.bm.y;
                    self.touchBlock(self.bm);
                  
                if(self.yVel < self.thudTresh and self.yVel > -self.thudTresh):
                    self.yVel = 0;
                  
                if(math.abs(self.yVel) > 6):
                    self.rotSpeed = self.rotSpeed * (math2.random(8) - 4);
                else:
                  self.rotSpeed = self.rotSpeed * 0.5;
                  
        if(self.xVel < 0):
            if(self.checkTile(x + self.xVel + self.modX,y,3,self.curLevel)):
                x = x + (self.xVel + self.modX);
            else:
                self.yVel = self.yVel * self.yF;
                self.xVel = self.xVel * self.bounce;
                #                if(self.xVel < self.bounceTolerance):               
                if(self.bl):
                    x = self.bl.x + self.targetObject.width / 2 + self.tileSize;
                    self.touchBlock(self.bl);
                    
                elif(self.br):
                    x = self.br.x - self.targetObject.width / 2 + self.tileSize;
                    self.touchBlock(self.br);
                  
                if(self.xVel < self.thudTresh and self.xVel > -self.thudTresh):
                    self.xVel = 0;
        elif(self.xVel > 0):
            if(self.checkTile(x + self.xVel + self.modX,y,2,self.curLevel)):
                x = x + (self.xVel + self.modX);
               
            else:
                self.yVel = self.yVel * self.yF;
                self.xVel = self.xVel * self.bounce;
               #               if(self.xVel > self.bounceTolerance):
               
               
               if(self.br):  
                   x = self.br.x - self.targetObject.width / 2;
                   self.touchBlock(self.br);
               elif(self.bl):
                   x = self.bl.x + self.targetObject.width / 2;
                   self.touchBlock(self.bl);
                if(self.xVel < self.thudTresh and self.xVel > -self.thudTresh):
                    self.xVel = 0;
                  
        if(self.xVel > self.xMax):
            self.xVel = self.xMax;
        if(self.xVel < -self.xMax):
            self.xVel = -self.xMax;
        if(self.yVel > self.yMax):
            self.yVel = self.yMax;
        if(self.yVel < -self.yMax):
            self.yVel = -self.yMax;

    def hitBlock(self, p1):
        pass

    def pAss(self, p1):
        pass
            
    def init(self, level):
        self.curLevel = level
        self.lastX = x;
        self.lastY = y;


               

    def checkTile(self, param1, param2, param3, param4):
        var _loc_7:* = null;
        self.guyTL = False;
        self.guyTR = False;
        self.guyBL = False;
        self.guyBR = False;
        self.guyBM = False;
        self.guyTM = False;
        self.guyLM = False;
        self.guyRM = False;
        _loc_5 = self.targetObject.width;
        _loc_6 = self.targetObject.height;
        self.ctlx = param1 - _loc_5 / 2 + 1;
        self.ctly = param2 - _loc_6 + 1;
        self.ctrx = param1 + _loc_5 / 2 - 1;
        self.ctry = param2 - _loc_6 + 1;
        self.cbrx = param1 + _loc_5 / 2 - 1;
        self.cbry = param2 - 1;
        self.cblx = param1 - _loc_5 / 2 + 1;
        self.cbly = param2 - 1;
        self.clmx = param1 - _loc_5 / 2 + 1;
        self.clmy = param2 - _loc_6 / 2 + 1;
        self.ctmx = param1 + 1;
        self.ctmy = param2 - _loc_6 + 1;
        self.crmx = param1 + _loc_5 / 2 - 1;
        self.crmy = param2 - _loc_6 / 2 + 1;
        self.cbmx = param1 + 1;
        self.cbmy = param2 - 1;
        self.cmx = self.ctmx;
        self.cmy = self.clmy;
        self.tl = self.curLevel.getChildByName("tile" + math.floor(self.ctlx / self.tileSize) + "x" + math.floor(self.ctly / self.tileSize)) as MovieClip;
        self.tr = self.curLevel.getChildByName("tile" + math.floor(self.ctrx / self.tileSize) + "x" + math.floor(self.ctry / self.tileSize)) as MovieClip;
        self.br = self.curLevel.getChildByName("tile" + math.floor(self.cbrx / self.tileSize) + "x" + math.floor(self.cbry / self.tileSize)) as MovieClip;
        self.bl = self.curLevel.getChildByName("tile" + math.floor(self.cblx / self.tileSize) + "x" + math.floor(self.cbly / self.tileSize)) as MovieClip;
        self.tm = self.curLevel.getChildByName("tile" + math.floor(self.ctmx / self.tileSize) + "x" + math.floor(self.ctmy / self.tileSize)) as MovieClip;
        self.lm = self.curLevel.getChildByName("tile" + math.floor(self.clmx / self.tileSize) + "x" + math.floor(self.clmy / self.tileSize)) as MovieClip;
        self.bm = self.curLevel.getChildByName("tile" + math.floor(self.cbmx / self.tileSize) + "x" + math.floor(self.cbmy / self.tileSize)) as MovieClip;
        self.rm = self.curLevel.getChildByName("tile" + math.floor(self.crmx / self.tileSize) + "x" + math.floor(self.crmy / self.tileSize)) as MovieClip;
        self.mb = self.curLevel.getChildByName("tile" + math.floor(self.cbmx / self.tileSize) + "x" + math.floor(self.cbly / self.tileSize)) as MovieClip;
        if(self.tl):
            if(self.tl.type == 1):
                self.guyTL = True;
                _loc_7 = self.tl;
                self.pass(self.tl);
            else:
                self.guyTL = False;
        if(self.tr):
            if(self.tr.type == 1):
                self.guyTR = True;
                _loc_7 = self.tr;
                self.pass(self.tr);
            else:
                self.guyTR = False;
        if(self.br):
            if(self.br.type == 1):
                self.guyBR = True;
                _loc_7 = self.br;
                self.pass(self.br);
            elif(self.br.type == 2 and self.yVel > 0):
                self.guyBR = True;
                _loc_7 = self.br;
            else:
                self.guyBR = False;
        if(self.bl):
            if(self.bl.type == 1):
                self.guyBL = True;
                _loc_7 = self.bl;
                self.pass(self.bl);
            elif(self.bl.type == 2 and self.yVel > 0):
                self.guyBL = True;
                _loc_7 = self.bl;
            else:
                self.guyBL = False;
        if(self.tm):
            if(self.tm.type == 1):
                self.guyTM = True;
                _loc_7 = self.tm;
                self.pass(self.tm);
            else:
                self.guyTM = False;
        if(self.bm):
            if(self.bm.type == 1):
                self.guyBM = True;
                _loc_7 = self.bm;
                self.pass(self.bm);
            else:
                self.guyBM = False;
        if(self.lm):
            if(self.lm.type == 1):
                self.guyLM = True;
                _loc_7 = self.lm;
                self.pass(self.lm);
            else:
                self.guyLM = False;
        if(self.rm):
            if(self.rm.type == 1):
                self.guyRM = True;
                _loc_7 = self.rm;
                self.pass(self.rm);
            else:
                self.guyRM = False;
        if(self.yGrav > 0):
            if(self.guyBM or self.guyBL or self.guyBR):
                self.yLove = 0;
                self.holdCounter = 0;
            if(self.playerSize == 0):
                if(self.guyBM and self.guyBL or self.guyBM and self.guyBR):
                    self.jumpLevel = True;
                if(self.guyBL and not self.guyTL):
                    self.jumpLevel = True;
                if(self.guyBR and not self.guyTR):
                    self.jumpLevel = True;
            if(self.playerSize == 1):
                if(self.guyBR and self.guyBL):
                    self.jumpLevel = True;
                if(self.guyBL and not self.guyTL):
                    self.jumpLevel = True;
                if(self.guyBR and not self.guyTR):
                    self.jumpLevel = True;
        else:
            if(self.guyTM or self.guyTL or self.guyTR):
                self.yLove = 0;
                self.holdCounter = 0;
            if(self.guyTM and self.guyTL or self.guyTM and self.guyTR):
                self.jumpLevel = True;
        if(param3>=0 and param3<=3):
            if(param3==0):
                if(self.guyTL or self.guyTR):
                    return False;
            if(param3==1):
                if(self.guyBR or self.guyBL):
                    return False;
            if(param3==2):
                if(self.guyTR or self.guyBR):
                    return False;
            if(param3==3):
                if(self.guyTL or self.guyBL):
                    return False;
        else:
            if(self.guyTL or self.guyBL):
                return False;
        return True;
        
