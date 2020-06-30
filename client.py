import socket
from globals import *
import pickle
import time

HEADERSIZE = 16

class Client():
  def __init__(self):
    pass
  def onlineClient(self, add, ol, player, olP):
    prevPos = (-1,-1)
    print("connect to "+str(add))
    c = (add.split(":")[0], int(add.split(":")[1]))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(c)

    d = {"REQ":"LVL", "ID": player.username}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    s.send(msg)

    msg = self.receiveMsg(s)
    ol["code"] = msg["LVL"]
    
    print("client: "+str(ol))
    while True:
      pos = (player.rect.x, player.rect.y)
      if(pos != prevPos):
        d = {"REQ":"POS", "ID": player.username, "DATA":pos}
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        #print(msg)
        s.send(msg)

      d = {"REQ":"UPDPOS", "ID": "klem"}
      msg = pickle.dumps(d)
      msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
      #print("POSSSSS"+str(msg))
      s.send(msg)
      p = self.receiveMsg(s)["UPDPOS"]
      
      for e in set(olP)-set(p):
        del olP[e]
      for e in p:
        olP[e] = p[e]
      

      time.sleep(0.5)

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


          if len(full_msg) == msglen:
              #print(pickle.loads(full_msg))
              return pickle.loads(full_msg)
  def stop(self):
    exit()