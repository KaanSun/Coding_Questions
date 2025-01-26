'''
Problem Description:

Given an m x n board (matrix) and a word, determine if the word exists in the board. 
The word can be constructed from letters of sequentially adjacent cells, where 
"adjacent" cells are those horizontally or vertically neighboring. The same letter 
cell may not be used more than once.

Example:
Input:

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"

Output:

True


'''
def exist(board, word):
    collen = len(board)
    rowlen = len(board[0])
    traversed = []

    for i in range(0,collen):
        traversed.append([])
        for j in range(0,rowlen):
            traversed[i].append(False)


    def dfs(i,j,word):
        if word == "":
            return True

        result = False

        if i < 0 or i >= collen or j < 0 or j >= rowlen or board[i][j] != word[0] or traversed[i][j] != False:
            return False
        else:
            traversed[i][j] = 'true'
            if( dfs(i+1,j,word[1:]) or dfs(i-1,j,word[1:]) or dfs(i,j+1,word[1:]) or dfs(i,j-1,word[1:])):
                result = True
            
        return result

    result = False
    for i in range(0,collen):
        for j in range(0,rowlen):
            if board[i][j] == word[0]:
                result = dfs(i,j,word)
                if result == True:
                    return result

    return result


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"

print(exist(board,word))