# import all graphical objects
from objects import *
# the list of all of the objects in the scene
sceneObjects = []

# initialize graphical objects based on window size
def init(windowWidth,windowHeight):
    # the button for a new game. It is clickable
    newGame = rectangle("newGame", round(windowWidth / 2), round(windowHeight / 4), True, True, round(windowWidth / 4), round(windowHeight / 4), red)
    # the button to quit the game. It is clickable
    quitGame = rectangle("quitGame", round(windowWidth / 2), round(windowHeight * 8/15), True, True, round(windowWidth / 4), round(windowHeight / 6), blue)
    # the text for a new game.
    newGameText = text("newGameText", 0, 0, False, True, "New Game", white, True, 25)
    # centre it in the newGame button
    newGameText.centreText((newGame.x + round(newGame.width / 2), newGame.y + round(newGame.height / 2)))
    # the text to quit the game.
    quitGameText = text("quitGameText", 0, 0, False, True, "Quit Game", white, True, 25)
    # centre it in the quit game button
    quitGameText.centreText((quitGame.x + round(quitGame.width / 2), quitGame.y + round(quitGame.height / 2)))
    # The controls and leaderboard buttons, and their text
    controls = rectangle("controls", round(windowWidth / 2), round(windowHeight * 11/15), True, True, round(windowWidth / 4), round(windowHeight / 8), green)
    controlsText = text("controlsText", 0, 0, False, True, "Controls", white, True, 25)
    leaderboard = rectangle("leaderboard", round(windowWidth / 2), round(windowHeight / 10), True, True, round(windowWidth / 4), round(windowHeight / 8), green)
    leaderboardText = text("leaderboardText", 0, 0, False, True, "Leaderboard", white, True, 25)
    leaderboardText.centreText((leaderboard.x + round(leaderboard.width / 2), leaderboard.y + round(leaderboard.height / 2)))
    controlsText.centreText((controls.x + round(controls.width / 2), controls.y + round(controls.height / 2)))
    # The animated standing player
    playerAnimation = animation("playerAnimation",round(windowWidth / 8),round(windowWidth * 2/5),False,True,"player/stand",1,4)
    # Return all objects
    return [newGame, quitGame,newGameText,quitGameText,playerAnimation,controls,controlsText,leaderboard,leaderboardText]
