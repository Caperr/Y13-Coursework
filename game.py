#Imports
import time
import random
import pygame
import objects

#list of all enemy instances
enemies = []

def damage(giverObject, recieverObject, recieverEntity, damType, amount):
  print(giverObject.name,"dealt",amount,damType,"damage to",recieverObject.name)

##############################

#Class templates
class classes():
  #player health
  health = 20
  #Max player health
  maxHealth = 20
  #Armour - % physical damage reduction
  armour = 0
  #Maximum armour. I'll need this if I have an armour boosting spell etc
  maxArmour = 0
  #Player name. used in game and also in save management
  name = ''
  #How many health potions the player has
  healthPot = 0
  #what class they are
  classType = ""
  #Stamina determines how fast the player can use physical moves, such as dodging, hitting, running, etc.
  #When completely depleated, the player is immobilized to pant for a small amount of time to allow stamina to recharge.
  #Stamina is recharged naturally over time, or can be recharged instantly with sugary food.
  stamina = 10
  #Player walking speed
  speed = 20
  #Player jump height
  jumpHeight = 100

  #initialize player
  def init(self,name):
    #Set the player's name
    self.name = name

  #Dodge an incoming attack. Since attack hit is based solely on proximity, all it needs to do is move the player.
  def dodge(self):
    pass

  def levelUp(self):
    pass
  #update BY ADDING (NOT BY SETTING (MAYBE??????)) armour, maxArmour, health, maxHealth, etc based on level
  
#Class template for a knight
class knight(classes):
  classType = "Knight"
  armour = 10
  maxArmour = armour

  def __init__(self,name):
    self.init(name)

  #hit all frontal entities with your sword
  #medium physical damage, small knockback
  #medium stamina consumption
  def hit(self):
    pass

  #hit all frontal entities with your shield
  #low physical damage, large knockback
  #medium stamina consumption
  def shieldBash(self):
    pass

  #dash in a line in front of player with your sword. ensure movement keys do not interrupt.
  #high physical damage, low knockback
  #high stamina consumption
  def swordDash(self):
    pass

  #block all frontal attacks (not sure if it's only physical or not)
  #low stamina consumption
  #on 0 stamina, play a block break animation and take damage
  #may stun based on timing? not sure.
  def block(self):
    pass
  
#Mage template
class mage(classes):
  armour = 5
  maxArmour = armour
  #similar concept to stamina, but for casting spells.
  mana = 100
  classType = "Mage"
  
#archer template
class archer(classes):
  armour = 3
  maxArmour = armour
  classType = "Archer"
  
#rogue template
class rogue(classes):
  armour = 3
  maxArmour = armour
  classType = "Rogue"

###############################

#Enemy templates
class enemy():
  #entity name. used for linking this class and graphics class.
  name = ""
  #entity health
  health = 0
  #max entity health
  maxHealth = 0
  #armour
  armour = 0
  maxArmour = 0
  #entity level
  level = 1
  #Walking speed
  speed = 10
  #Jump Height
  jumpHeight = 30
  #The delay, in frames, between attacks
  attackDelay = 0
  #last attack scanned
  currentAttack = "none"
  #current distance from the player
  distance = 0

  #same as player dodge
  def dodge(self):
    pass

  #set entity health and maxhealth
  def setHealth(self):
    #slightly randomize entity health and maxhealth based on a base, class specific value, and also based on level.
    self.health = round(self.health + (((random.randint(0,5)) / 10) * self.level))
    self.health = random.randint(self.health - round(0.3 * self.level), self.health + round(0.3 * self.level))
    self.maxHealth = self.health

  def __init__ (self, name):
    ###################SET LEVEL BASED ON LOCATION
    ###################
    #get the base entity health used for randomizing in setHealth()
    self.getHealth()
    self.setHealth()
    self.name = name

##  def die(self):
##    del self

  #Use an attack based on range
  def attack(self,playerObject,playerEntity,enemyObject,windowWidth):
    if not enemyObject.state in self.attackNames:
      if playerObject.x > enemyObject.x:
        self.distance = playerObject.x - enemyObject.x
        enemyObject.face = "r"
      else:
        self.distance = enemyObject.x - playerObject.x
        enemyObject.face = "l"
      if self.attackDelay > 0:
##        print(self.attackDelay)
        self.attackDelay -= 1
      else:
        for attack in self.attacks:
          if attack[1] <= self.distance <= attack[2]:
            attack[0](self,0,playerObject,playerEntity,enemyObject,attack,windowWidth)
            self.currentAttack = attack
            break
    else:
      self.currentAttack[0](self,1,playerObject,playerEntity,enemyObject,self.currentAttack,windowWidth)

#Troll template
class troll(enemy):
  armour = 10
  maxArmour = armour
  attackDelay = 0
  attackDelayMax = 50
  #temporary variables for use in swing
  startX = 0
  startWidth = 0
  
  #set base health
  def getHealth(self):
    #base is 5 * the troll's level
    self.health = 5 * self.level

  def swing(self,act,playerObject,playerEntity,enemyObject,attack,windowWidth):
    if act == 0:
      enemyObject.changeState("swing")
      enemyImage = pygame.image.load("graphics/troll/swing/0.PNG")
      self.startX = enemyObject.x
      self.startWidth = enemyImage.get_width()
      if enemyObject.face == "r":
        self.startX += self.startWidth
