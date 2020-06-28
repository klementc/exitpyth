# Import the pygame module
import pygame
from player import Player

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
print("limits: "+str(player.curLevel.maxWidth)+" "+str(player.curLevel.maxHeight))
#cam = camera.Camera(camera.complex_camera, player.curLevel.maxWidth, player.curLevel.maxHeight)
cam = camera.Camera(camera.simple_camera, player.curLevel.maxWidth, player.curLevel.maxHeight)

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.ping(pressed_keys)

    screen.fill((0, 0, 0))
    print("maxWH: "+str(player.curLevel.maxWidth)+" "+str(player.curLevel.maxHeight))
    #screen.blit(player.curLevel.image, (0,0))#SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    #screen.blit(player.surf, player.rect )#(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    cam.update(player)
    for e in player.curLevel.tiles:
        #print("tile x:"+str(e.x) )
        screen.blit(e.surf, cam.apply(e))
    screen.blit(player.image, cam.apply(player))

    #pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
