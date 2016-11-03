# import graphic objects
from objects import *
# used to store and transfer all objects to be loaded
sceneObjects = []


def init(entities,windowWidth,windowHeight):
    # find the player and enemy game objects, these are needed for assigning health bars
    for currentEntity in entities:
        if currentEntity.name == "player":
            playerEntity = currentEntity
        elif currentEntity.name == "enemy1":
            enemy1Entity = currentEntity
        elif currentEntity.name == "enemy2":
            enemy2Entity = currentEntity
        elif currentEntity.name == "enemy3":
            enemy3Entity = currentEntity

    # create the player graphic object as an entity
    player = entity("player", round(windowWidth / 10), round(windowHeight / 2), False, True,
                    [["walk", 4], ["stand", 4], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],
                     ["shieldBash", 7], ["swordDash", 1],["pant", 4],["block",1]], "stand", "player", "r")
    # assign the player's healthbar
    playerHealth = healthBar("playerHealth", playerEntity, player)
    # Assign the player's staminaBar
    playerStamina = staminaBar("playerStamina", playerEntity, player)
    # create the enemy1 graphic object as an entity
    enemy1 = entity("enemy1", round(windowWidth / 10 * 7), round(windowHeight / 2), False, True,
                    [["walk", 4], ["stand", 4], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],["shieldBash", 7], ["swordDash", 1],["pant", 4]], "stand",
                    "troll", "l")
    # assign enemy1's healthbar
    enemy1Health = healthBar("enemy1Health", enemy1Entity, enemy1)
    # the counter for the kills the player has
    killCount = killCounter("killCount",playerEntity)
    # animation to display if the player attempts an action without the appropriate stamina
    noStamina = animation("noStamina",round(windowWidth / 2),playerStamina.y,False,True,"noStamina",0,4)

##    # create the enemy1 graphic object as an entity
##    enemy2 = entity("enemy2", round(windowHeight / 10 * 8), round(windowHeight / 2), False, True,
##                    [["walk", 4], ["stand", 4], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],["shieldBash", 7], ["swordDash", 1],["pant", 4]], "stand",
##                    "troll", "l")
##    # assign enemy1's healthbar
##    enemy2Health = healthBar("enemy2Health", enemy2Entity, enemy2)
##
##    # create the enemy1 graphic object as an entity
##    enemy3 = entity("enemy3", round(windowHeight / 10 * 9), round(windowHeight / 2), False, True,
##                    [["walk", 4], ["stand", 4], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],["shieldBash", 7], ["swordDash", 1],["pant", 4]], "stand",
##                    "troll", "l")
##    # assign enemy1's healthbar
##    enemy3Health = healthBar("enemy3Health", enemy3Entity, enemy3)
    
    # return all of the objects
##    return [player, playerHealth, playerStamina, enemy1, enemy1Health, enemy2, enemy2Health, enemy3, enemy3Health, killCount, noStamina]
##    return [player, playerHealth, playerStamina, enemy1, enemy1Health, enemy2, enemy2Health, killCount, noStamina]
    return [player, playerHealth, playerStamina, enemy1, enemy1Health, killCount, noStamina]
