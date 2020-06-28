from globals import *
import pygame

# thanks https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame
class Camera():
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        #print("apply: "+str(target.rect))
        return target.rect.move(self.state.topleft)

    def update(self, target):
        #print("update: "+str(target.rect))
        self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect # l = left,  t = top
    _, _, w, h = camera      # w = width, h = height
    return pygame.Rect(-l+SCREEN_WIDTH/2 , -t+SCREEN_HEIGHT/2 , w, h)