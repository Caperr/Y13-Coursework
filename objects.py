import pygame
pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

font = pygame.font.SysFont(None,25)

class objects():
  objectType = ""
  name = ""
  x = 0
  y = 0
  clickable = False
  toRender = True

  def init(self,objectType,name,x,y,clickable,toRender):
    self.objectType = objectType
    self.name = name
    self.x = x
    self.y = y
    self.clickable = clickable
    self.toRender = toRender

##  def __init__(self,objectType,name,x,y,clickable,toRender):
##    self.init(objectType,name,x,y,clickable,toRender)

class rectangle(objects):
  width = 0
  height = 0
  colour = ""

  def __init__(self,objectType,name,x,y,clickable,toRender, width,height,colour):
    self.init(objectType,name,x,y,clickable,toRender)
    self.width = width
    self.height = height
    self.colour = colour

class text(objects):
  text = ""
  colour = ""
  antialiasing = True

  def __init__(self,objectType,name,x,y,clickable,toRender, text,colour,antialiasing):
    self.init(objectType,name,x,y,clickable,toRender)
    self.text = text
    self.colour = colour
    self.antialiasing = antialiasing

  def centreText(self,centre):
    textSize = font.size(self.text)
    self.x = centre[0] - round(textSize[0]/2)
    self.y = centre[1] - round(textSize[1]/2)

class image(objects):
  file = ""

  def __init__(self,objectType,name,x,y,clickable,toRender, file):
    self.init(objectType,name,x,y,clickable,toRender)
    self.file = file

class animation(objects):
  folder = ""
  current = 0
  state = 1
  totalStates = 0

  def __init__(self,objectType,name,x,y,clickable,toRender, folder,images,state):
    self.init(objectType,name,x,y,clickable,toRender)
    self.folder = folder
    self.state = state

class entity(objects):
  #list of states and how many images each state has
  states = [["stand",3],["walk",5]]
  #the entities folder. contains all of it's graphics
  folder = ""
  #Player specific - should the player walk after landing a jump?
  jumpWalk = [False,"r"]
  #current image to render
  current = 0
  #total number of states in the folder
  totalStates = 3
  #current state folder to load from
  state = "stand"
  #previous active state
  previous = []
  #current entity orientation
  face = "r"
  #The distance left to knock back after an attack on the entity
  knockbackDistance = 0
  #The starting knockback distance
  knockbackDistanceMax = 0
  #The direction to knock back
  knockbackFace = "l"

  def __init__(self,objectType,name,x,y,clickable,toRender, states,state,folder,face):
    self.init(objectType,name,x,y,clickable,toRender)
    self.states = states
    self.state = state
    self.folder = folder
    self.face = face
    self.updateVars()

  def changeState(self,new):
    oldHeight = pygame.image.load("graphics/" + self.folder + "/" + self.state + "/" + str(self.current) + ".PNG").get_height()
    newHeight = pygame.image.load("graphics/" + self.folder + "/" + new + "/0.PNG").get_height()
    if newHeight < oldHeight:
      self.y += oldHeight - newHeight
    self.previous.append(self.state)
    if len(self.previous) > 2:
      self.previous.pop(0)
    self.state = new
    self.updateVars()

  def updateVars(self):
    for i in range(len(self.states)):
      if self.states[i][0] == self.state:
        self.current = 0
        self.totalStates = self.states[i][1]
