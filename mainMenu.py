from objects import *

backdrop = ""

newGame = rectangle("rectangle", "newGame", 300, 150, True, False, 200, 100, red)
loadGame = rectangle("rectangle", "loadGame", 300, 270, True, False, 200, 100, green)
quitGame = rectangle("rectangle", "quitGame", 300, 390, True, False, 200, 50, blue)

# newGameText = text("text", "newGameText", 0, 0, False, True, "New Game", white, True)
# newGameText.centreText((newGame.x + round(newGame.width/2), newGame.y + round(newGame.height/2)))
# ^^^Add to sceneObjects

sceneObjects = [newGame, loadGame, quitGame]
