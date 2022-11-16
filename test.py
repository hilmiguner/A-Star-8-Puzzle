from algorithm import A_Star, createState

result = A_Star(createState([[2, 8, 3], [1, 6, 4], [7, None, 5]], None, [[1, 2, 3], [8, None, 4], [7, 6, 5]]), [[1, 2, 3], [8, None, 4], [7, 6, 5]])
for state in result:
    print(state.tiles)