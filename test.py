# file for testing code. not used in the game.

import pygame

pygame.init()
# The dimentions of the game window
windowWidth = 800
windowHeight = 600
# Initialize the game window
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("RPG Game")

image = pygame.image.load("graphics/player/stand/0.PNG").convert_alpha()