##      else:
##        enemyImage = pygame.image.load("graphics/troll/swing/1.PNG")
##        enemyObject.x = self.startX - (enemyImage.get_width() - self.startWidth)
    else:
##      if attack[1] <= self.distance <= attack[2]:
      hit = 0
      playerImage = pygame.image.load("graphics/player/" + playerObject.state + "/" + str(playerObject.current) + ".PNG")
      enemyImage = pygame.image.load("graphics/troll/swing/" + str(enemyObject.current - 1) + ".PNG")
      if enemyObject.face == "l":
        if self.startX > playerObject.x + playerImage.get_width() > enemyObject.x or self.startX > playerObject.x > enemyObject.x or playerObject.x + playerImage.get_width() > enemyObject.x > playerObject.x:
          hit = 1
        print("UPDATE##############################")
        enemyObject.x = self.startX - (enemyImage.get_width() - self.startWidth)
        print("startX",self.startX)
        print("width",enemyImage.get_width())
        print("startWidth",self.startWidth)
        print("difference",enemyImage.get_width() - self.startWidth)
        print("final",self.startX - (enemyImage.get_width() - self.startWidth),"\n")
      else:
        if self.startX < playerObject.x < enemyObject.x + enemyImage.get_width() or self.startX < playerObject.x + playerImage.get_width() < enemyObject.x or playerObject.x < enemyObject.x + enemyImage.get_width() < playerObject.x + playerImage.get_width():
          hit = 1
      if hit == 1:
        damage(enemyObject,playerObject,playerEntity, "physical", (2 * self.level + random.randint(-self.level,self.level)))
        playerObject.changeState("knockback")
        playerObject.knockbackDistance = round(windowWidth/4)
        playerObject.knockbackDistanceMax = playerObject.knockbackDistance
        playerObject.knockbackFace = enemyObject.face
    if enemyObject.current == enemyObject.totalStates - 1:
      enemyObject.changeState("stand")
      self.attackDelay = self.attackDelayMax
      if enemyObject.face == "l":
        enemyObject.x = self.startX
      else:
        enemyObject.x = self.startX - self.startWidth

  attacks = [[swing,0,220]]
  attackNames = ["swing"]
    
#giant spider template
class spider(enemy):
  armour = 2
  maxArmour = armour
  def getHealth(self):
    #base is 4 * the spider's level.
    self.health = 4 * self.level

######################################

#Save management

#Check a requested name is valid
def checkName(name):
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
  #check name length
  if not 0 < len(name) < 16:
    return False, 0
  
  #check all characters are in the alphabet
  for i in range(len(name)):
    if not name[i] in alphabet:
      return False, 1
    
  #no errors
  return True, 0

#Get the desired new save name
def getNewGame():
  ################################GIVE USER A LIST OF EXISTING SAVES - MAKE A DATABASE?
  newName = input() #####################################################GET NEW NAME FROM TEXT INPUT
  #Check the name is valid
  valid, error = checkName(newName)
  #give error feedback based on checkName() results
  while valid == False:
    if error == 0:
      msg = "Please use between 1 and 15 characters"
    else:
      msg = "Please use only letters, numbers and underscores"
    print(msg) ########################################################################SHOW ERROR ON SCREEN

  #see if the same already exists
  try:
    open("saves/" + newName, 'r')
  #file not found
  except IOError:
    #name must be valid
    return newName
  #ask for new name if save is found
  print("That save already exists, please try again") ##########################################SHOW ERROR ON SCREEN
  return ""

#Initialize a new game
#not sure if I'll need to use this one.
def newGame(name):
  pass

#Get the desired save name to load
##############################CHANGE! GIVE USER A LIST OF EXISTING SAVES - MAKE A DATABASE?
##def getLoadGame():
##  name = input() #####################################################GET NEW NAME FROM TEXT INPUT
##  valid, error = checkName(newName)
##  while valid == False:
##    if error == 0:
##      msg = "Please use between 1 and 15 characters"
##    else:
##      msg = "Please use only letters, numbers and underscores"
##    print(msg) ########################################################################SHOW ERROR ON SCREEN
##
##  try:
##    open("saves/" + name, 'r')
##  except IOError:
##    print("That save does not exist, please try again") ##########################################SHOW ERROR ON SCREEN
##    return
##  return name

#Load a save file into the game by reading
def loadGame():
  pass

#Save game data to a file. Inefficient.
def saveGame():
  #open the file
  f = open("saves/" + player.name, "w")
  #get all data to be saved
  data = [player.health,player.maxHealth,player.name,player.healthPot,player.classType]
  #If the player is a mage, add mana to the save.
  if player.classType == "Mage":
    data.append(player.mana)
  #run through data to be saved, writing to the file
  for i in range(len(data)):
    f.write(str(data[i]) + "\n")
  #save and close the file
  f.close()
  

##################################

#Game








