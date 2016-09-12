import graphicsBackend
import game

#The number of frames until another attack
attackDelay = 0

def getPlayer():
  for currentObject in graphicsBackend.entities:
    if currentObject.name == "player":
      playerObject = currentObject

def attack():
  if attackDelay > 0:
    attackDelay -= 1
##  elif:
##    print("nah")
