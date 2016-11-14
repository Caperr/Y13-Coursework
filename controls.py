# import all graphical objects
from objects import *
# the list of all of the objects in the scene
sceneObjects = []

# initialize graphical objects based on window size
def init(windowWidth,windowHeight,controlScheme):
    sceneObjects = []
    for control in range(len(controlScheme)):
        sceneObjects.append(rectangle(controlScheme[control][0],\
                                      round(windowWidth / 15),\
                                      round(windowWidth / 15) + (control * round(windowHeight / (len(controlScheme) + (2 * round(windowWidth / 15))))),\
                                      True,\
                                      True,\
                                      round(windowWidth / 4),\
                                      round(windowHeight / (len(controlScheme) + (2 * round(windowWidth / 15))),\
                                            grey))
        sceneObjects.append(text(controlScheme[control][0], 0, 0, False, True, controlScheme[control][0], black, True, 25))
        sceneObjects[-1].centreText((sceneObjects[-2].x + round(sceneObjects[-2].width / 2), sceneObjects[-2].y + round(sceneObjects[-2].height / 2)))
    return sceneObjects