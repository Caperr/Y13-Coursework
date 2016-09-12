#Support libraries
import pygame
#Scenes
import mainMenu
import forest
#Game modules
import objects
import game
#Enemies
import troll

floor = 575

entities = []

playerObject = "none"

#Initialize pygame
pygame.init()

#Rate of height game due to jumping (px/s)
jumpSpeed = 35

#rate of falling due to gravity (px/s)
gravity = 40

#The dimentions of the game window
windowWidth = 800
windowHeight = 600
#Initialize the game window
window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("RPG Game")

#Initialize game clock
gameClock = pygame.time.Clock()
FPS = 10

#Start game loop
def gameLoop():
  key = ""
  #Game has is not quitting yet
  gameQuit = False
  #Current graphics module to use
  currentScene = "forest"

  #Load graphics module
  if currentScene == "mainMenu":
    sceneObjects = mainMenu.sceneObjects
    backdrop = mainMenu.backdrop

  #...
  elif currentScene == "forest":
    sceneObjects = forest.sceneObjects
    backdrop = forest.backdrop

  #initialize player
  player = game.knight("player")
  entities = [player]
##  player = entity("entity","player",80,475,False,True,[["walk",3],["stand",1]],"stand","player","r")
##  sceneObjects.append(player)

  enemy1 = game.troll("enemy1")
  game.enemies.append(enemy1)
  
  for enemy in game.enemies:
    entities.append(enemy)
##  for currentObject in sceneObjects:
##    if currentObject.objectType == "entity":
##      entities.append(currentObject)

  for currentObject in sceneObjects:
    if currentObject.name == "player":
      playerObject = currentObject
  for currentEntity in entities:
    if currentEntity.name == "player":
      playerEntity = currentEntity
  
  #While the game is not quitting...
  while not gameQuit:

##    for currentObject in sceneObjects:
##      for currentEntity in entities:
##        if currentObject.name == currentEntity.name:
##          if currentObject.name != "player":
##              currentEntity.attack(playerObject,playerEntity,currentObject,windowWidth)
    
##    print(entities)
##    print(sceneObjects)
    #Check for events
    for event in pygame.event.get():
##      print(event)
      #If the quit button (X) has been pressed
      if event.type == pygame.QUIT:
        #Quit the game
        gameQuit = True
      #If ANY mouse button has pressed
      elif event.type == pygame.MOUSEBUTTONDOWN:
        #If it was left click
        if event.button == 1:
          #Check through all loaded graphic objects
          for currentObject in range(len(sceneObjects)):
            #is the object we're checking clickable?
            if sceneObjects[currentObject].clickable:
              #Is the mouse over the object?
              if sceneObjects[currentObject].x - 1 < event.pos[0] < sceneObjects[currentObject].x + sceneObjects[currentObject].width + 1 and sceneObjects[currentObject].y -1 < event.pos[1] < sceneObjects[currentObject].y + sceneObjects[currentObject].height + 1:
                #Say so (will be used later)
                print("click " + sceneObjects[currentObject].name)

      #If a key has been pressed
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          key = "a"
          playerObject.face = "l"
          if not playerObject.state in ["jump","drop,knockback"]:
            playerObject.changeState("walk")
          else:
            playerObject.jumpWalk = [True,"l"]
        elif event.key == pygame.K_d:
          key = "d"
          playerObject.face = "r"
          if not playerObject.state in ["jump","drop,knockback"]:
            playerObject.changeState("walk")
          else:
            playerObject.jumpWalk = [True,"r"]
        elif event.key == 257:
          if not playerObject.state in ["jump","drop","knockback"]:
            playerObject.changeState("swing")
            key == "KP1"
        if event.key == pygame.K_SPACE and playerObject.state in ["walk","stand"]:
          playerObject.changeState("jump")
          if key == "a":
            playerObject.jumpWalk = [True,"l"]
          elif key == "d":
            playerObject.jumpWalk = [True,"r"]
            

      elif event.type == pygame.KEYUP:
        if (event.key == pygame.K_a and key == "a") or (event.key == pygame.K_d and key == "d"):
          if not playerObject.state in ["jump","drop"]:
            playerObject.changeState("stand")
          else:
            playerObject.jumpWalk[0] = False
          key = ""

    #Wipe the screen
    window.fill(objects.white)
    #If the current scene has a backdrop
    if backdrop != "":
      #Load the backdrop
      bg = pygame.image.load(backdrop)
      #blit it onto the screen
      window.blit(bg,[0,0])

########GRAPHIC OBJECT BEHAVIOUR
    #Check through all loaded objects
    for currentObject in range(len(sceneObjects)):
      #If the current object is visible
      if sceneObjects[currentObject].toRender:
        #"shortcut" to the current object's class instance
        workingObject = sceneObjects[currentObject]
        #if the object is a rectangle
        if workingObject.objectType == "rectangle":
          #draw it
          pygame.draw.rect(window, workingObject.colour, [workingObject.x,workingObject.y,workingObject.width,workingObject.height])
        #If it's text
        elif workingObject.objectType == "text":
          #Render the text
          shownText = font.render(workingObject.text,workingObject.antialiasing,workingObject.colour)
          #blit it onto the screen
          window.blit(shownText, [workingObject.x,workingObject.y])
        #If it's an image
        elif workingObject.objectType == "image":
          #load
          image = pygame.image.load(workingObject.file).convert_alpha()
          #blit
          window.blit(image, [workingObject.x,workingObject.y])
        #if it's an animated image
        elif workingObject.objectType == "animation":
          #if the animation is running
          if workingObject.state == 1:
            #load it's current image, taken from the images array inside of it's folder
            image = pygame.image.load("graphics/" + workingObject.folder + "/" + str(workingObject.current) + ".PNG").convert_alpha()
            #blit
            window.blit(image, [workingObject.x,workingObject.y])
            #increment current image
            workingObject.current += 1
            #reset current image id if the last image has been drawn
            if workingObject.current == workingObject.totalStates:
              workingObject.current = 0
        #if it's an entity. entities are used for associating the state of an entity with multiple animations
        #entity animations are always running
        elif workingObject.objectType == "entity":
          #load the current image from it's state folder, from the entity's folder
          image = pygame.image.load("graphics/" + workingObject.folder + "/" + workingObject.state + "/" + str(workingObject.current) + ".PNG").convert_alpha()
          #if the image is facing left, flip it
          if workingObject.face == "l":
            image = pygame.transform.flip(image, True, False)
          #blit
          window.blit(image, [workingObject.x,workingObject.y])
          #increment current image
          workingObject.current += 1
          #reset if last image is reached.
          if workingObject.current == workingObject.totalStates:
            workingObject.current = 0

    #entity actions
    for currentObject in sceneObjects:
