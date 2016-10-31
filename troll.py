# the troll's "AI" file - its reactions and behaviour
import random

def react(enemyObject, entities, playerObject, playerEntity, windowWidth):
    # find the troll's game object in the entities list
    for entity in entities:
        if entity.name == enemyObject.name:
            enemyEntity = entity
            break

    # if the troll is not disabled
    if not (enemyObject.state in ["jump", "drop","knockback"] or enemyObject.state in enemyEntity.attackNames):
        # if the player is on the right of the enemy
        if playerObject.x > enemyObject.x:
            # get the distance between the enemy and the player
            enemyEntity.distance = playerObject.x - enemyObject.x
            # face right
            enemyObject.face = "r"
        # if the player is on the left of the enemy
        else:
            # get the distance between the enemy and the player
            enemyEntity.distance = enemyObject.x - playerObject.x
            # face left
            enemyObject.face = "l"
            # if the attack delay isnt 0
        if enemyEntity.attackDelay > 0:
            # take one away
            enemyEntity .attackDelay -= 1
            # choose the next attack to execute
            if enemyEntity.currentAttackID == None:
                enemyEntity.currentAttackID = random.randint(0,len(enemyEntity.attackNames))
                while x < enemyEntity.attacks[enemyEntity.currentAttackID][1]:
                    enemyEntity.currentAttackID -= 1
                    if enemyEntity.currentAttackID == -1:
                        enemyEntity.currentAttackID = 0
                        break
        # if the attack delay is 0
        else:
            if enemyEntity.currentAttackID == None:
                enemyEntity.currentAttackID = random.randint(0,len(enemyEntity.attackNames))
                while x < enemyEntity.attacks[enemyEntity.currentAttackID][1]:
                    enemyEntity.currentAttackID -= 1
                    if enemyEntity.currentAttackID == -1:
                        enemyEntity.currentAttackID = 0
                        break
            if not (enemyEntity.maxDistance < enemyEntity.distance or enemyEntity.distance > enemyEntity.minDistance):
                # read through the list of attacks
                attack = enemyEntity.attacks[enemyEntity.currentAttackID]
                # execute the attack
                enemyEntity.attack(playerObject, playerEntity, enemyObject, windowWidth, attack)
                # update the enemy's current attack variable
                enemyEntity.currentAttack = attack
                # break from the loop, no more scanning needs to be done.
                return
                
        if (enemyEntity.maxDistance < enemyEntity.distance or enemyEntity.distance > enemyEntity.minDistance) and enemyObject.state != "walk":
            enemyObject.changeState("walk")

        if enemyEntity.minDistance <= enemyEntity.distance <= enemyEntity.maxDistance:
            enemyObject.changeState("stand")
