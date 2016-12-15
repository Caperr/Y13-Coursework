# import all graphical objects
from objects import *
# the list of all of the objects in the scene
sceneObjects = []

# initialize graphical objects based on window size
def init(windowWidth,windowHeight):
    # the button for a new game. It is clickable
    newGame = rectangle("newGame", round(windowWidth / 2), round(windowHeight / 4), True, True, round(windowWidth / 4), round(windowHeight / 4), red)
    # the button to load a game. It is clickable
    # loadGame = rectangle("loadGame", round(windowWidth * 3/8), round(windowHeight * 27/60), True, True, round(windowWidth / 4), round(windowHeight / 6), green)
    # the button to quit the game. It is clickable
    quitGame = rectangle("quitGame", round(windowWidth / 2), round(windowHeight * 8/15), True, True, round(windowWidth / 4), round(windowHeight / 6), blue)
    # the text for a new game.
    newGameText = text("newGameText", 0, 0, False, True, "New Game", white, True, 25)
    # centre it in the newGame button
    newGameText.centreText((newGame.x + round(newGame.width / 2), newGame.y + round(newGame.height / 2)))
    # # the text to load a game.
    # loadGameText = text("loadGameText", 0, 0, False, True, "Load Game", white, True, 25)
    # # centre it in the load game button
    # loadGameText.centreText((loadGame.x + round(loadGame.width/2), loadGame.y + round(loadGame.height/2)))
    # the text to quit the game.
    quitGameText = text("quitGameText", 0, 0, False, True, "Quit Game", white, True, 25)
    # centre it in the quit game button
    quitGameText.centreText((quitGame.x + round(quitGame.width / 2), quitGame.y + round(quitGame.height / 2)))
    # return all of the objects
    controls = rectangle("controls", round(windowWidth / 2), round(windowHeight * 11/15), True, True, round(windowWidth / 4), round(windowHeight / 8), green)
    controlsText = text("controlsText", 0, 0, False, True, "Controls", white, True, 25)
    leaderboard = rectangle("leaderboard", round(windowWidth / 2), round(windowHeight / 10), True, True, round(windowWidth / 4), round(windowHeight / 8), green)
    leaderboardText = text("leaderboardText", 0, 0, False, True, "Leaderboard", white, True, 25)
    leaderboardText.centreText((leaderboard.x + round(leaderboard.width / 2), leaderboard.y + round(leaderboard.height / 2)))
    # centre it in the quit game button
    controlsText.centreText((controls.x + round(controls.width / 2), controls.y + round(controls.height / 2)))
    playerAnimation = animation("playerAnimation",round(windowWidth / 8),round(windowWidth * 2/5),False,True,"player/stand",1,4)
    return [newGame, quitGame,newGameText,quitGameText,playerAnimation,controls,controlsText,leaderboard,leaderboardText]
