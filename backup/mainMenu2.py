red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#backdrop = "graphics/mainMenu.png"

class objects():
  name = ""
  colour = ""
  x = 0
  y = 0
  width = 0
  height = 0
  clickable = False

  def __init__(self,name,colour,x,y,width,height,clickable):
    self.name = name
    self.colour = colour
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.clickable = clickable

newGame = objects("newGame",red,300,150,200,100,True)
loadGame = objects("loadGame", green, 300, 270, 200, 100,True)
quitGame = objects("quitGame", blue, 300, 390, 200, 50,True)

allObjects = [newGame, loadGame, quitGame]
