'''
Matrix + Breadth-First Search (BFS) Problem: Shortest Path in a Binary Matrix
Problem Description

You are given an nxm binary matrix grid. Each cell in the grid has a value of either 0 (walkable) 
or 1 (blocked). Your task is to find the shortest path from the top-left corner (grid[0][0]) to the 
bottom-right corner (grid[n-1][n-1]) if such a path exists.

    The path can only move horizontally, vertically to adjacent cells.
    Return the length of the shortest path. If no such path exists, return -1.

Example

Input:

grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 0]
]

Output:

4

Explanation: The shortest path from grid[0][0] to grid[2][2] is:

    Start at (0, 0), then (1, 1), (2, 1), and finally (2, 2).
'''

def ShortestPath(grid):

    collen = len(grid)
    rowlen = len(grid[0])
    queue = []
    queue.append([0,0,0])
    
    traversed = []
    for i in range(0,collen):
        traversed.append([])
        for j in range(0,rowlen):
            traversed[i].append(False)
            

    while queue:
        popped = queue.pop()
        if popped[0] != collen -1 or popped[1] != rowlen -1:
            leftCoords = None
            rightCoords = None
            upCoords = None
            downCoords = None

            if not(popped[1] == 0 or popped[1] >= rowlen):
                leftCoords = popped[1] - 1
                if traversed[popped[0]][leftCoords] == False and grid[popped[0]][leftCoords] != 1:
                    queue.append([popped[0],leftCoords,popped[2]+1])
                    traversed[popped[0]][leftCoords] == True
            if not(popped[1] <= -1 or popped[1] >= rowlen-1):
                rightCoords = popped[1] + 1
                if traversed[popped[0]][rightCoords] == False and grid[popped[0]][rightCoords] != 1:
                    queue.append([popped[0],rightCoords,popped[2]+1])
                    traversed[popped[0]][rightCoords] == True
            if not(popped[0] <= 0 or popped[0] >= collen):
                upCoords = popped[0] - 1
                if traversed[upCoords][popped[1]] == False and grid[upCoords][popped[1]] != 1:
                    queue.append([upCoords,popped[1],popped[2]+1])
                    traversed[upCoords][popped[1]] = True
            if not(popped[0] <= -1 or popped[0] >= collen -1):
                downCoords = popped[0] + 1
                if traversed[downCoords][popped[1]] == False and grid[downCoords][popped[1]] != 1:
                    queue.append([downCoords,popped[1],popped[2]+1])
                    traversed[downCoords][popped[1]] = True
        else:
            return popped[2]

grid = [
    [0, 1, 0 , 1 , 0],
    [0, 1, 0 , 1 , 0],
    [0, 1, 0 , 0 , 0],
    [0, 1, 0 , 1 , 0],
    [0, 0, 0 , 1 , 0],
]
print(ShortestPath(grid))            


