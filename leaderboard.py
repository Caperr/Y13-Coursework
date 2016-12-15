from objects import *

sceneObjects = []

def init(scores):
    sceneObjects = [text("none", 80, 60, False, True,"", black, True, 40)]
    for score in range(len(scores)):
        sceneObjects.append(text("score" + str(score + 1), 80, sceneObjects[-1].y + 30, False, True,str(score + 1) + ": " + scores[score][0] + " - " + str(scores[score][1]), black, True, 40))
    sceneObjects.pop(0)

    sceneObjects.append(rectangle("playGame", 420, 130, True, True,180,80, green))
    sceneObjects.append(text("playGameText", 0, 0, False, True, "Main Menu", white, True, 45))
    sceneObjects[-1].centreText((sceneObjects[-2].x + round(sceneObjects[-2].width / 2), sceneObjects[-2].y + round(sceneObjects[-2].height / 2)))
    sceneObjects.append(rectangle("quitGame", 420, 220, True, True, 180, 80, red))
    sceneObjects.append(text("quitGameText", 0, 0, False, True, "Quit Game", white, True, 45))
    sceneObjects[-1].centreText((sceneObjects[-2].x + round(sceneObjects[-2].width / 2), sceneObjects[-2].y + round(sceneObjects[-2].height / 2)))

    return sceneObjects
