# template https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
# import socket programming library 
import socket
import pickle
import time
import threading
  
# import thread module 
from _thread import *
import threading 
from datetime import datetime

lock = threading.Lock()
lockLc = threading.Lock()

HEADERSIZE = 16
# data to keep on the server
playerPositions = {}
levelCode = "2,0,0;1,25,25"
hLvl = hash(levelCode)
msgBuf = {}

# thread function 
def threaded(c):
    full_msg = b''
    new_msg = True

    while True: 
        # data received from client
        
        msg = c.recv(16)
        if(len(msg) == 0):
            return
        if new_msg:
            #print(msg)
            #print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        #print(f"full message length: {msglen}")

        full_msg += c.recv(msglen)

        #print(len(full_msg))

        if len(full_msg) == msglen:
            #print("full msg recvd")
            #print(full_msg)
            #print(pickle.loads(full_msg))
            ans = processRequest(pickle.loads(full_msg))
            if(ans):
                msg = pickle.dumps(ans)
                msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
                print("send: "+str(msg))
                c.send(msg)
        new_msg = True
        full_msg = b""
    # connection closed 
    c.close() 
  
def processRequest(msg):
    global levelCode
    global hLvl
    ans = {}
    print(msg)
    if(msg["ID"] == None):
        return None
    if(not (msg["ID"] in msgBuf)):
        msgBuf[msg["ID"]] = []
    if(msg["REQ"] == "NWLVL"):
        lockLc.acquire()
        levelCode = msg["DATA"]
        lockLc.release()
        hLvl = hash(levelCode)
    if(msg["REQ"] == "LVL"):
        lockLc.acquire()
        ans["LVL"] = levelCode
        lockLc.release()
        ans["HSHLVL"]= hLvl
    if(msg["REQ"] == "CHT"):
        for p in msgBuf:
            msgBuf[p].append(msg["DATA"])
    if(msg["REQ"] == "POS"):
        lock.acquire()
        try:
            playerPositions[msg["ID"]] = (msg["DATA"],datetime.now())
        finally:
            lock.release()

        #print("updated position")
    if(msg["REQ"] == "UPDPOS"):
        ans["UPDPOS"] = playerPositions

        #print("send position:"+str(playerPositions))
        ans["HSHLVL"]= hLvl
        ans["CHT"] = msgBuf[msg["ID"]]
        msgBuf[msg['ID']] = []
    #print(ans)
    return ans

def refresh_pos():
    while True:
        toRemove = []

        print("cleaning old pos")
        d = datetime.now()
        for p in playerPositions:
            print((d-playerPositions[p][1]).total_seconds())
            if((d-playerPositions[p][1]).total_seconds()  > 120):
                toRemove.append(p)
                print("p pos removed")      
        lock.acquire()
        try:
            for p in toRemove: 
                del playerPositions[p]
        finally:
            lock.release()
        time.sleep(60)
                           
def Main(): 
    start_new_thread(refresh_pos, ())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((socket.gethostname(), 13337))
  
    # put the socket into listening mode 
    s.listen() 
    print("EPyth Server Started")
  
    while True: 
        # establish connection with client 
        c, addr = s.accept() 
  
        print('Connected to :', addr[0], ':', addr[1]) 
  
        start_new_thread(threaded, (c,)) 
    s.close() 
    
if __name__ == '__main__': 
    Main() 
