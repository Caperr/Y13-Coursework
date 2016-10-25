# mport all graphical objects
from objects import *
# the list of all of the objects in the scene
sceneObjects = []

# initialize graphical objects based on window size
def init(windowWidth,windowHeight):
    # the button for a new game. It is clickable
    newGame = rectangle("newGame", round(windowWidth * 3/8), round(windowHeight / 4), True, True, round(windowWidth / 4), round(windowHeight / 6), red)
    # the button to load a game. It is clickable
    loadGame = rectangle("loadGame", round(windowWidth * 3/8), round(windowHeight * 27/60), True, True, round(windowWidth / 4), round(windowHeight / 6), green)
    # the button to quit the game. It is clickable
    quitGame = rectangle("quitGame", round(windowWidth * 3/8), round(windowHeight * 39/60), True, True, round(windowWidth / 4), round(windowHeight / 12), blue)
    # the text for a new game.
    newGameText = text("newGameText", 0, 0, False, True, "New Game", white, True)
    # centre it in the newGame button
    newGameText.centreText((newGame.x + round(newGame.width / 2), newGame.y + round(newGame.height / 2)))
    # the text to load a game.
    loadGameText = text("loadGameText", 0, 0, False, True, "Load Game", white, True)
    # centre it in the load game button
    loadGameText.centreText((loadGame.x + round(loadGame.width/2), loadGame.y + round(loadGame.height/2)))
    # the text to quit the game.
    quitGameText = text("quitGameText", 0, 0, False, True, "Quit Game", white, True)
    # centre it in the quit game button
    quitGameText.centreText((quitGame.x + round(quitGame.width / 2), quitGame.y + round(quitGame.height / 2)))
    # return all of the objects
    return [newGame, loadGame, quitGame,newGameText,loadGameText,quitGameText]