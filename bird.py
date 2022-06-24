import pygame
from pygame.locals import *
from pygame.surface import Surface

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, fps, screen_height,animationSpeed = 1):
        pygame.sprite.Sprite.__init__(self)
        self.__images = [
            pygame.image.load('images/bird1.png'),
            pygame.image.load('images/bird2.png'),
            pygame.image.load('images/bird3.png')
        ]
        
        self.initial_x = x
        self.initial_y = y
        self.__index = 0
        self.__counter = 0
        self.__fps = fps
        self.image = self.__images[self.__index]
        self.rect = self.image.get_rect()
        self.screen_height = screen_height
        self.x = x
        self.y = y
        self.vy = 5
        self.rect.center = [x, y]
        self.__imageUpdateCount = (self.__fps / (1 / animationSpeed)) / len(self.__images)

    def jump(self):
         self.vy = -10

    def update(self):
        self.vy += 1
        if self.vy > 25:
            self.vy = 25

        self.y += self.vy
        if self.y > 768:
            self.y = 768

        self.rect.center = [self.x, self.y]
        self.__counter += 1

        if self.__counter >= self.__imageUpdateCount:
            self.__index += 1
            self.__index = self.__index % len(self.__images) - 1
            self.__counter = 0
            self.image = self.__images[self.__index]
        
        self.image = pygame.transform.rotate(self.__images[self.__index], -self.vy * 2 )

    def reset(self):
        self.x = self.initial_x
        self.y  = self.initial_y
        self.rect.center = [self.x, self.y]

    def collides(self, pipes):
        for pipe in pipes:
            if pipe.collides(self):
                return True
        return False


