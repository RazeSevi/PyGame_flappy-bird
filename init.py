import pygame
import pygame_gui
from pygame.locals import *
import background as bg
import ground as g
import bird as b
import bpipes as p
import counter as c
import sounds.sounds as s
import sys
import os

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)


pygame.init()
pygame.mixer.init()

#for button
manager = pygame_gui.UIManager((800, 600))
#crash_sound = pygame.mixer.Sound("crash.wav")
clock = pygame.time.Clock()

#game variables
fps = 60
screen_width =  864
screen_height = 936
game_over = True
speed = 4
borderDistance = 100
GameCount = 0


#set width and height
screen = pygame.display.set_mode((screen_width, screen_height))
#Title
pygame.display.set_caption('Flappy Bird')
#shows start and stop button
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350,420),(120,80)), text='Start game', manager=manager)
stop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350,520),(120,80)), text='Stop game', manager=manager)
#Bird groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
#Objects
background = bg.Background(screen, screen_width, speed)
ground = g.Ground(screen, screen_width, speed)
flappy = b.Bird(borderDistance, int(screen_height / 2), fps, screen_height, .5)
counter = c.Counter(screen)
sounds = s.Sound()

bird_group.add(flappy)
#pipe list
pipes = [
    p.PipePair(650, 768, speed, screen_width),
    p.PipePair(950, 768, speed, screen_width),
    p.PipePair(1250, 768, speed, screen_width),
]
game_over_delay = .8
__game_over_delay_max_count = fps * game_over_delay
__game_over_delay_count = __game_over_delay_max_count 
#Game loop
run = True
while run:
    if __game_over_delay_count < __game_over_delay_max_count:
        __game_over_delay_count += 1

    time_delta = clock.tick(fps)/1000.0
    #draw background
    background.draw()
    
    if not game_over:
        flappy.update()
        for pipe in pipes:
            if pipe.draw(screen) == 1:
                counter.increment()
                sounds.Point()

    bird_group.draw(screen)
    counter.draw()
    ground.draw()

    if flappy.collides(pipes):
        game_over = True
        __game_over_delay_count = 0
        flappy.reset()
        sounds.Crash()
        for pipe in pipes:
            pipe.reset()
        bird_group.draw(screen)

    if flappy.rect.bottom > 768:
        game_over = True
        flappy.reset()
        sounds.Crash()
        __game_over_delay_count = 0

        for pipe in pipes:
            pipe.reset()
        bird_group.draw(screen)
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    GameCount += 1
                    print(f'Game {GameCount}: Started')
                    counter.reset()
                    __game_over_delay_count = __game_over_delay_max_count
                    game_over = False
                if event.ui_element == stop_button:
                    run = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over == True:
                    GameCount += 1
                    print(f'Game {GameCount}: Started')
                    counter.reset()
                if __game_over_delay_count >= __game_over_delay_max_count:
                    sounds.Pop()                 
                    flappy.jump()                 
                    game_over = False
        manager.process_events(event)
    manager.update(time_delta)
    if game_over:
        manager.draw_ui(screen)
    pygame.display.update()
pygame.quit()


