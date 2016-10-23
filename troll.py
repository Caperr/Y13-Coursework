def react(enemyObject, entities, playerObject, playerEntity, windowWidth):
    for entity in entities:
        if entity.name == enemyObject.name:
            enemyEntity = entity
            break

    if not (enemyObject.state in ["jump", "drop,knockback"] or enemyObject.state in enemyEntity.attackNames):
        if playerObject.x > enemyObject.x:
            enemyEntity.distance = playerObject.x - enemyObject.x
            enemyObject.face = "r"
        else:
            enemyEntity.distance = enemyObject.x - playerObject.x
            enemyObject.face = "l"
        for attack in enemyEntity.attacks:
            if attack[1] <= enemyEntity.distance <= attack[2]:
                enemyEntity.attack(playerObject, playerEntity, enemyObject, windowWidth, attack)
                enemyEntity.currentAttack = attack
                break
