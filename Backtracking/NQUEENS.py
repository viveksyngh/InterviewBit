__author__ = 'Vivek'

#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#Given an integer n, return all distinct solutions to the n-queens puzzle.
#Each solution contains a distinct board configuration of the n-queens’ placement,
# where 'Q' and '.' both indicate a queen  and an empty space respectively.


def isValid(a, col) :
    for i in range(col) :
        if a[i] == a[col] or abs(i-col) == abs(a[i] - a[col]) :
            return False
    return True

def storeResult(res, a, n) :
    temp = []
    for i in range(n) :
        temp.append( "." * a[i] + 'Q' + "." * (n - a[i] - 1))
    res.append(temp[:])

def backTrack(res, a, col, n) :
    if col == n :
        storeResult(res, a, n)
    else :
        for i in range(n) :
            a[col] = i
            if isValid(a, col) :
                backTrack(res, a, col+1, n)
def solveNQueens(A) :
    board = []
    res = []
    for i in range(A) :
        board.append([0] * A)
    print board
    a = [-1] * A
    backTrack(res, a, 0, A)
    print res
solveNQueens(4)