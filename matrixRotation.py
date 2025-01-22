# Rotating a Matrix by 90 Degrees
# Problem:

# Given an n×nn×n matrix, rotate it 90 degrees clockwise in-place (without using extra space for another matrix).

def rotateMatrix(matrix):
    matlen = len(matrix)
    rowlen = len(matrix[0])

    for i in range(0,matlen):
        for j in range(0,rowlen):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(0,matlen):
        matrix[i].reverse()


    return matrix


mat = rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])# 3

# do a pretty print
for i in mat:
    print(i)    
# Expected output:
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]

# what is effectively done is every nth row is swaapped with 
# every nth column. Then the rows are reversed. This is done
# in place. 

# this is the best possible solution.


        