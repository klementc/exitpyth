# Import the pygame module
import pygame
from player import Player
import pygame_textinput

from globals import *
import camera

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

player = Player()
#print("limits: "+str(player.curLevel.maxWidth)+" "+str(player.curLevel.maxHeight))
#cam = camera.Camera(camera.complex_camera, player.curLevel.maxWidth, player.curLevel.maxHeight)
cam = camera.Camera(camera.simple_camera, player.curLevel.maxWidth, player.curLevel.maxHeight)
textInputting = False
textinput = pygame_textinput.TextInput()
textinput.text_color = (0,255,0)
textinput.set_cursor_color((255,255,255))

# Main loop
while running:
    # Look at every event in the queue
    events = pygame.event.get()

    if(textInputting):
        print("textinputting")
        textinput.update(events)

    for event in events:
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_a:
                player.init_level(LEVEL1)
            if event.key == K_z:
                player.init_level(LEVEL2)
            if(event.key == K_RETURN and textInputting==True):
                print("clooooooooooooooooo")
                print(textinput.get_text())
                textinput.clear_text()
                textInputting = False
            if(event.key == K_t and textInputting==False):
                print("YYYYYYYYYYYYYYYYYYYy")
                textInputting = True
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
    screen.blit(player.image, cam.apply(player))

    if(textInputting):
        screen.blit(textinput.get_surface(), (10, 10))
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
