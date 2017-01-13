import random

# Start game loop
def gameLoop(currentScene, optional):
    # Support libraries
    import pygame
    # temp is used to transfer data
    import temp

    keys = [[pygame.K_a,"a"],[pygame.K_b,"b"],[pygame.K_c,"c"],[pygame.K_d,"d"],[pygame.K_e,"e"],[pygame.K_f,"f"],[pygame.K_g,"g"],
            [pygame.K_h, "h"],[pygame.K_i,"i"],[pygame.K_j,"j"],[pygame.K_k,"k"],[pygame.K_l,"l"],[pygame.K_m,"m"],[pygame.K_n,"n"],
            [pygame.K_o, "o"],[pygame.K_p,"p"],[pygame.K_q,"q"],[pygame.K_r,"r"],[pygame.K_s,"s"],[pygame.K_t,"t"],[pygame.K_u,"u"],
            [pygame.K_v, "v"],[pygame.K_w,"w"],[pygame.K_x,"x"],[pygame.K_y,"y"],[pygame.K_z,"z"]]

    f = open("controls.txt","r")

    #The current control scheme. Name is the name of the control, key is the key assigned, found is whether the key was
    #found when iterating through heldKeys
    #[[name,key,found],[name,key,found]]
    controlScheme = [["left",int(f.readline()),False],["right",int(f.readline()),False],["jump",int(f.readline()),False],["attack 1",int(f.readline()),False],["attack 2",int(f.readline()),False],["attack 3",int(f.readline()),False],["block",int(f.readline()),False],["pause",int(f.readline()),False]]
    f.close()

    cL = 0
    cR = 1
    cJ = 2
    c1 = 3
    c2 = 4
    c3 = 5
    cB = 6
    cP = 7


    # the backdrop of the scene
    backdrop = ""
    # Later used to load the backdrop
    bg = None

    # Make the image path for the current backdrop
    backdrop = "graphics/" + currentScene + ".PNG"
    # load the image
    bg = pygame.image.load(backdrop)
    # get its dimensions
    windowWidth = bg.get_width()
    windowHeight = bg.get_height()

    # place the floor 1 tenth of the window size above the bottom
    floor = round((43 / 50) * windowHeight)

    # transfer the dimensions to temp
    temp.width = windowWidth
    temp.height = windowHeight
    temp.floor = floor

    # game modules
    import objects
    import game
    # Enemies
    import troll

    numEnemies = 1

    # if the scene is forest
    if currentScene == "forest":
        # import the scene module
        import forest
        # update knight stats based on window size
        game.knight.speed = round(windowWidth / 30)
        game.knight.jumpHeight = round(windowHeight / 4)

        # initialize player
        player = game.knight("player")
        entities = [player]
        player.attacks = player.setAttacks()

        # update troll stats based on window size
        game.troll.speed = round(windowWidth / 100)
        game.troll.jumpHeight = round(windowHeight / 10)

        game.enemyEntities = []
        # initialize enemy1
        for i in range(numEnemies):
            game.enemyEntities.append(game.troll("enemy" + str(i + 1)))
            game.enemyEntities[-1].__init__("enemy" + str(i + 1))

        # add all game objects to entities array
        for enemy in game.enemyEntities:
            entities.append(enemy)

        # find the player game object
        # store it for quicker access later
        for currentEntity in entities:
            if currentEntity.name == "player":
                playerEntity = currentEntity

        # initialize graphic objects based on window size
        forest.sceneObjects = forest.init(entities, windowWidth, windowHeight,numEnemies)
        # get list of objects
        sceneObjects = forest.sceneObjects

    # if the current scene is mainMenu
    elif currentScene == "mainMenu":
        # import the module
        import mainMenu
        # initialize the graphic objects based on window size
        mainMenu.sceneObjects = mainMenu.init(windowWidth, windowHeight)
        sceneObjects = mainMenu.sceneObjects

    elif currentScene == "controls":
        # import the module
        import controls
        # initialize the graphic objects based on window size
        controls.sceneObjects = controls.init(windowWidth, windowHeight, controlScheme)
        sceneObjects = controls.sceneObjects
        # Used to store which key is currently being remapped.
        currentKey = -1

    elif currentScene == "newScore":
        import newScore
        newScore.sceneObjects = newScore.init(optional)
        sceneObjects = newScore.sceneObjects

    elif currentScene == "leaderboard":
        import leaderboard
        leaderboard.sceneObjects = leaderboard.init(optional)
        sceneObjects = leaderboard.sceneObjects

    # find the player graphic object
    playerObject = None
    # by scanning through the list of graphic objects
    for currentObject in sceneObjects:
        if currentObject.name == "player":
            playerObject = currentObject
        # if the object's name starts with "enemy" add it a list of enemies
        elif currentObject.name[0:5] == "enemy":
            game.enemyObjects.append(currentObject)

    # Initialize pygame
    pygame.init()

    # Rate of height gain due to jumping (px/s)
    jumpSpeed = round(windowHeight * 0.08)

    # rate of falling due to gravity (px/s)
    gravity = round(windowHeight * 0.07)

    # Initialize the game window
    window = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("RPG Game")

    # Initialize game clock
    gameClock = pygame.time.Clock()
    FPS = 15

    # track how many more times to show the noStamina animation
    noStamina = 0

    paused = False

    # keys currently down
    heldKeys = []

    # Game has is not quitting yet
    gameQuit = False
    quitTimer = 30
    # the number of kills the player got. only used on gameQuit
    kills = 0

    # ID of the current attack being run
    attackID = 0

    # While the game is not quitting...
    while quitTimer > 0:
        # if the player exists
        if playerObject != None:
            # if the player is executing an attack
            if playerObject.state in playerEntity.attackNames:
                # execute the next frame
                playerEntity.attack(playerObject, playerEntity, windowWidth, attackID)

        # Check for events
        for event in pygame.event.get():
            # If the quit button (X) has been pressed
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                return "quitGame"
            # If ANY mouse button has pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If it was left click
                if event.button == 1:
                    # Check through all loaded graphic objects
                    for currentObject in range(len(sceneObjects)):
                        # is the object we're checking clickable?
                        if sceneObjects[currentObject].clickable:
                            # Is the mouse over the object?
                            if sceneObjects[currentObject].x - 1 < event.pos[0] < sceneObjects[currentObject].x + \
                                    sceneObjects[currentObject].width + 1 and sceneObjects[currentObject].y - 1 < \
                                    event.pos[1] < sceneObjects[currentObject].y + sceneObjects[
                                    currentObject].height + 1:
                                # Say so (will be used later)
                                # print(sceneObjects[currentObject].name)
                                if sceneObjects[currentObject].name == "quitGame":
                                    pygame.quit()
                                    return "quitGame"
                                if currentScene == "newScore":
                                    if len(sceneObjects[0].text) > 0:
                                        return sceneObjects[0].text
                                if currentScene == "controls":
                                    if sceneObjects[currentObject].name == "menu":
                                        f = open("controls.txt","w")
                                        for control in controlScheme:
                                            f.write(str(control[1]) + "\n")
                                        return "menu"
                                    else:
                                        if currentKey != -1:
                                            sceneObjects[currentKey].colour = objects.white
                                            for control in range(len(controlScheme)):
                                                if controlScheme[control][0] == sceneObjects[currentObject + 1].text:
                                                    sceneObjects[currentKey + 2].text = "=  " + pygame.key.name(controlScheme[control][1])
                                        currentKey = currentObject
                                else:
                                    return sceneObjects[currentObject].name

            # If a key has been pressed
            elif event.type == pygame.KEYDOWN:
                # add it to an array of held keys
                heldKeys.append(event.key)

            # if a key was lifted
            elif event.type == pygame.KEYUP:
                # see if it was held before
                for current in heldKeys:
                    # if it was
                    if current == event.key:
                        # remove it from the array of held keys
                        heldKeys.remove(current)

        if currentScene == "newScore":
            for key in heldKeys:
                if key == pygame.K_BACKSPACE and len(sceneObjects[0].text) > 0:
                    sceneObjects[0].text = sceneObjects[0].text[0:len(sceneObjects[0].text) - 1]
                elif len(sceneObjects[0].text) < 10:
                    for letter in keys:
                        if letter[0] == key:
                            sceneObjects[0].text = sceneObjects[0].text + letter[1]

        elif currentScene == "controls":
            if currentKey != -1:
                sceneObjects[currentKey].colour = objects.green
                sceneObjects[currentKey + 2].text = "Press a key..."
                if len(heldKeys) > 0:
                    for control in range(len(controlScheme)):
                        if controlScheme[control][0] == sceneObjects[currentKey + 1].text:
                            controlScheme[control][1] = heldKeys[0]
                            print(controlScheme[control][1])
                            sceneObjects[currentKey].colour = objects.white
                            key = pygame.key.name(heldKeys[0])
                            if len(key) > 2 and key[0] == "[" and key[-1] == "]":
                                key = "Keypad " + key[1:-1]
                            sceneObjects[currentKey + 2].text = "=  " + key
                            currentKey = -1
                            break


        # default to disabled
        disabled = True
        # if the player exists
        if playerObject is not None:
            # check if the player is in a state where keys should not be pressed
            disabled = playerObject.state in ["jump", "drop", "knockback", "pant","block"] or playerObject.state in playerEntity.attackNames or playerEntity.stamina <= 0

            # default all recognised keys to not pressed
            controlScheme[cL][2] = controlScheme[cR][2] = controlScheme[cJ][2] = controlScheme[c1][2] = controlScheme[c2][2] = controlScheme[c3][2] = controlScheme[cB][2] = False

            # check through all keys currently down
            for key in heldKeys:
                # if it's pause
                if key == controlScheme[cP][1] or paused == True:
                #     pause
                    paused = True
                    for currentObject in sceneObjects:
                        if currentObject.name == "pauseText":
                            currentObject.toRender = True
                            break
                    while paused:
                        for event in pygame.event.get():  # If the quit button (X) has been pressed
                            if event.type == pygame.QUIT:
                                # Quit the game
                                pygame.quit()
                                return "quitGame"

                            # If pause was pressed
                            elif event.type == pygame.KEYDOWN:
                                if event.key == controlScheme[cP][1]:
                                    # unpause
                                    paused = False
                                    currentObject.toRender = False
                                # add it to an array of held keys
                                heldKeys.append(event.key)  # if a key was lifted

                            elif event.type == pygame.KEYUP:
                                # see if it was held before
                                for current in heldKeys:
                                    # if it was
                                    if current == event.key:
                                        # remove it from the array of held keys
                                        heldKeys.remove(current)

                        font = pygame.font.SysFont(None, currentObject.size)
                        # Render the text
                        shownText = font.render(currentObject.text, currentObject.antialiasing, currentObject.colour)
                        # blit it onto the screen
                        window.blit(shownText, [currentObject.x, currentObject.y])
                        pygame.display.flip()

                        gameClock.tick(FPS)

                # if it's a
                if key == controlScheme[cL][1]:
                    # note that the key was found
                    controlScheme[cL][2] = True
                    # if the player isnt walking already
                    if not disabled:
                        if playerObject.state != "walk":
                        # walk
                            playerObject.changeState("walk")
                        # left
                        playerObject.face = "l"
                # if it's d
                if key == controlScheme[cR][1]:
                    controlScheme[cR][2] = True
                    # walk right
                    if not disabled:
                        if playerObject.state != "walk":
                            playerObject.changeState("walk")
                        playerObject.face = "r"
                # if both a and d are down
                if controlScheme[cL][2] and controlScheme[cR][2]:
                    # stand
                    if playerObject.state != "stand" and not disabled:
                        playerObject.changeState("stand")
                # if it's space
                if key == controlScheme[cJ][1]:
                    # jump
                    if playerObject.state != "jump" and not disabled:
                        playerObject.changeState("jump")
                        controlScheme[cL][2] = True
                # if it's KP1
                if key == controlScheme[c1][1]:
                    controlScheme[c1][2] = True
                    # execute attack 1
                    if not disabled:
                        if playerEntity.stamina >= playerEntity.attacks[0][1]:
                            playerEntity.attack(playerObject, playerEntity, windowWidth, 0)
                        else:
                            noStamina = 7
                    attackID = 0
                    controlScheme[c1][2] = True
                # if it's KP2
                if key == controlScheme[c2][1]:
                    controlScheme[c2][2] = True
                    # execute attack 2
                    if not disabled:
                        if playerEntity.stamina >= playerEntity.attacks[1][1]:
                            playerEntity.attack(playerObject, playerEntity, windowWidth, 1)
                        else:
                            noStamina = 7
                    attackID = 1
                # if it's KP3
                if key == controlScheme[c3][1]:
                    controlScheme[c3][2] = True
                    # execute attack 3
                    if not disabled:
                        if playerEntity.stamina >= playerEntity.attacks[2][1]:
                            playerEntity.attack(playerObject, playerEntity, windowWidth, 2)
                        else:
                            noStamina = 7
                    attackID = 2
                if key == controlScheme[cB][1]:
                    controlScheme[cB][2] = True
                    #block
                    if playerObject.state != "block" and not disabled:
                        if playerEntity.stamina >= round(currentEntity.maxStamina / (FPS * 5)):
                            playerObject.changeState("block")
                        else:
                            noStamina = 7
            # if no keys were found
            if True not in [controlScheme[cL][2], controlScheme[cR][2], controlScheme[cJ][2], controlScheme[c1][2], controlScheme[c2][2], controlScheme[c3][2], controlScheme[cB][2]] and not disabled:
                # stand
                if playerObject.state != "stand":
                    playerObject.changeState("stand")

        # entity actions
        for currentObject in sceneObjects:
            if currentObject.name == "noStamina":
                if noStamina > 0:
                    if currentObject.current == currentObject.totalStates - 2:
                        noStamina -= 1
                    if currentObject.state == 0:
                        currentObject.state = 1
                elif currentObject.state == 1:
                    currentObject.state = 0

            # if the current graphic object being scanned is an entity
            if currentObject.objectType == "entity":
                # associate entities with their game class counterpart (e.g knight/mage for the player etc)
                for currentEntity in entities:
                    if currentObject.name == currentEntity.name:

                        # if the entity is out of stamina
                        if currentEntity.stamina <= 0:
                            # Make sure it isn't negative
                            currentEntity.stamina = 0
                            # If the entity is not disabled
                            if not (currentObject.state in ["jump", "drop", "knockback", "pant","block"] or currentObject.state in currentEntity.attackNames):
                                # make them pant
                                currentObject.changeState("pant")
                                noStamina = 7

                        # if the entity is panting
                        if currentObject.state == "pant":
                            # if the entity's stamina has reached the minimum to stop
                            if currentEntity.stamina >= round(currentEntity.maxStamina / 4):
                                # revert to standing
                                currentObject.changeState("stand")

                        # add stamina naturally
                        if not (currentObject.state in ["jump", "drop", "knockback","block"] or currentObject.state in currentEntity.attackNames):
                            if currentEntity.maxStamina - currentEntity.stamina >= round(currentEntity.maxStamina / (FPS * 5)):
                                currentEntity.stamina += round(currentEntity.maxStamina / (FPS * 5))
                            else:
                                currentEntity.stamina = currentEntity.maxStamina

                        # if the entity is out of health
                        if currentEntity.health <= 0:
                            if currentObject.name == "player":
                                # store the player's kills
                                kills = playerEntity.kills
                                # remove them from the list of objects
                                sceneObjects.remove(currentObject)
                                entities.remove(currentEntity)
                                # start game quit
                                gameQuit = True
                            # if an enemy was defeated, add it to the players kill count
                            if currentObject.name[0:5] == "enemy":
                                # reset their current attack tracker
                                currentEntity.currentAttackID = None
                                playerEntity.kills += 1
                                position = 0
                                distance = 0
                                while distance < round(windowWidth/3):
                                    position = random.randint(0,windowWidth)
                                    # if the player is on the right of the enemy
                                    if playerObject.x > position:
                                        # get the distance between the enemy and the player
                                        distance = playerObject.x - position
                                    # if the player is on the left of the enemy
                                    else:
                                        # get the distance between the enemy and the player
                                        distance = position - playerObject.x
                                # if the attack delay isnt 0
                                # initialize the enemy
                                currentObject.__init__(currentObject.name, position, round(windowHeight / 2), currentObject.clickable,
                                                currentObject.toRender,currentObject.states, "stand",currentObject.folder, "l")
                                currentEntity.getHealth()
                                currentEntity.setHealth()

                        # if game is quitting, take 1 from the timer
                        if gameQuit:
                            quitTimer -= 1

                        # load the entity's current frame
                        image = pygame.image.load(
                            "graphics/" + currentObject.folder + "/" + currentObject.state + "/" + str(
                                currentObject.current) + ".PNG")
                        # get the y value of the entity's feet
                        feet = currentObject.y + image.get_height()

                        # Make sure entities are above the ground
                        if feet > floor:
                            currentObject.y = floor - image.get_height()

                        # Make sure entities are on the screen
                        if currentObject.x < 0:
                            currentObject.x = 0
                        elif currentObject.x + image.get_width() > windowWidth:
                            currentObject.x = windowWidth - image.get_width()

                        # blocking
                        if currentObject.state == "block":
                            if currentObject.name == "player" and (not controlScheme[cB][2] or playerEntity.stamina < round(currentEntity.maxStamina / (FPS * 5))):
                                playerObject.changeState("stand")
                                if playerEntity.stamina < round(currentEntity.maxStamina / (FPS * 5)):
                                    noStamina = 7
                            else:
                                currentEntity.stamina -= round(currentEntity.maxStamina / (FPS * 5))

                        elif currentEntity.armour != currentEntity.maxArmour:
                            currentEntity.armour = currentEntity.maxArmour

                        # gravity
                        # if the entity is not jumping, dropping or being knocked back AND the feet are above the floor
                        if (currentObject.state not in ["jump", "drop", "knockback"]) and (
                                not currentObject.state in currentEntity.attackNames) and (feet < floor):
                            # make the entity drop
                            if floor - feet >= gravity:
                                currentObject.changeState("drop")
                            else:
                                currentObject.y += floor - feet

                        # if the entity is dropping
                        if currentObject.state == "drop":
                            # if the distance between the entity's feet and the floor is more than or equal to the distance the entity moves per frame due to gravity
                            if floor - feet >= gravity:
                                # move the entity down at the rate of game gravity
                                currentObject.y += gravity
                            # if the distance is less than the amount needed for normal gravity
                            else:
                                # move the entity down the remaining distance
                                currentObject.y += floor - feet

                        # if the entity is attacking and the entity's feet are above the ground
                        # if currentObject.state in currentEntity.attackNames and feet < floor:
                        #     # move them back onto the ground
                        #     currentObject.y = floor - image.get_height()

                            # if the entity is dropping but they have reached the ground
                            if currentObject.y + image.get_height() == floor:
                                # revert to standing
                                currentObject.changeState("stand")

                        # if the entity is being knocked back
                        if currentObject.state == "knockback":
                            # Reset the enemy's attack
                            if currentObject.name[0:5] == "enemy":
                                currentEntity.currentAttackID = None
                            # keep them facing the right way
                            currentObject.face = currentObject.knockbackFace
                            # if the entity is below half way through the knockback sequence
                            if currentObject.knockbackDistance >= round(currentObject.knockbackDistanceMax / 2):
                                # make them gain height at half jump rate
                                currentObject.y -= round(jumpSpeed / 2)
                            # if the entity is above half way through the knockback sequence
                            elif currentObject.knockbackDistance != 0:
                                # make them lose weight at jump speed, in the same way as gravity
                                if floor - feet >= round(jumpSpeed / 2):
                                    currentObject.y += round(jumpSpeed / 2)
                                else:
                                    currentObject.y += floor - feet
                            # if the remaining knockback distance is more than 1.5 * the jump speed
                            if currentObject.knockbackDistance >= round(1.5 * jumpSpeed):
                                # add 1.5 * the jump speed to the x position
                                if currentObject.face == "l":
                                    currentObject.x -= round(1.5 * jumpSpeed)
                                else:
                                    currentObject.x += round(1.5 * jumpSpeed)
                                # take the amount moved from the remaining distance
                                currentObject.knockbackDistance -= 1.5 * jumpSpeed
                            # if the remaining distance is less than 1.5 * the jump speed
                            elif currentObject.knockbackDistance != 0:
                                # add the remaining distance
                                if currentObject.face == "l":
                                    currentObject.x -= currentObject.knockbackDistance
                                else:
                                    currentObject.x += currentObject.knockbackDistance
                                # reset knockback
                                currentObject.knockbackDistance = 0
                            # if there is no knockback remaining
                            else:
                                # if the entity is on the ground
                                if currentObject.y == 0:
                                    # stand
                                    currentObject.changeState("stand")
                                # if the entity is in the air
                                else:
                                    # drop
                                    currentObject.changeState("drop")

                        # walking
                        # if:
                        # the entity is walking
                        # OR
                        # they're walking AND they were walking before they jumped
                        # OR
                        # they're dropping AND they were last walking OR the state before last was walk
                        if currentObject.state == "walk" or (
                                        currentObject.state == "jump" and currentObject.previous[-1] == "walk") or (
                                        currentObject.state == "drop" and (
                                                currentObject.previous[-1] == "walk" or currentObject.previous[
                                            -2] == "walk")):
                            # move the entity based on their game entity's walk speed
                            if currentObject.face == "l":
                                currentObject.x -= currentEntity.speed
                            else:
                                currentObject.x += currentEntity.speed

                        # jumping
                        # if the entity is jumping
                        if currentObject.state == "jump":
                            # if the entity is below the jump height
                            if currentObject.y > floor - image.get_height() - currentEntity.jumpHeight:
                                # if the difference between the entity and the jump height is 15 or more
                                if currentObject.y - (
                                                floor - image.get_height() - currentEntity.jumpHeight) >= jumpSpeed:
                                    # move up 15
                                    currentObject.y -= jumpSpeed
                                # if the difference is less than 15
                                else:
                                    # set the y to max jump height
                                    currentObject.y = floor - image.get_height() - currentEntity.jumpHeight
                                    # if the entity is at or above jump height
                            if currentObject.y <= floor - image.get_height() - currentEntity.jumpHeight:
                                # switch to dropping
                                currentObject.changeState("drop")

                        # enemy attack continuation and AI call
                        # if they are not the player and they are not disabled
                        if currentObject.name[0:5] == "enemy" and currentObject.state not in ["jump", "drop", "knockback", "pant"]:
                            # if they are not attacking
                            if not currentObject.state in currentEntity.attackNames:
                                # call their AI file
                                troll.react(currentObject, currentEntity, playerObject, playerEntity, windowWidth)
                            # if they just finished attacking, revert to standing
                            elif currentEntity.currentAttack == "none":
                                currentObject.changeState("stand")
                                currentEntity.currentAttackID = None
                            # if they are attacking
                            else:
                                currentEntity.currentAttackID = None
                                # continue the attack
                                currentEntity.attack(playerObject, playerEntity, currentObject, windowWidth,
                                                     currentEntity.currentAttack)

        # Wipe the screen
        window.fill(objects.white)
        # If the current scene has a backdrop
        if backdrop != "":
            # blit it onto the screen
            window.blit(bg, [0, 0])

        ########GRAPHIC OBJECT BEHAVIOUR
        # Check through all loaded objects
        for currentObject in range(len(sceneObjects)):
            # If the current object is visible
            if sceneObjects[currentObject].toRender:
                # "shortcut" to the current object's class instance
                workingObject = sceneObjects[currentObject]
                # if the object is a rectangle

                if workingObject.objectType == "rectangle":
                    # draw it
                    pygame.draw.rect(window, workingObject.colour,
                                     [workingObject.x, workingObject.y, workingObject.width, workingObject.height])

                # If it's text
                elif workingObject.objectType == "text":
                    # initialize the font
                    font = pygame.font.SysFont(None, workingObject.size)
                    # Render the text
                    shownText = font.render(workingObject.text, workingObject.antialiasing, workingObject.colour)
                    # blit it onto the screen
                    window.blit(shownText, [workingObject.x, workingObject.y])

                # If it's an image
                elif workingObject.objectType == "image":
                    # load
                    image = pygame.image.load(workingObject.file).convert_alpha()
                    # blit
                    window.blit(image, [workingObject.x, workingObject.y])

                # if it's an animated image
                elif workingObject.objectType == "animation":
                    # if the animation is running
                    if workingObject.state == 1:
                        # load its current image, taken from the images array inside of its folder
                        image = pygame.image.load("graphics/" + workingObject.folder + "/" + str(
                            workingObject.current) + ".PNG").convert_alpha()

                        # get the height of the old frame
                        if workingObject.totalStates > 1:
                            if workingObject.current == 0:
                                oldHeight = pygame.image.load(
                                    "graphics/" + workingObject.folder + "/" + str(workingObject.totalStates - 1) + ".PNG").get_height()
                            else:
                                oldHeight = pygame.image.load(
                                    "graphics/" + workingObject.folder + "/" + str(workingObject.current - 1) + ".PNG").get_height()
                            newHeight = image.get_height()

                            # if the new feet are different to the old, move to compensate
                            if newHeight < oldHeight:
                                workingObject.y += oldHeight - newHeight
                            elif newHeight > oldHeight:
                                workingObject.y -= newHeight - oldHeight

                        # blit
                        window.blit(image, [workingObject.x, workingObject.y])
                        # reset current image id if the last image has been drawn
                        if workingObject.current == workingObject.totalStates - 1:
                            workingObject.current = 0
                        else:
                            # increment current image
                            workingObject.current += 1

                # if it's an entity. entities are used for associating the state of an entity with multiple animations
                # entity animations are always running
                elif workingObject.objectType == "entity":
                    # load the current image from it's state folder, from the entity's folder
                    image = pygame.image.load(
                        "graphics/" + workingObject.folder + "/" + workingObject.state + "/" + str(
                            workingObject.current) + ".PNG").convert_alpha()
                    # if the image is facing left, flip it
                    if workingObject.face == "l":
                        image = pygame.transform.flip(image, True, False)
                    # blit
                    window.blit(image, [workingObject.x, workingObject.y])
                    # reset if last image is reached.
                    if workingObject.current >= workingObject.totalStates - 1:
                        workingObject.current = 0
                    elif workingObject.totalStates > 1:
                        # increment current image
                        workingObject.current += 1

                # if it's a health bar
                elif workingObject.objectType == "healthBar":
                    # update the health bar's position
                    workingObject.update()
                    # draw the green section
                    pygame.draw.rect(window, objects.green,
                                     [workingObject.x, workingObject.y, workingObject.gwidth, workingObject.height])
                    # draw the red section
                    pygame.draw.rect(window, objects.red,
                                     [workingObject.x + workingObject.gwidth, workingObject.y, workingObject.rwidth,
                                      workingObject.height])

                    if workingObject.object.name == "player":
                        font = pygame.font.SysFont(None, round(workingObject.entityWidth * 25 / 320))
                    else:
                        font = pygame.font.SysFont(None, round(workingObject.entityWidth * 25 / 100))
                    shownText = font.render(str(workingObject.entity.health) + "/" + str(workingObject.entity.maxHealth), True, objects.green)
                    # blit it onto the screen
                    if workingObject.object.name == "player":
                        window.blit(shownText,
                                    [workingObject.x + workingObject.entityWidth, workingObject.y])
                    else:
                        window.blit(shownText, [workingObject.x, workingObject.y - font.size(str(workingObject.entity.health))[1]])

                # if it's a stamina bar
                elif workingObject.objectType == "staminaBar":
                    # update the stamina bar's position
                    workingObject.update()
                    # draw the green section
                    pygame.draw.rect(window, objects.lblue,
                                     [workingObject.x, workingObject.y, workingObject.bwidth, workingObject.height])
                    # draw the red section
                    pygame.draw.rect(window, objects.grey,
                                     [workingObject.x + workingObject.bwidth, workingObject.y, workingObject.gwidth,
                                      workingObject.height])

                elif workingObject.objectType == "killCounter":
                    font = pygame.font.SysFont(None, round(windowWidth * 25 / 800))
                    shownText = font.render("Kills: " + str(workingObject.entity.kills), True, objects.yellow)
                    window.blit(shownText, [windowWidth - round(windowWidth / 100) - font.size("Kills: " + str(workingObject.entity.kills))[0], round(windowWidth / 100)])

        # update all loaded graphic objects
        pygame.display.flip()

        # tick the game clock
        gameClock.tick(FPS)

    # outside of game loop, so the game must be ending. Quit pygame.
    pygame.quit()
    if currentScene == "forest":
        return kills
