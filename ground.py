import pygame
from pygame.locals import *
from pygame.surface import Surface

#load image
ground = pygame.image.load('images/ground.png')

class Ground:
    def __init__(self, screen: Surface, screen_width: int, speed: float):
        self.ground_scroll = 0
        self.ground_scroll_2 = screen_width
        self.screen_width = screen_width
        self.screen = screen
        self.speed = speed
    
    def draw(self):
        #draw and scroll the ground
        self.screen.blit(ground, (self.ground_scroll, 768))
        self.screen.blit(ground, (self.ground_scroll_2, 768))

        self.ground_scroll -= self.speed
        self.ground_scroll_2 -= self.speed
        if abs(self.ground_scroll) > self.screen_width:
            self.ground_scroll = self.screen_width
        if abs(self.ground_scroll_2) > self.screen_width:
            self. ground_scroll_2 = self.screen_width