__author__ = 'Vivek'

#Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.
#Do it in place

# @param  A : List of list of integers
# @return list of list of integers
def setZeroes(A):
    M = len(A)
    N = len(A[0])
    rows = [0] * M
    cols = [0] * N
    for i in range(M) :
        for j in range(N) :
            if A[i][j] == 0 :
                rows[i] = 1
                cols[j] = 1
    for i in range(M) :
        for j in range(N) :
            if rows[i] == 1 or cols[j] == 1 :
                A[i][j] = 0
    return A
