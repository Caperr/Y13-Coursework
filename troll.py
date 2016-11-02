# the troll's "AI" file - its reactions and behaviour
import random

def react(enemyObject, enemyEntity, playerObject, playerEntity, windowWidth):
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

        if enemyEntity.currentAttackID is None:
            enemyEntity.currentAttackID = random.randint(0, len(enemyEntity.attackNames) - 1)
            originalAttack = enemyEntity.currentAttackID
            while enemyEntity.distance < enemyEntity.attacks[enemyEntity.currentAttackID][1]:
                if enemyEntity.currentAttackID == -1:
                    enemyEntity.currentAttackID = originalAttack
                    break
                enemyEntity.currentAttackID -= 1
            # enemyEntity.currentAttackID = 2

        if enemyEntity.attackDelay > 0:
            # take one away
            enemyEntity .attackDelay -= 1
        # if the attack delay is 0
        elif enemyEntity.currentAttackID is not None:
            if enemyEntity.attacks[enemyEntity.currentAttackID][2] >= enemyEntity.distance >= enemyEntity.attacks[enemyEntity.currentAttackID][1]:
                # read through the list of attacks
                enemyEntity.currentAttack = enemyEntity.attacks[enemyEntity.currentAttackID]
                # execute the attack
                enemyEntity.attack(playerObject, playerEntity, enemyObject, windowWidth, enemyEntity.currentAttack)
                # reset attack delay
                enemyEntity.attackDelay = enemyEntity.attackDelayMax
                # update the enemy's current attack variable
                enemyEntity.currentAttackID = None
                # break from the loop, no more scanning needs to be done.
                return

        if (enemyEntity.attacks[enemyEntity.currentAttackID][2] < enemyEntity.distance or enemyEntity.distance < enemyEntity.attacks[enemyEntity.currentAttackID][1]):
            if enemyObject.state != "walk":
                enemyObject.changeState("walk")
            if enemyEntity.distance < enemyEntity.attacks[enemyEntity.currentAttackID][1]:
                if enemyObject.face == "l":
                    enemyObject.face = "r"
                else:
                    enemyObject.face = "l"

        if enemyEntity.attacks[enemyEntity.currentAttackID][1] <= enemyEntity.distance <= enemyEntity.attacks[enemyEntity.currentAttackID][2]:
            enemyObject.changeState("stand")