##        print(currentObject.previous)
##        print(currentObject.jumpWalk)
      if currentObject.objectType == "entity":
        image = pygame.image.load("graphics/" + currentObject.folder + "/" + currentObject.state + "/" + str(currentObject.current) + ".PNG")
        feet = currentObject.y + image.get_height()
##          print("feet",feet)
##          print("floor",floor)
##          print(feet > floor)
        #Make sure entities are above the ground
        if feet > floor:
          currentObject.y = floor - image.get_height()
        #Make sure entities are on the screen
        if currentObject.x < 0:
          currentObject.x = 0
        elif currentObject.x + image.get_width() > windowWidth:
          currentObject.x = windowWidth - image.get_width()
        #gravity
        if currentObject.state not in ["jump","drop","knockback"] and feet < floor:
          currentObject.changeState("drop")
        if currentObject.state == "drop":
          if floor - feet >= gravity:
            currentObject.y += gravity
          else:
            currentObject.y += floor - feet
        if currentObject.state == "drop" and currentObject.y + image.get_height() == floor:
          currentObject.changeState("stand")
          if currentObject.name == "player":
            if currentObject.jumpWalk[0]:
              currentObject.changeState("walk")
              currentObject.face = currentObject.jumpWalk[1]
            currentObject.jumpWalk[0] = False
        if currentObject.state == "knockback":
          currentObject.face = currentObject.knockbackFace
          if currentObject.knockbackDistance >= round(currentObject.knockbackDistanceMax/2):
            currentObject.y -= round(jumpSpeed/2)
          elif currentObject.knockbackDistance != 0:
            if floor - feet >= round(jumpSpeed/2):
              currentObject.y += round(jumpSpeed/2)
            else:
              currentObject.y += floor - feet
          if currentObject.knockbackDistance >= round(1.5*jumpSpeed):
            if currentObject.face == "l":
              currentObject.x -= round(1.5*jumpSpeed)
            else:
              currentObject.x += round(1.5*jumpSpeed)
            currentObject.knockbackDistance -= 1.5*jumpSpeed
          elif currentObject.knockbackDistance != 0:
            if currentObject.face == "l":
              currentObject.x -= currentObject.knockbackDistance
            else:
              currentObject.x += currentObject.knockbackDistance
            currentObject.knockbackDistance = 0
          else:
            if currentObject.y == 0:
              currentObject.changeState("stand")
              if currentObject.name == "player":
                if currentObject.jumpWalk[0]:
                  currentObject.changeState("walk")
                  currentObject.face = currentObject.jumpWalk[1]
                currentObject.jumpWalk[0] = False
            else:
              currentObject.changeState("drop")
        #associate entities with their game class counterpart (e.g knight/mage for the player etc)
        for currentEntity in entities:
          if currentObject.name == currentEntity.name:
            #walking
            if currentObject.state == "walk" or (currentObject.state == "jump" and currentObject.previous[-1] == "walk") or (currentObject.state == "drop" and (currentObject.previous[1] == "walk" or currentObject.previous[-2] == "walk")):
              if currentObject.face == "l":
                currentObject.x -= currentEntity.speed
              else:
                currentObject.x += currentEntity.speed
            #jumping
            if currentObject.state == "jump":
  ##              maxheight = floor - image.get_height() - currentEntity.jumpHeight
  ##              print("max",floor - image.get_height() - currentEntity.jumpHeight)
  ##              print("y",currentObject.y)
              #if the entity is below the jump height
              if currentObject.y > floor - image.get_height() - currentEntity.jumpHeight:
                #if the difference between the entity and the jump height is 15 or more
                if currentObject.y - (floor - image.get_height() - currentEntity.jumpHeight) >= jumpSpeed:
                  #move up 15
                  currentObject.y -= jumpSpeed
                #if the difference is less than 15
                else:
                  #set the y to max jump height
                  currentObject.y = floor - image.get_height() - currentEntity.jumpHeight
              #if the entity is at or above jump height
              if currentObject.y <= floor - image.get_height() - currentEntity.jumpHeight:
                #switch to dropping
                currentObject.changeState("drop")

        for currentObject in sceneObjects:
          for currentEntity in entities:
            if currentObject.name == currentEntity.name:
              if currentObject.name != "player":
                  currentEntity.attack(playerObject,playerEntity,currentObject,windowWidth)
        


    #update all loaded graphic objects
    pygame.display.flip()

    #tick the game clock
    gameClock.tick(FPS)

  #outside of game loop, so the game must be ending. Quit pygame.
  pygame.quit()

#start the game loop
gameLoop()
