# Import the pygame module
import pygame
from player import Player

from globals import *

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

player = Player()


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
    screen.blit(player.curLevel.image, (0,0))#SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(player.surf, player.rect )#(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    pygame.display.flip()
    clock.tick(30)
