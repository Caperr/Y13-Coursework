import pygame
# import and initialize pygame. this is just to make text, as font is needed
pygame.init()
# initialize colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lblue = (110, 220, 255)
grey = (225, 225, 225)
# initialize window zize
windowWidth = 0
windowHeight = 0
floor = 0
# initialize text
font = pygame.font.SysFont(None, 25)
# set window width and height
def init():
    from temp import width,height,floor
    return width,height,floor
windowWidth, windowHeight, floor = init()

# parent class for all graphical objects
class objects:
    # what type of object it is
    objectType = ""
    # its name
    name = ""
    # its position
    x = 0
    y = 0
    # where it can be clicked on
    clickable = False
    # whether it is visible
    toRender = True

    # set the values of all attributes
    def init(self, objectType, name, x, y, clickable, toRender):
        self.objectType = objectType
        self.name = name
        self.x = x
        self.y = y
        self.clickable = clickable
        self.toRender = toRender

# skeleton init for making new objects
#  def __init__(self,objectType,name,x,y,clickable,toRender):
#    self.init(objectType,name,x,y,clickable,toRender)

# rectangles
class rectangle(objects):
    # dimensions
    width = 0
    height = 0
    # the colour
    colour = ""

    # configure attributes
    def __init__(self, name, x, y, clickable, toRender, width, height, colour):
        self.init("rectangle", name, x, y, clickable, toRender)
        self.width = width
        self.height = height
        self.colour = colour

# entity stamina bars
class staminaBar(objects):
    # width based on the stamina the entity still has
    swidth = 0
    # width based on the stamina the entity has lost
    gwidth = 0
    # the height of the bar
    height = 0
    # the objects to associate with
    entity = ""
    object = ""

    # configure attributes
    def __init__(self, name, entity, object):
        self.init("staminaBar", name, 0, 0, False, True)
        self.entity = entity
        self.object = object
        # if the bar is the player's, make it thicker
        if self.object.name == "player":
            self.height = round(windowHeight/40)
            # Move the bar to the top left of the screen
            self.x = round(windowWidth / 50)
            self.y = self.x + round(windowWidth / 30)
        else:
            self.height = round(windowHeight/60)
        self.update()
    # update position and widths
    def update(self):
        # Update position and bar width
        # The width for the player's bar is much bigger than that of enemy bars.
        if self.object.name == "player":
            # set the player's healthBar's width based on window size
            entityWidth = round(windowWidth * 2 / 5)
        else:
            # move the bar to just above the entity's position
            self.x = self.object.x
            self.y = self.object.y - round(windowHeight / 24) + round(windowHeight / 50)
            # get the width of the entity's default frame
            entityWidth = pygame.image.load("graphics/" + self.object.folder + "/stand/0" + ".PNG").get_width()
        # set the width of the light blue section as a percentage of the max entity stamina and width of the entity
        self.bwidth = self.entity.stamina / self.entity.maxStamina * entityWidth
        # set width of the grey section
        self.gwidth = entityWidth - self.bwidth

# entity health bars
class healthBar(objects):
    # width based on the health the entity still has
    gwidth = 0
    # width based on the health the entity has lost
    rwidth = 0
    # the height of the bar
    height = 0
    # the objects to associate with
    entity = ""
    object = ""

    # configure attributes
    def __init__(self, name, entity, object):
        self.init("healthBar", name, 0, 0, False, True)
        self.entity = entity
        self.object = object
        # if the bar is the player's, make it thicker
        if self.object.name == "player":
            self.height = round(windowHeight / 30)
            # Move the bar to the top left of the screen
            self.x = round(windowWidth / 50)
            self.y = self.x
        else:
            self.height = round(windowHeight / 50)
        self.update()

    # update position and widths
    def update(self):
        # Update position and bar width
        # The width for the player's bar is much bigger than that of enemy bars.
        if self.object.name == "player":
            # set the player's healthBar's width based on window size
            entityWidth = round(windowWidth / 2)
        else:
            # move the bar to just above the entity's position
            self.x = self.object.x
            self.y = self.object.y - round(windowHeight / 24)
            # get the width of the entity's default frame
            entityWidth = pygame.image.load("graphics/" + self.object.folder + "/stand/0" + ".PNG").get_width()
        # set the width of the green section as a percentage of the max entity health and width of the entity
        self.gwidth = self.entity.health / self.entity.maxHealth * entityWidth
        # set width of the red section
        self.rwidth = entityWidth - self.gwidth

