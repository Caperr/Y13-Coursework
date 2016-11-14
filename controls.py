# import all graphical objects
from objects import *
# the list of all of the objects in the scene
sceneObjects = []

# initialize graphical objects based on window size
def init(windowWidth,windowHeight,controlScheme):
    sceneObjects = [rectangle("none", 0, round(windowWidth / 30), True, True,0,0, lblue),0,0]
    x = round(windowWidth / 15)
    width = round(windowWidth / 4)
    height = round((windowHeight - round(windowWidth * 2/15) - (round(windowWidth / 30) * len(controlScheme))) / (len(controlScheme) - 1))

    for control in range(len(controlScheme)):
        sceneObjects.append(rectangle(controlScheme[control][0], x, sceneObjects[-3].y + sceneObjects[-3].height + round(windowWidth / 30), True, True, width, height, white))

        sceneObjects.append(text(controlScheme[control][0] + "ButtonText", 0, 0, False, True, controlScheme[control][0], black, True, 25))
        sceneObjects[-1].centreText((sceneObjects[-2].x + round(sceneObjects[-2].width / 2), sceneObjects[-2].y + round(sceneObjects[-2].height / 2)))

        key = pygame.key.name(controlScheme[control][1])
        if len(key) > 2 and key[0] == "[" and key[-1] == "]":
            key = "Keypad " + key[1:-1]
        sceneObjects.append(text(controlScheme[control][0] + "AssignedText", round(windowWidth/2), sceneObjects[-2].y, False, True, "=  " + key, white, True, 45))

    for i in range(3):
        sceneObjects.pop(0)

    sceneObjects.append(rectangle("menu", round(windowWidth * 9/10), 0, True, True,round(windowWidth /10),round(windowWidth/10), lblue))
    sceneObjects.append(text("menuText", 0, 0, False, True, "Menu", white, True, 30))
    sceneObjects[-1].centreText((sceneObjects[-2].x + round(sceneObjects[-2].width / 2), sceneObjects[-2].y + round(sceneObjects[-2].height / 2)))
    return sceneObjects