from objects import *

backdrop = "graphics/background.png"
sceneObjects = []


def init(entities):
    for currentEntity in entities:
        if currentEntity.name == "player":
            playerEntity = currentEntity
        elif currentEntity.name == "enemy1":
            enemy1Entity = currentEntity
    player = entity("player", 80, 300, False, True,
                    [["walk", 4], ["stand", 1], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7],
                     ["shieldBash", 7], ["swordDash", 1]], "stand", "player", "r")
    playerHealth = healthBar("playerHealth", playerEntity, player)
    enemy1 = entity("enemy1", 450, 475, False, True,
                    [["walk", 4], ["stand", 1], ["jump", 1], ["drop", 1], ["knockback", 1], ["swing", 7]], "stand",
                    "troll", "l")
    enemy1Health = healthBar("enemy1Health", enemy1Entity, enemy1)
    # add to sceneObjects
    return [player, enemy1, playerHealth, enemy1Health]
