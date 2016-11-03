# Imports
import random
import pygame
import temp

windowWidth = temp.width
windowHeight = temp.height

# list of all enemy instances
enemyObjects = []
enemyEntities = []

# Deal damage to an entity
def damage(giverObject, receiverObject, receiverEntity, damType, amount):
    # print(giverObject.name, "dealt", amount, damType, "damage to", receiverObject.name)
    # for physical damage...
    if damType == "physical":
        # Take health away from the receiver based on their armour
        receiverEntity.health -= amount - round(amount * (receiverEntity.armour / 100))


##############################

# Class templates
class classes:
    # player health
    health = 20
    # Max player health
    maxHealth = 20
    # Armour - % physical damage reduction
    armour = 0
    # Maximum armour. I'll need this if I have an armour boosting spell etc
    maxArmour = 0
    # Player name. used in game and also in save management
    name = ''
    # How many health potions the player has
    healthPot = 0
    # what class they are
    classType = ""
    # Stamina determines how fast the player can use physical moves, such as dodging, hitting, running, etc.
    # When completely depleted, the player is immobilized to pant for a small amount of time to allow stamina to
    # recharge.
    # Stamina is recharged naturally over time, or can be recharged instantly with sugary food.
    stamina = 100
    maxStamina = 100
    # Player walking speed
    speed = 0
    # Player jump height
    jumpHeight = 0
    # temporary variables for use in animation
    startX = 0
    startWidth = 0
    # current move being run
    currentAttack = []
    # level, increased by experience
    level = 1
    # track the progress, in frames, of certain attacks/moves
    progress = 0
    # The number of kills the player has achieved
    kills = 0

    # run an attack or move.
    def attack(self, playerObject, playerEntity, windowWidth, move):
        # if they are not already running the move, this must be the first frame.
        if playerObject.state not in self.attackNames:
            # run the move specified by the user, with initialization
            self.attacks[move][0](True, playerObject, windowWidth)
            # store the attack being run for later
            self.currentAttack = self.attacks[move]
        # if it's not the first frame
        else:
            # run the move as normal without initialization
            self.currentAttack[0](False, playerObject, windowWidth)

    # initialize player
    def init(self, name):
        # Set the player's name
        self.name = name

    # Dodge an incoming attack. Since attack hit is based solely on proximity, all it needs to do is move the player.
    def dodge(self):
        pass

    # update player stats when they pass a boundary in experience
    def levelUp(self):
        pass
        # update BY ADDING (NOT BY SETTING (MAYBE??????)) armour(?), maxArmour, health, maxHealth, etc based on level


