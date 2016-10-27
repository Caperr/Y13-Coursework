import graphicsBackend

result = graphicsBackend.gameLoop("mainMenu")

if result == "newGame":
    graphicsBackend.gameLoop("forest")