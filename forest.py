# import graphic objects
from objects import *
# used to store and transfer all objects to be loaded
sceneObjects = []


def init(entities,windowWidth,windowHeight,numEnemies):
    sceneObjects = []
    # find the player and enemy game objects, these are needed for assigning health bars
    for currentEntity in entities:
        if currentEntity.name == "player":
            playerEntity = currentEntity

    # create the player graphic object as an entity
    player = entity("player", round(windowWidth / 10), round(windowHeight / 2), False, True,
                    [["walk", 9], ["stand", 9], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],
                     ["shieldBash", 7], ["swordDash", 1],["pant", 5],["block",1]], "stand", "player", "r")
    # assign the player's healthbar
    playerHealth = healthBar("playerHealth", playerEntity, player)
    # Assign the player's staminaBar
    playerStamina = staminaBar("playerStamina", playerEntity, player)
    for i in range(numEnemies):
        # create the enemy1 graphic object as an entity
        sceneObjects.append(entity("enemy" + str(i + 1), round(windowWidth / 10 * 7), round(windowHeight / 2) + (2 * i), False, True,
                        [["walk", 8], ["stand", 6], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 8],["shieldBash", 8], ["swordDash", 1],["pant", 4]], "stand",
                        "troll", "l"))
        # assign enemy1's healthbar
        for n in entities:
            if n.name == sceneObjects[-1].name:
                sceneObjects.append(healthBar("enemy" + str(i + 1) + "Health", n, sceneObjects[-1]))
                break
    # the counter for the kills the player has
    killCount = killCounter("killCount",playerEntity)
    # animation to display if the player attempts an action without the appropriate stamina
    noStamina = animation("noStamina",round(windowWidth / 2),playerStamina.y,False,True,"noStamina",0,4)
    # Text to display when the game is paused
    pauseText = text("pauseText",round(windowWidth * 2/5),round(windowHeight/2),False,False,"Game paused",blue,True,50)

    other = [player, playerHealth, playerStamina, killCount, noStamina, pauseText]

    for i in other:
        sceneObjects.append(i)
    return sceneObjects