# Class template for a knight
class knight(classes):
    # configure the class instance
    classType = "Knight"
    armour = 10
    maxArmour = armour
    startX = 0
    startWidth = 0

    # set the instance's name
    def __init__(self, name):
        self.init(name)

    # hit all frontal entities with your sword
    # medium physical damage, small knockback
    # medium stamina consumption
    def swing(self, firstFrame, playerObject, windowWidth):
        # if it's the first frame of the attack
        if firstFrame:
            # change the graphic object's state
            playerObject.changeState("swing")
            # load the first frame of the attack
            playerImage = pygame.image.load("graphics/player/swing/0.PNG")
            # get the starting position and width
            self.startX = playerObject.x
            self.startWidth = playerImage.get_width()
            # if the player is facing right
            if playerObject.face == "r":
                # add their starting width. This means that hits will be detected from on the right of the player, rather than inside of them.
                self.startX += self.startWidth
            # take a medium amount of stamina
            self.stamina -= round(self.maxStamina * 0.3)
        # if it's not the first frame
        else:
            # load the current frame
            playerImage = pygame.image.load("graphics/player/swing/" + str(playerObject.current) + ".PNG")
            # check through all enemies for hits
            for enemyObject in enemyObjects:
                # The attack has not landed a hit on this enemy this frame
                hit = 0
                # associate enemy graphic objects with their game objects
                for enemyEntity in enemyEntities:
                    if enemyEntity.name == enemyObject.name:
                        # load the enemy's current frame
                        enemyImage = pygame.image.load(
                            "graphics/" + enemyObject.folder + "/" + enemyObject.state + "/" + str(enemyObject.current) + ".PNG")
                        # if the player is facing left
                        if playerObject.face == "l":
                            # See if the player and the enemy images intersect in any of the space the player extended into
                            if self.startX > enemyObject.x + enemyImage.get_width() > playerObject.x or self.startX > enemyObject.x > playerObject.x or enemyObject.x + enemyImage.get_width() > playerObject.x > enemyObject.x:
                                # if an intersection is found, the enemy was hit on this frame
                                if not (enemyObject.state == "block" and enemyObject.face != playerObject.face):
                                    hit = 1
                            # Move the player back to compensate for the extending image
                            playerObject.x = self.startX - (playerImage.get_width() - self.startWidth)
                        # if the player is facing right
                        else:
                            # check for intersections
                            if self.startX < enemyObject.x < playerObject.x + playerImage.get_width() or self.startX < enemyObject.x + enemyImage.get_width() < playerObject.x or enemyObject.x < playerObject.x + playerImage.get_width() < enemyObject.x + enemyImage.get_width():
                                if not (enemyObject.state == "block" and enemyObject.face != playerObject.face):
                                    hit = 1
                        # if the enemy was hit
                        if hit == 1:
                            # take away health
                            damage(playerObject, enemyObject, enemyEntity, "physical",
                                   round(2 * self.level + random.randint(-self.level, self.level)))
                            # knock the enemy back
                            enemyObject.changeState("knockback")
                            # knock them back 1 tenth of the screen length
                            enemyObject.knockbackDistance = round(windowWidth / 10)
                            enemyObject.knockbackDistanceMax = enemyObject.knockbackDistance
                            # make the enemy face the way the player is facing
                            enemyObject.knockbackFace = playerObject.face
        # if the animation is complete
        if playerObject.current == playerObject.totalStates - 1:
            # revert back to standing
            playerObject.changeState("stand")
            # move the player back to their original position
            if playerObject.face == "l":
                playerObject.x = self.startX
            else:
                playerObject.x = self.startX - self.startWidth

    # hit all frontal entities with your shield
    # low physical damage, large knockback
    # medium stamina consumption
    def shieldBash(self, firstFrame, playerObject, windowWidth):
        # if its the first frame
        if firstFrame:
            # update their graphic object
            playerObject.changeState("shieldBash")
            # load the starting frame
            playerImage = pygame.image.load("graphics/player/shieldBash/0.PNG")
            # get their starting position and width
            self.startX = playerObject.x
            self.startWidth = playerImage.get_width()
            # if the player is facing right
            if playerObject.face == "r":
                # add their starting width. This means that hits will be detected from on the right of the player, rather than inside of them.
                self.startX += self.startWidth
            # take a small amount of stamina
            self.stamina -= round(self.maxStamina * 0.25)
        # if it's not the first frame
        else:
            playerImage = pygame.image.load("graphics/player/shieldBash/" + str(playerObject.current) + ".PNG")
            # scan through all enemies
            for enemyObject in enemyObjects:
                # the attack has not hit the enemy this frame
                hit = 0
                # associate the enemy graphic object with their game object
                for enemyEntity in enemyEntities:
                    if enemyEntity.name == enemyObject.name:
                        # load this enemy's current frame
                        enemyImage = pygame.image.load(
                            "graphics/" + enemyObject.folder + "/" + enemyObject.state + "/" + str(
                                enemyObject.current) + ".PNG")
                        # if the player is facing left
                        if playerObject.face == "l":
                            # See if the player and the enemy images intersect in any of the space the player extended into
                            if self.startX > enemyObject.x + enemyImage.get_width() > playerObject.x or self.startX > enemyObject.x > playerObject.x or enemyObject.x + enemyImage.get_width() > playerObject.x > enemyObject.x:
                                # if an intersection is found, the enemy was hit
                                if not (enemyObject.state == "block" and enemyObject.face != playerObject.face):
                                    hit = 1
                            # move the player back to compensate for width gain
                            playerObject.x = self.startX - (playerImage.get_width() - self.startWidth)
                        # if the player is facing right
                        else:
                            # scan for intersections
                            if self.startX < enemyObject.x < playerObject.x + playerImage.get_width() or self.startX < enemyObject.x + enemyImage.get_width() < playerObject.x or enemyObject.x < playerObject.x + playerImage.get_width() < enemyObject.x + enemyImage.get_width():
                                if not (enemyObject.state == "block" and enemyObject.face != playerObject.face):
                                    hit = 1
                        # if the enemy was hit
                        if hit == 1:
                            # deal damage
                            damage(playerObject, enemyObject, enemyEntity, "physical",
                                   round(1.2 * self.level + random.randint(-self.level, self.level)))
                            # knock them back
                            enemyObject.changeState("knockback")
                            enemyObject.knockbackDistance = round(windowWidth / 4)
                            enemyObject.knockbackDistanceMax = enemyObject.knockbackDistance
                            enemyObject.knockbackFace = playerObject.face
        # if the animation is complete
        if playerObject.current == playerObject.totalStates - 1:
            # revert to standing
            playerObject.changeState("stand")
            # move back to original position
            if playerObject.face == "l":
                playerObject.x = self.startX
            else:
                playerObject.x = self.startX - self.startWidth

    # dash in a line in front of player with your sword. ensure movement keys do not interrupt.
    # high physical damage, low knockback
    # high stamina consumption
    def swordDash(self, firstFrame, playerObject, windowWidth):
        # if it's the first frame
        if firstFrame:
            # change graphic object state
            playerObject.changeState("swordDash")
            # load the first frame
            playerImage = pygame.image.load("graphics/player/stand/0.PNG")
            # get starting width
            self.startWidth = playerImage.get_width()
            # reset the move progress
            self.progress = 5
            # take a large amount of stamina
            self.stamina -= round(self.maxStamina * 0.6)
        # if it's not the first frame and the progress is not 0
        elif self.progress > 0:
            # load the current frame
            playerImage = pygame.image.load("graphics/player/swordDash/" + str(playerObject.current) + ".PNG")
            # scan through all enemies
            for enemyObject in enemyObjects:
                # associate with their graphic object
                for enemyEntity in enemyEntities:
                    # the enemy was not hit this frame
                    hit = 0
                    if enemyEntity.name == enemyObject.name:
                        # load this enemy's current frame
                        enemyImage = pygame.image.load(
                            "graphics/" + enemyObject.folder + "/" + enemyObject.state + "/" + str(
                                enemyObject.current) + ".PNG")
                        # if the player is facing left
                        if playerObject.face == "l":
                            # check for intersections in the width the player gained
                            if self.startX > enemyObject.x + enemyImage.get_width() > playerObject.x or self.startX > enemyObject.x > playerObject.x or enemyObject.x + enemyImage.get_width() > playerObject.x > enemyObject.x:
                                if not (enemyObject.state == "block" and enemyObject.face != playerObject.face):
                                    hit = 1
                        # if the player facing right
                        else:
                            # check for intersections
                            if self.startX < enemyObject.x < playerObject.x + playerImage.get_width() or self.startX < enemyObject.x + enemyImage.get_width() < playerObject.x or enemyObject.x < playerObject.x + playerImage.get_width() < enemyObject.x + enemyImage.get_width():
                                if not (enemyObject.state == "block" and enemyObject.face != playerObject.face):
                                    hit = 1
                        # if the enemy was hit
                        if hit == 1:
                            # deal damage
                            damage(playerObject, enemyObject, enemyEntity, "physical",
                                   round(1.7 * self.level + random.randint(-self.level, self.level)))
                            # knock them back
                            enemyObject.changeState("knockback")
                            enemyObject.knockbackDistance = round(windowWidth / 15)
                            enemyObject.knockbackDistanceMax = enemyObject.knockbackDistance
                            enemyObject.knockbackFace = playerObject.face
            # move the player
            if playerObject.face == "r":
                playerObject.x += round(windowWidth * 5/80)
            else:
                playerObject.x -= round(windowWidth * 5/80)
            # take one from the progress
            self.progress -= 1
        # if progress is done, revert to standing
        else:
            playerObject.changeState("stand")

    # block all frontal attacks (not sure if it's only physical or not)
    # low stamina consumption
    # on 0 stamina, play a block break animation and take damage
    # may stun based on timing (maybe distance)? not sure.
    # def block(self):
    #     pass

    def setAttacks(self):
        return [[self.swing, round(self.maxStamina * 0.3)], [self.shieldBash, round(self.maxStamina * 0.25)],
         [self.swordDash, round(self.maxStamina * 0.6)]]

    # list of all of the attacks. used multi-dimensional array because I might need to pass more data in the future
    attacks = []
    # list of all of the attack names
    attackNames = ["swing", "shieldBash", "swordDash"]


