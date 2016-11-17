# TODO: Keep a record of the player's attacks and react. e.g swordDash if player is constantly shieldBashing
# TODO: Randomly choose whether to block a player attack or not
# TODO: Add difficulty setting -> e.g increase base troll difficulty, FPS, number of trolls

# the troll's "AI" file - its reactions and behaviour
import random

playerAttacks = []

# This code taken from Max Shawabkeh on stackoverflow.com
# source: http://stackoverflow.com/questions/2130016/splitting-a-list-of-arbitrary-size-into-only-roughly-n-equal-parts
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out
# end code by Max Shawabkeh


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

        if len(playerAttacks) > 2:
            for attackNum in range(len(playerAttacks[0:-3])):
                if playerEntity.attackNames[attackNum] == playerEntity.attackNames[attackNum + 1] == playerEntity.attackNames[attackNum + 2]:
                    splitAttacks = chunkIt(playerEntity.attackNames,3)
                    
                        

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
