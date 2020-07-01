import socket
from globals import *
import pickle
import time
import threading

HEADERSIZE = 16
lock = threading.Lock()

class Client():
  def __init__(self):
    self.lock = threading.Lock()
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
    #print(msg)
    print("ASKING FOR LEVEL")
    lock.acquire()
    try:
      print("AAAAAAA")
      self.s.send(msg)
      print("BBBBBBB")
      msg = self.receiveMsg(self.s)
      print("CCCCCCCC")
    finally:
        lock.release()
    ol["code"] = msg["LVL"]
    ol["HSH"]= msg["HSHLVL"]

    while True:
      pos = (player.rect.x, player.rect.y)
      if(pos != prevPos):
        d = {"REQ":"POS", "ID": player.username, "DATA":pos}
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        print("UPDATING POS WITH SRV")
        lock.acquire()
        try:
          self.s.send(msg)
        finally:
          lock.release()
        
      
      d = {"REQ":"UPDPOS", "ID": player.username}
      msg = pickle.dumps(d)
      msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
      print("POSSSSS"+str(msg))

      lock.acquire()
      try:
        self.s.send(msg)
        mr = self.receiveMsg(self.s)
      finally:
        lock.release()

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
        lock.acquire()
        try:
          self.s.send(msg)
          print("RECEIVING")
          msg = self.receiveMsg(self.s)
          print("RECEIVED")
        finally:
          lock.release()

        print("CHANGE LEVELLLLLLLLLLLLLLLLLL" + str(msg))
        ol["code"] = msg["LVL"]
        ol["HSH"]= msg["HSHLVL"]

      time.sleep(0.5)

  def setLevel(self, newCode, player):
    d = {"REQ":"NWLVL", "ID": player.username, "DATA":newCode}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    lock.acquire()
    try:
      self.s.send(msg)
    finally:
      lock.release()

  def sendChat(self, msg, player):
    d = {"REQ":"CHT", "ID": player.username, "DATA":msg}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    lock.acquire()
    try:
      self.s.send(msg)
    finally:
      lock.release()
    


  def receiveMsg(self, s):
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
      while(len(full_msg) != msglen):
        print("RCVNGGGGG")
        full_msg+=s.recv(msglen - len(full_msg))
      print(full_msg)

      print(pickle.loads(full_msg))
      return pickle.loads(full_msg)

      print("len prob "+str(msglen)+"/"+str(len(full_msg)))
  def stop(self):
    exit()