# Mage template
class mage(classes):
    armour = 5
    maxArmour = armour
    # similar concept to stamina, but for casting spells.
    mana = 100
    classType = "Mage"


# archer template
class archer(classes):
    armour = 3
    maxArmour = armour
    classType = "Archer"


# rogue template
class rogue(classes):
    armour = 3
    maxArmour = armour
    classType = "Rogue"


###############################

# Enemy templates
class enemy:
    # entity name. used for linking this class and graphics class.
    name = ""
    # entity health
    health = 0
    # max entity health
    maxHealth = 0
    # armour
    armour = 0
    maxArmour = 0
    # entity level
    level = 1
    # Walking speed
    speed = 0
    # Jump Height
    jumpHeight = 0
    # The delay, in frames, between attacks
    attackDelay = 0
    # last attack scanned
    currentAttack = "none"
    # The ID of the attack to be run
    currentAttackID = None
    # current distance from the player
    distance = 0
    # temporary variables for use in animation
    startX = 0
    startWidth = 0
    # track the progress, in frames, of certain attacks/moves
    progress = 0
    # placeholders to stop errors
    stamina = 1
    maxStamina = 1

    # same as player dodge
    def dodge(self):
        pass

    # set entity health and maxhealth
    def setHealth(self):
        # slightly randomize entity health and maxhealth based on a base, class specific value, and also based on level.
        self.health = round(self.health + (((random.randint(0, 5)) / 10) * self.level))
        self.health = random.randint(self.health - round(0.3 * self.level), self.health + round(0.3 * self.level))
        self.maxHealth = self.health

    def __init__(self, name):
        ###################SET LEVEL BASED ON LOCATION
        # get the base entity health used for randomizing in setHealth()
        self.getHealth()
        self.setHealth()
        self.name = name

    # def die(self):
    #     del self

    # Use an attack
    def attack(self, playerObject, playerEntity, enemyObject, windowWidth, attack):
        # if the enemy isnt already attacking
        if enemyObject.state not in self.attackNames:
            # attack with initialization
            attack[0](self, True, playerObject, playerEntity, enemyObject, windowWidth)
        # if the enemy is already attacking
        else:
            # attack without initialization
            self.currentAttack[0](self, False, playerObject, playerEntity, enemyObject, windowWidth)


