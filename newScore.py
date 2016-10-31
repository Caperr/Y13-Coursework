from objects import *
sceneObjects = []

def init(kills):
    playerName = text("playerName",100,270,False,True,"",black,True,40)
    killText = text("killText",20,20,False,True,"Score: " + str(kills),black,True,40)
    submit = rectangle("submit", 210, 360, True, True,230,60, lblue)
    submitText = text("submitText", 0, 0, False, True, "Submit", white, True, 45)
    submitText.centreText((submit.x + round(submit.width / 2), submit.y + round(submit.height / 2)))
    return [playerName,submit,submitText,killText]