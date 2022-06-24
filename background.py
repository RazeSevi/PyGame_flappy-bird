import pygame
from pygame.locals import *
from pygame.surface import Surface

#load image
bg = pygame.image.load('images/bg.png')

class Background:
    def __init__(self, screen: Surface, screen_width: int, speed: float):
        self.ground_scroll = 0
        self.ground_scroll_2 = screen_width
        self.screen_width = screen_width
        self.screen = screen
        self.speed = speed
    
    def draw(self):
        self.screen.blit(bg, (self.ground_scroll, 0))
        self.screen.blit(bg, (self.ground_scroll_2, 0))
        self.ground_scroll -= self.speed
        self.ground_scroll_2 -= self.speed
        if abs(self.ground_scroll) > self.screen_width:
            self.ground_scroll = self.screen_width
        if abs(self.ground_scroll_2) > self.screen_width:
            self. ground_scroll_2 = self.screen_width