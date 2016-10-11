from objects import *
backdrop = "graphics/forest.png"

##player = image("image", "player", 80, 490, False, True, "graphics/player.jpg")
player = entity("entity","player",80,475,False,True,[["walk",3],["stand",1],["jump",1],["drop",1],["knockback",1],["swing",5],["shieldBash",5],["swordDash",1]],"stand","player","r")
enemy1 = entity("entity","enemy1",300,475,False,True,[["walk",1],["stand",1],["jump",1],["drop",1],["knockback",1],["swing",5]],"stand","troll","l")
#add to sceneObjects
sceneObjects = [player,enemy1]
