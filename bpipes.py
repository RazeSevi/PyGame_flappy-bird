import pygame
from pygame.locals import *
from pygame.surface import Surface
import random

pipe_gap=170

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/pipe.png')
        self.rect = self.image.get_rect()
        self.speed = speed
        self.initial_x = x
        self.x = x
        self.y = y
        self.position = position

        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x, self.y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, self.y + int(pipe_gap / 2)]

    def update_position(self, x_position):
        self.x = x_position
        if self.position == 1:
            self.rect.bottomleft = [self.x, self.y - int(pipe_gap / 2)]
        if self.position == -1:
            self.rect.topleft = [self.x, self.y + int(pipe_gap / 2)]

    def collides(self, bird):
        return pygame.Rect.colliderect(bird.rect, self.rect)

    def reset(self, y):
        self.x = self.initial_x
        self.y  = y
        if self.position == 1:
            self.rect.bottomleft = [self.x, self.y - int(pipe_gap / 2)]
        if self.position == -1:
            self.rect.topleft = [self.x, self.y + int(pipe_gap / 2)]

class PipePair:
    def __init__(self, x, screen_height, speed, screen_width):
        self.x = x
        self.screen_height = screen_height
        self.speed = speed
        self.gainedPoint = False
        self.margin = 200
        self.y = random.randrange(self.margin, self.screen_height - self.margin)
        self.bottom = Pipe(x, self.y, -1, speed)
        self.top = Pipe(x, self.y, 1, speed)
        self.pipe_group = pygame.sprite.Group()
        self.pipe_group.add(self.bottom)
        self.pipe_group.add(self.top)
        self.ground_scroll = x
        self.screen_width = screen_width

    def collides(self, bird):
        if self.bottom.collides(bird):
            return True
        if self.top.collides(bird):
            return True
        return False

    def draw(self, screen):
        self.ground_scroll -= self.speed
        point = 0
        if self.ground_scroll < -100:
            self.ground_scroll = self.screen_width
            self.y = random.randrange(self.margin, self.screen_height - self.margin)
            self.top.reset(self.y)
            self.bottom.reset(self.y)
            self.gainedPoint = False
        if self.ground_scroll < 100 and not self.gainedPoint:
            self.gainedPoint = True
            point = 1
            
        self.bottom.update_position(self.ground_scroll)
        self.top.update_position(self.ground_scroll)
        self.pipe_group.draw(screen)
        self.pipe_group.update()
        return point

    def reset(self):
        self.y = random.randrange(self.margin, self.screen_height - self.margin)
        self.top.reset(self.y)
        self.bottom.reset(self.y)
        self.ground_scroll = self.top.initial_x
        self.gainedPoint = False
