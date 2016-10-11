import pygame
from mainMenu import *

pygame.init()

windowWidth = 800
windowHeight = 600

window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("RPG Game")

white = (255,255,255)
red = (255,0,0)

gameClock = pygame.time.Clock()
FPS = 30

font = pygame.font.SysFont(None,25)

currentScreen = "main menu"

def gameLoop():
  gameQuit = False

  while not gameQuit:
    for event in pygame.event.get():
      #print(event)
      if event.type == pygame.QUIT:
        gameQuit = True
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if newGame.x - 1 < event.pos[0] < newGame.x + newGame.width + 1 and newGame.y -1 < event.pos[1] < newGame.y + newGame.height + 1:
            print("click" + newGame.name)

    window.fill(white)
    pygame.draw.rect(window, newGame.colour, [newGame.x,newGame.y,newGame.width,newGame.height])

    pygame.display.update()

    gameClock.tick(FPS)

  pygame.quit()

gameLoop()