# Text objects
class text(objects):
    # text to write
    text = ""
    # colour of the text
    colour = ""
    # whether to antialias the text
    antialiasing = True

    # configure attributes
    def __init__(self, name, x, y, clickable, toRender, text, colour, antialiasing):
        self.init("text", name, x, y, clickable, toRender)
        self.text = text
        self.colour = colour
        self.antialiasing = antialiasing

    # centre text around coordinates
    def centreText(self, centre):
        textSize = font.size(self.text)
        self.x = centre[0] - round(textSize[0] / 2)
        self.y = centre[1] - round(textSize[1] / 2)

# images
class image(objects):
    # the path to the image
    file = ""
    # configure attributes
    def __init__(self, name, x, y, clickable, toRender, file):
        self.init("image", name, x, y, clickable, toRender)
        self.file = file

#animations. A folder of images to change every frame
class animation(objects):
    # the path to the folder name containing the images
    folder = ""
    # the current image ID
    current = 0
    # whether the animation is running
    state = 1
    # the total number of images in the folder
    totalStates = 0

    # configure attributes
    def __init__(self, name, x, y, clickable, toRender, folder, state):
        self.init("animation", name, x, y, clickable, toRender)
        self.folder = folder
        self.state = state

# entities. An object that has multiple animations it can switch between
class entity(objects):
    # list of states and how many images each state has
    states = [["stand", 3], ["walk", 5]]
    # the entities folder. contains all of it's graphics
    folder = ""
    # Player specific - should the player walk after landing a jump?
    jumpWalk = [False, "r"]
    # current image to render
    current = 0
    # total number of states in the folder
    totalStates = 3
    # current state folder to load from
    state = "stand"
    # previous active state
    previous = []
    # current entity orientation
    face = "r"
    # The distance left to knock back after an attack on the entity
    knockbackDistance = 0
    # The starting knockback distance
    knockbackDistanceMax = 0
    # The direction to knock back
    knockbackFace = "l"

    # configure attributes
    def __init__(self, name, x, y, clickable, toRender, states, state, folder, face):
        self.init("entity", name, x, y, clickable, toRender)
        self.states = states
        self.state = state
        self.folder = folder
        self.face = face
        self.updateVars()

    # change state
    def changeState(self, new):
        # TODO: This is probably breaking animations too
        # get the height of the old frame
        oldHeight = pygame.image.load(
            "graphics/" + self.folder + "/" + self.state + "/" + str(self.current) + ".PNG").get_height()
        # get the height of the new frame
        newHeight = pygame.image.load("graphics/" + self.folder + "/" + new + "/0.PNG").get_height()
        # if the new feet are different to the old, move to compensate
        # if self.y + oldHeight > self.y + newHeight:
        #     self.y += (self.y + oldHeight) - (self.y + newHeight)
        # elif self.y + oldHeight < self.y + newHeight:
        #     self.y += (self.y + newHeight) - (self.y + oldHeight)
        # add the old state to the previous states array
        if newHeight < oldHeight:
            self.y += oldHeight - newHeight
        self.previous.append(self.state)
        # if the array holds more than 2 states
        if len(self.previous) > 2:
            # remove the oldest one
            self.previous.pop(0)
        # change state
        self.state = new
        # update attributes
        self.updateVars()

    # update attributes after a state change etc
    def updateVars(self):
        # find the current state in the list of states
        for i in range(len(self.states)):
            if self.states[i][0] == self.state:
                # reset the current image
                self.current = 0
                # get the total number of images
                self.totalStates = self.states[i][1]
