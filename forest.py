from objects import *
backdrop = "graphics/forest.png"

##player = image("image", "player", 80, 490, False, True, "graphics/player.jpg")
player = entity("entity","player",80,300,False,True,[["walk",4],["stand",1],["jump",1],["drop",1],["knockback",1],["swing",7],["shieldBash",7],["swordDash",1]],"stand","player","r")
enemy1 = entity("entity","enemy1",450,475,False,True,[["walk",4],["stand",1],["jump",1],["drop",1],["knockback",1],["swing",7]],"stand","troll","l")
#add to sceneObjects
sceneObjects = [player,enemy1]