# Troll template
class troll(enemy):
    armour = 10
    maxArmour = armour
    attackDelay = 50
    attackDelayMax = 50

    # set base health
    def getHealth(self):
        # base is 5 * the troll's level
        self.health = 5 * self.level

    # swing sword and hit the player if in front
    def swing(self, firstFrame, playerObject, playerEntity, enemyObject, windowWidth):
        # if it's the first frame
        if firstFrame:
            # update the graphic object
            enemyObject.changeState("swing")
            # load the first frame
            enemyImage = pygame.image.load("graphics/troll/swing/0.PNG")
            # get the starting position and width
            self.startX = enemyObject.x
            self.startWidth = enemyImage.get_width()
            # compensate for image width
            if enemyObject.face == "r":
                self.startX += self.startWidth
        # if it's not the first frame
        else:
            # the player has not been hit yet
            hit = 0
            # load the player's current frame
            playerImage = pygame.image.load(
                "graphics/player/" + playerObject.state + "/" + str(playerObject.current) + ".PNG")
            # load the enemy's current frame
            enemyImage = pygame.image.load("graphics/troll/swing/" + str(enemyObject.current) + ".PNG")
            # if the enemy is facing left
            if enemyObject.face == "l":
                # check for intersections with the player image on the left of the enemy, with the width the enemy gained
                if self.startX > playerObject.x + playerImage.get_width() > enemyObject.x or self.startX > playerObject.x > enemyObject.x or playerObject.x + playerImage.get_width() > enemyObject.x > playerObject.x:
                    if not (playerObject.state == "block" and enemyObject.face != playerObject.face):
                        hit = 1
                # move back to compensate for width gain
                enemyObject.x = self.startX - (enemyImage.get_width() - self.startWidth)
            # if the enemy is facing right
            else:
                # check for intersections
                if self.startX < playerObject.x < enemyObject.x + enemyImage.get_width() or self.startX < playerObject.x + playerImage.get_width() < enemyObject.x or playerObject.x < enemyObject.x + enemyImage.get_width() < playerObject.x + playerImage.get_width():
                    if not (playerObject.state == "block" and enemyObject.face != playerObject.face):
                        hit = 1
            # if the player was hit
            if hit == 1:
                # deal physical damage
                damage(enemyObject, playerObject, playerEntity, "physical",
                       round(2 * self.level + random.randint(-self.level, self.level)))
                # knock the player back
                playerObject.changeState("knockback")
                playerObject.knockbackDistance = round(windowWidth / 4)
                playerObject.knockbackDistanceMax = playerObject.knockbackDistance
                playerObject.knockbackFace = enemyObject.face
        # if the animation is complete
        if enemyObject.current == enemyObject.totalStates - 1:
            # revert to standing
            enemyObject.changeState("stand")
            # move back to original position
            if enemyObject.face == "l":
                enemyObject.x = self.startX
            else:
                enemyObject.x = self.startX - self.startWidth

    # hit all frontal entities with shield
    # low physical damage, large knockback
    def shieldBash(self, firstFrame, playerObject, playerEntity, enemyObject, windowWidth):
        # if its the first frame
        if firstFrame:
            # update their graphic object
            enemyObject.changeState("shieldBash")
            # load the starting frame
            enemyImage = pygame.image.load("graphics/" + enemyObject.folder + "/shieldBash/0.PNG")
            # get their starting position and width
            self.startX = enemyObject.x
            self.startWidth = enemyImage.get_width()
            # if the enemy is facing right
            if enemyObject.face == "r":
                # add their starting width. This means that hits will be detected from on the right of the player, rather than inside of them.
                self.startX += self.startWidth
        # if it's not the first frame
        else:
            enemyImage = pygame.image.load("graphics/" + enemyObject.folder + "/shieldBash/" + str(enemyObject.current) + ".PNG")
            # check for collisions with player
            hit = 0
            playerImage = pygame.image.load("graphics/player/" + playerObject.state + "/" + str(
                    playerObject.current) + ".PNG")
            # if the player is facing left
            if enemyObject.face == "l":
                # See if the player and the enemy images intersect in any of the space the enemy extended into
                if self.startX > playerObject.x + playerImage.get_width() > enemyObject.x or self.startX > playerObject.x > enemyObject.x or playerObject.x + playerImage.get_width() > enemyObject.x > playerObject.x:
                    # if an intersection is found, the player was hit
                    if not (playerObject.state == "block" and enemyObject.face != playerObject.face):
                        hit = 1
                # move the enemy back to compensate for width gain
                enemyObject.x = self.startX - (enemyImage.get_width() - self.startWidth)
            # if the player is facing right
            else:
                # scan for intersections
                if self.startX < playerObject.x < enemyObject.x + enemyImage.get_width() or self.startX < playerObject.x + playerImage.get_width() < enemyObject.x or playerObject.x < enemyObject.x + enemyImage.get_width() < playerObject.x + playerImage.get_width():
                    if not (playerObject.state == "block" and enemyObject.face != playerObject.face):
                        hit = 1
            # if the enemy was hit
            if hit == 1:
                # deal damage
                damage(enemyObject, playerObject, playerEntity, "physical",
                       round(1.2 * self.level + random.randint(-self.level, self.level)))
                # knock them back
                playerObject.changeState("knockback")
                playerObject.knockbackDistance = round(windowWidth / 4)
                playerObject.knockbackDistanceMax = enemyObject.knockbackDistance
                playerObject.knockbackFace = enemyObject.face
        # if the animation is complete
        if enemyObject.current == enemyObject.totalStates - 1:
            # revert to standing
            enemyObject.changeState("stand")
            # move back to original position
            if enemyObject.face == "l":
                enemyObject.x = self.startX
            else:
                enemyObject.x = self.startX - self.startWidth

    # dash in a line in front of player with your sword. ensure movement keys do not interrupt.
    # high physical damage, low knockback
    # high stamina consumption
    def swordDash(self, firstFrame, playerObject, playerEntity, enemyObject, windowWidth):
        # if it's the first frame
        if firstFrame:
            # change graphic object state
            enemyObject.changeState("swordDash")
            # load the first frame
            enemyImage = pygame.image.load("graphics/" + enemyObject.folder + "/stand/0.PNG")
            # get starting width
            self.startWidth = enemyImage.get_width()
            # reset the move progress
            self.progress = 5
        # if it's not the first frame and the progress is not 0
        else:
            if self.progress > 0:
                # load the current frame
                enemyImage = pygame.image.load("graphics/" + enemyObject.folder + "/swordDash/" + str(enemyObject.current) + ".PNG")
                # Check for collisions with player
                hit = 0
                # load this enemy's current frame
                playerImage = pygame.image.load(
                    "graphics/player/" + playerObject.state + "/" + str(playerObject.current) + ".PNG")
                # if the player is facing left
                if enemyObject.face == "l":
                    # check for intersections in the width the player gained
                    if self.startX > playerObject.x + playerImage.get_width() > enemyObject.x or self.startX > playerObject.x > enemyObject.x or playerObject.x + playerImage.get_width() > enemyObject.x > playerObject.x:
                        if not (playerObject.state == "block" and enemyObject.face != playerObject.face):
                            hit = 1
                # if the player facing right
                else:
                    # check for intersections
                    if self.startX < playerObject.x < enemyObject.x + enemyImage.get_width() or self.startX < playerObject.x + playerImage.get_width() < enemyObject.x or playerObject.x < enemyObject.x + enemyImage.get_width() < playerObject.x + playerImage.get_width():
                        if not (playerObject.state == "block" and enemyObject.face != playerObject.face):
                            hit = 1
                # if the enemy was hit
                if hit == 1:
                    # deal damage
                    damage(enemyObject, playerObject, playerEntity, "physical",
                           round(1.7 * self.level + random.randint(-self.level, self.level)))
                    # knock them back
                    playerObject.changeState("knockback")
                    playerObject.knockbackDistance = round(windowWidth / 15)
                    playerObject.knockbackDistanceMax = playerObject.knockbackDistance
                    playerObject.knockbackFace = enemyObject.face
                    # move the player
                if enemyObject.face == "r":
                    enemyObject.x += round(windowWidth * 5/80)
                else:
                    enemyObject.x -= round(windowWidth * 5/80)
                # take one from the progress
                self.progress -= 1
            else:
                # if progress is done, revert to standing
                enemyObject.changeState("stand")

    # list of all attacks AND the range in which the enemy will ATTEMPT them
    attacks = [[shieldBash, 0, round(windowWidth * 5/24)],[swing, round(windowWidth * 5/24), round(windowWidth / 4)],[swordDash, round(windowWidth / 4), round(windowWidth * 3/5)]]
    # list of all of the attack names
    attackNames = ["shieldBash","swing","swordDash"]


