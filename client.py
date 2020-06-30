import socket
from globals import *
import pickle
import time
import threading

HEADERSIZE = 16

class Client():
  def __init__(self):
    pass
  def onlineClient(self, add, ol, player, olP, msgbuf):
    prevPos = (-1,-1)
    print("connect to "+str(add))
    c = (add.split(":")[0], int(add.split(":")[1]))
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.connect(c)

    d = {"REQ":"LVL", "ID": player.username}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    self.s.send(msg)

    msg = self.receiveMsg(self.s)
    ol["code"] = msg["LVL"]
    ol["HSH"]= msg["HSHLVL"]

    while True:
      pos = (player.rect.x, player.rect.y)
      if(pos != prevPos):
        d = {"REQ":"POS", "ID": player.username, "DATA":pos}
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        #print(msg)
        self.s.send(msg)
      
      d = {"REQ":"UPDPOS", "ID": player.username}
      msg = pickle.dumps(d)
      msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
      print("POSSSSS"+str(msg))
      self.s.send(msg)
      mr = self.receiveMsg(self.s)
      for m in range(len(mr["CHT"])):
        msgbuf.append(mr["CHT"][m])
        if(len(msgbuf)>7):
          msgbuf.pop(0)

      p = mr["UPDPOS"]

      for e in set(olP)-set(p):
        del olP[e]
      for e in p:
        olP[e] = p[e]
      
      if(mr["HSHLVL"] and mr["HSHLVL"] != ol["HSH"]):
        print("SERVER LEVEL CHANGED")
        d = {"REQ":"LVL", "ID": player.username}
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        self.s.send(msg)
        msg = self.receiveMsg(self.s)
        print("CHANGE LEVELLLLLLLLLLLLLLLLLL" + str(msg))
        ol["code"] = msg["LVL"]
        ol["HSH"]= msg["HSHLVL"]

      time.sleep(0.5)

  def setLevel(self, newCode, player):
    d = {"REQ":"NWLVL", "ID": player.username, "DATA":newCode}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    self.s.send(msg)

  def sendChat(self, msg, player):
    d = {"REQ":"CHT", "ID": player.username, "DATA":msg}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    self.s.send(msg)


  def receiveMsg(self, s):
    while True:
      full_msg = b''
      new_msg = True
      while True:
          msg = s.recv(16)
          if(len(msg) == 0):
              return
          if new_msg:
              msglen = int(msg[:HEADERSIZE])
              new_msg = False

          #print(f"full message length: {msglen}")

          full_msg += s.recv(msglen)

          print(full_msg)
          if len(full_msg) == msglen:
              print(pickle.loads(full_msg))
              return pickle.loads(full_msg)

  def stop(self):
    exit()