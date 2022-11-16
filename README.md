# A-Star-8-Puzzle
In 'test.py', 3rd line; There is the function 'A_Star(startState: State, goalStateTiles: list)'.
You can choose any start state in form: [[a, b, c], [d, e, f], [g, h, j]]
Every letter is different number from 1 to 8 and one of the letter is must be 'None' for the blank tile.
You must create the start state with 'createState(tiles: list, parentState: State, goalTiles: list)' for the heuristic calculation.
So you can change parameters in 'A_Star' function in 3rd line in 'test.py' according to above rules.
Example:
  Let start state tiles be [[2, 8, 3], [1, 6, 4], [7, None, 5]].
  Let goal state tiles be [[1, 2, 3], [8, None, 4], [7, 6, 5]].
  There is no parent state for start state.
  So createState must be -> 'createState([[2, 8, 3], [1, 6, 4], [7, None, 5]], None, [[1, 2, 3], [8, None, 4], [7, 6, 5]])'
  So A_Star must be -> 'A_Star(createState([[2, 8, 3], [1, 6, 4], [7, None, 5]], None, [[1, 2, 3], [8, None, 4], [7, 6, 5]]), [[1, 2, 3], [8, None, 4], [7, 6, 5]])'
  After the parameter changing algorithm is ready to run.
  Result will be ordered step list of the optimal path.
