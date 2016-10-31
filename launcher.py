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

go = "playGame"

while go == "playGame":
    result = graphicsBackend.gameLoop("mainMenu",None)

    if result == "newGame":
        scores = []
        # graphicsBackend.gameLoop("forest", None)
        score = graphicsBackend.gameLoop("forest", None)
        name = graphicsBackend.gameLoop("newScore",score)
        f = open("leaderboard.txt","a")
        f.write(name + " " + str(score) + "\n")
        f.close()
        f = open("leaderboard.txt","r")
        for line in range(file_len("leaderboard.txt")):
            read = f.readline()
            scores.append(read[0:len(read) - 1].split(" "))
        f.close()
        scores = bubblesort(scores)[::-1]
        if len(scores) > 10:
            scores = scores[0:9]
        go = graphicsBackend.gameLoop("leaderboard",scores)
    else:
        go = ""