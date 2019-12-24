import random
import pygame
import sys
from pygame.locals import *

#Globla variables for the pygame
FPS = 32
SCREENWIDTH     = 289
SCREENHEIGHT    = 511
SCREEN          = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY         = SCREENHEIGHT * 0.8
GAME_SPRITES    = {}
GAME_SOUNDS     = {}
PLAYER          = 'images/bird.png'
BACKGROUND      = 'images/game_background.jpg'
PIPE            = 'images/pipe.png'


def welcomeScreen():
    '''
    Shows welcome images on the SCREEN
    '''
    playerx = 


if __name__ == '__main__':

    # Initialize all pygame modules
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    )

    GAME_SPRITES['message'] = pygame.image.load('images/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('images/message.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        mainGame() # This is the main game function