# giant spider template
class spider(enemy):
    armour = 2
    maxArmour = armour

    # initial maxHealth calculation
    def getHealth(self):
        # base is 4 * the spider's level.
        self.health = 4 * self.level


######################################

# Save management

# Check a requested name is valid
def checkName(name):
    # valid characters
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    # maximum name length
    maxLen = 16
    # minimum name length
    minLen = 1
    # check name length
    if not minLen <= len(name) <= maxLen:
        return False, 0

    # check all characters are in the alphabet
    for i in range(len(name)):
        if not name[i] in alphabet:
            return False, 1

    # no errors
    return True, 0


# Get the desired new save name
def getNewGame():
    # TODO: GIVE USER A LIST OF EXISTING SAVES - MAKE A DATABASE?
    newName = input()  # TODO: GET NEW NAME FROM TEXT INPUT
    # Check the name is valid
    valid, error = checkName(newName)
    # give error feedback based on checkName() results
    while not valid:
        if error == 0:
            msg = "Please use between 1 and 15 characters"
        else:
            msg = "Please use only letters, numbers and underscores"
        print(msg)  ########################################################################SHOW ERROR ON SCREEN

    # see if the same already exists
    try:
        open("saves/" + newName, 'r')
    # file not found
    except IOError:
        # name must be valid
        return newName
    # ask for new name if save is found
    print("That save already exists, please try again")  ##########################################SHOW ERROR ON SCREEN
    return ""


