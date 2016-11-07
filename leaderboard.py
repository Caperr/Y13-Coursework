from objects import *

sceneObjects = []

def init(scores):
    topScores1 = topScores2 = topScores3 = topScores4 = topScores5 = topScores6 = topScores7 = topScores8 = topScores9 = topScores10 = ""
    if len(scores) > 0:
        topScores1 = "1: " + scores[0][0] + " - " + str(scores[0][1])
    if len(scores) > 1:
        topScores2 = "2: " + scores[1][0] + " - " + str(scores[1][1])
    if len(scores) > 2:
        topScores3 = "3: " + scores[2][0] + " - " + str(scores[2][1])
    if len(scores) > 3:
        topScores4 = "4: " + scores[3][0] + " - " + str(scores[3][1])
    if len(scores) > 4:
        topScores5 = "5: " + scores[4][0] + " - " + str(scores[4][1])
    if len(scores) > 5:
        topScores6 = "6: " + scores[5][0] + " - " + str(scores[5][1])
    if len(scores) > 6:
        topScores7 = "7: " + scores[6][0] + " - " + str(scores[6][1])
    if len(scores) > 7:
        topScores8 = "8: " + scores[7][0] + " - " + str(scores[7][1])
    if len(scores) > 8:
        topScores9 = "9: " + scores[8][0] + " - " + str(scores[8][1])
    if len(scores) > 9:
        topScores10 = "10: " + scores[9][0] + " - " + str(scores[9][1])

    line1 = text("line1", 80, 90, False, True, topScores1, black, True, 40)
    line2 = text("line1", 80, line1.y + 30, False, True, topScores2, black, True, 40)
    line3 = text("line1", 80, line2.y + 30, False, True, topScores3, black, True, 40)
    line4 = text("line1", 80, line3.y + 30, False, True, topScores4, black, True, 40)
    line5 = text("line1", 80, line4.y + 30, False, True, topScores5, black, True, 40)
    line6 = text("line1", 80, line5.y + 30, False, True, topScores6, black, True, 40)
    line7 = text("line1", 80, line6.y + 30, False, True, topScores7, black, True, 40)
    line8 = text("line1", 80, line7.y + 30, False, True, topScores8, black, True, 40)
    line9 = text("line1", 80, line8.y + 30, False, True, topScores9, black, True, 40)
    line10 = text("line1", 80, line9.y + 30, False, True, topScores10, black, True, 40)
    playGame = rectangle("playGame", 420, 130, True, True,180,80, green)
    playGameText = text("playGameText", 0, 0, False, True, "play again", white, True, 45)
    playGameText.centreText((playGame.x + round(playGame.width / 2), playGame.y + round(playGame.height / 2)))
    quitGame = rectangle("quitGame", 420, 220, True, True, 180, 80, red)
    quitGameText = text("quitGameText", 0, 0, False, True, "quit game", white, True, 45)
    quitGameText.centreText((quitGame.x + round(quitGame.width / 2), quitGame.y + round(quitGame.height / 2)))

    return [playGame,playGameText,quitGame,quitGameText,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]