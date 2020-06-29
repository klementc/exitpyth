# Import the pygame module
import pygame
from player import Player
import pygame_textinput
import time

from globals import *
import camera

def message_box(text, f):
    pos = 50 # depends on message box location
    screen.blit(f.render("<tab> to hide/show chat", 0, (200,200,200)), ( 0, 27))
    for x in range(len(text)):
        rendered = f.render(text[x], 0, (255,255,255))
        screen.blit(rendered, ( 0, pos))
        pos += 20 # moves the following line down 30 pixels


# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
t0 = time.time()

# Variable to keep the main loop running
running = True

player = Player()
#print("limits: "+str(player.curLevel.maxWidth)+" "+str(player.curLevel.maxHeight))
#cam = camera.Camera(camera.complex_camera, player.curLevel.maxWidth, player.curLevel.maxHeight)
cam = camera.Camera(camera.simple_camera, player.curLevel.maxWidth, player.curLevel.maxHeight)
showInput = False
textinput = pygame_textinput.TextInput()
textinput.text_color = (0,255,0)
textinput.set_cursor_color((255,255,255))

showChat = True

msgBuffer = ["!say <message> to speak","!set <code> to set level"]

# Main loop
while running:
    # Look at every event in the queue
    events = pygame.event.get()
    for event in events:
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_a:
                t0 = time.time()
                player.init_level(LEVEL1)
            if event.key == K_TAB:
                showChat = not showChat
            if event.key == K_z:
                t0 = time.time()
                player.init_level(LEVEL2)
            if(event.key == K_RETURN and showInput):
                t0 = time.time()
                #print(textinput.get_text())
                if(not " " in textinput.get_text()):
                    continue
                c, v = textinput.get_text().split(" ",1)
                if(c == "!set"):
                    player.init_level(v)
                elif(c=="!say"):
                    msgBuffer.append(player.username+": "+v)
                    if(len(msgBuffer)>7):
                        msgBuffer=msgBuffer[1:]
                showInput = False
                textinput.clear_text()
            if(event.key == K_t):
                showInput = True
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.ping(pressed_keys)

    screen.fill((0, 0, 0))
    #print("maxWH: "+str(player.curLevel.maxWidth)+" "+str(player.curLevel.maxHeight))
    #screen.blit(player.curLevel.image, (0,0))#SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    #screen.blit(player.surf, player.rect )#(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    cam.update(player)
    for e in player.curLevel.tiles:
        #print("tile x:"+str(e.x) )
        screen.blit(e.surf, cam.apply(e))
    for e in player.curLevel.halfTiles:
        #print("tile x:"+str(e.x) )
        screen.blit(e.surf, cam.apply(e))
    for e in player.curLevel.checkPoints:
        #print("tile x:"+str(e.x) )
        screen.blit(e.surf, cam.apply(e))
    screen.blit(player.image, cam.apply(player))

    if(showInput):
        print("textinputting")
        textinput.update(events)
        screen.blit(textinput.get_surface(), (10, 10))
    #pygame.display.flip()

    myfont = pygame.font.SysFont('Arial', 18)
    textsurface = myfont.render(str(round(time.time()-t0,3)), False, (185, 185, 34))
    screen.blit(textsurface,(SCREEN_WIDTH/2,0))

    if(showChat):
        message_box(msgBuffer,myfont)

    pygame.display.update()
    clock.tick(30)
