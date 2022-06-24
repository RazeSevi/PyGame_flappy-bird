import pygame
from pygame.locals import *

class Sound():
    def __init__(self):
        pop_path = "sounds/pop_sound.wav"
        point_path = "sounds/point_sound.wav"
        crashed_path = "sounds/crash2.wav"
        #crashed_path = "sounds/crash.wav"
        newScore_path = "sounds/newScore.wav"

        self.soundFilePop = pygame.mixer.Sound(pop_path)
        self.soundFilePoint = pygame.mixer.Sound(point_path)
        self.soundFileCrash = pygame.mixer.Sound(crashed_path)
        self.soundFileNewScore = pygame.mixer.Sound(newScore_path)

    def Pop(self):
        pygame.mixer.Sound.play(self.soundFilePop)
        pygame.mixer.music.stop()
    
    def Point(self):
        pygame.mixer.Sound.play(self.soundFilePoint)
        pygame.mixer.music.stop()

    def Crash(self):
        pygame.mixer.Sound.play(self.soundFileCrash)
        pygame.mixer.music.stop()

    def NewScore(self):
        pygame.mixer.Sound.play(self.soundFileNewScore)
        pygame.mixer.music.stop()
        