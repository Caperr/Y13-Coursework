import graphicsBackend

# This code taken from SilentGhost on stackoverflow.com
# source: http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
# end code by SilentGhost

# this is an adapted version of Isai Damier's bubble sort from geekviewpoint.com
# source: http://www.geekviewpoint.com/python/sorting/bubblesort
# Damier's version is written for a single dimensional array, so I adapted it for my multi-dimensional array.
def bubblesort(A):
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
            if int(A[k][1]) < int(A[k - 1][1]):
                swap(A, k, k - 1)
    return A

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
# end adapted code by Isai Damier

def getScores():
    scores = []
    f = open("leaderboard.txt","r")
    for line in range(file_len("leaderboard.txt")):
        read = f.readline()
        scores.append(read[0:len(read) - 1].split(" "))
    f.close()
    scores = bubblesort(scores)[::-1]
    if len(scores) > 9:
        scores = scores[0:9]
    f = open("leaderboard.txt","w")
    for score in scores:
        f.write(score[0] + " " + score[1] + "\n")
    f.close()
    return scores

go = "playGame"

while go == "playGame":
    result = "menu"
    while result in ["menu","controls","leaderboard"]:
        result = graphicsBackend.gameLoop("mainMenu",None)
        if result == "controls":
            result = graphicsBackend.gameLoop("controls",None)
        elif result == "leaderboard":
            result = graphicsBackend.gameLoop("leaderboard",getScores())
            if result == "playGame":
                result = "menu"
    if result == "newGame":
        # graphicsBackend.gameLoop("forest", None)
        score = graphicsBackend.gameLoop("forest", None)
        if score == "quitGame":
            break
        name = graphicsBackend.gameLoop("newScore",score)
        if score == "quitGame":
            break
        f = open("leaderboard.txt","a")
        f.write(name + " " + str(score) + "\n")
        f.close()
        go = graphicsBackend.gameLoop("leaderboard",getScores())
    else:
        go = ""
