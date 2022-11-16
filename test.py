from algorithm import A_Star, createState

startStateTiles = [[3, 6, 1], [4, 5, 8], [2, 7, None]]
goalStateTiles = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
startState = createState(tiles=startStateTiles, parentState=None, goalTiles=goalStateTiles)
result = A_Star(startState=startState, goalStateTiles=goalStateTiles)

for state in result:
    print(state.tiles)