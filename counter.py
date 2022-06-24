import pygame
from pygame.locals import *
pygame.font.init()
import sounds.sounds as s

class Counter():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 120)
        self.scoreFont = pygame.font.Font("VarelaRound-Regular.ttf", 50)
        self.color = pygame.Color('white')
        self.count = 0
        self.temp = -1
        self.sounds = s.Sound()
        

    def reset(self):
        highScore = self.font.render(str(''), True, False)
        self.screen.blit(highScore, (400, 100))
        if self.count > self.temp:
            self.temp = self.count
        self.count = 0    

      
    def increment(self):
        self.count += 1
        if self.count == self.temp:
            self.sounds.NewScore()
            
    
    def draw(self):
        txt_surface = self.font.render(str(self.count), True, self.color)
        self.screen.blit(txt_surface, (385, 100))
        if self.count > self.temp:
            highScore = self.scoreFont.render(str('High Score'), True, self.color)
            self.screen.blit(highScore, (285, 20))