# Initialize a new game
# not sure if I'll need to use this one.
def newGame(name):
    pass


# Get the desired save name to load
# TODO: CHANGE! GIVE USER A LIST OF EXISTING SAVES - MAKE A DATABASE?
# def getLoadGame():
#  name = input() #####################################################GET NEW NAME FROM TEXT INPUT
#    valid, error = checkName(newName)
#   while valid == False:
#     if error == 0:
#       msg = "Please use between 1 and 15 characters"
#     else:
#       msg = "Please use only letters, numbers and underscores"
#     print(msg) ########################################################################SHOW ERROR ON SCREEN
#
#   try:
#     open("saves/" + name, 'r')
#   except IOError:
#     print("That save does not exist, please try again") ##########################################SHOW ERROR ON SCREEN
#     return
#   return name

# Load a save file into the game by reading
def loadGame():
    pass


# Save game data to a file. Inefficient.
def saveGame():
    # open the file
    f = open("saves/" + player.name, "w")
    # get all data to be saved
    data = [player.health, player.maxHealth, player.name, player.healthPot, player.classType]
    # If the player is a mage, add mana to the save.
    if player.classType == "Mage":
        data.append(player.mana)
    # run through data to be saved, writing to the file
    for i in range(len(data)):
        f.write(str(data[i]) + "\n")
    # save and close the file
    f.close()
