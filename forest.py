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
    # create the player graphic object as an entity
    player = entity("player", round(windowWidth / 10), round(windowHeight / 2), False, True,
                    [["walk", 4], ["stand", 4], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],
                     ["shieldBash", 7], ["swordDash", 1],["pant", 4],["block",1]], "stand", "player", "r")
    # assign the player's healthbar
    playerHealth = healthBar("playerHealth", playerEntity, player)
    # Assign the player's staminaBar
    playerStamina = staminaBar("playerStamina", playerEntity, player)
    # create the enemy1 graphic object as an entity
    enemy1 = entity("enemy1", round(windowHeight / 10 * 6), round(windowHeight / 2), False, True,
                    [["walk", 4], ["stand", 4], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],["shieldBash", 7], ["swordDash", 1],["pant", 4]], "stand",
                    "troll", "l")
    # assign enemy1's healthbar
    enemy1Health = healthBar("enemy1Health", enemy1Entity, enemy1)
    # the counter for the kills the player has
    killCount = killCounter("killCount",playerEntity)
    # animation to display if the player attempts an action without the appropriate stamina
    noStamina = animation("noStamina",round(windowWidth / 2),playerStamina.y,False,True,"noStamina",0,4)
    # return all of the objects
    return [player, enemy1, playerHealth, playerStamina, enemy1Health, killCount, noStamina]
