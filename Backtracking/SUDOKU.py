__author__ = 'Vivek'

def findUassignedLocation(grid, index) :
    N = len(grid)
    for i in range(N) :
        for j in range(N) :
            if grid[i][j] == 0:
                index[0] = i
                index[1] = j
                return True
    return False

def inRow(grid, row, num) :
    for col in range(len(grid)) :
        if grid[row][col] == num :
            return True
    return False

def inCol(grid, col, num) :
    for row in range(len(grid)) :
        if grid[row][col] == num :
            return True
    return False

def inBox(grid, startRow, startCol, num) :
    boxSize = int(len(grid) ** 0.5)
    for row in range(boxSize) :
        for col in range(boxSize) :
            if grid[startRow+row][startCol + col] == num :
                return True
    return False

def isSafe(grid, row, col, num) :
    boxSize = int(len(grid) ** 0.5)
    return not inRow(grid, row, num) and  not inCol(grid, col, num) and not inBox(grid, row - row%boxSize, col - col%boxSize, num)

def solve(grid) :
    index = [-1] * 2
    if not findUassignedLocation(grid, index) :
        return True
    row = index[0]
    col = index[1]
    for num in range(1, len(grid) + 1) :
        if isSafe(grid, row, col, num) :
            grid[row][col] = num
            if solve(grid) :
                return True
            grid[row][col] = 0
    return False
def printGrid(grid) :
    N = len(grid)
    for row in range(N) :
        for col in range(N) :
            print grid[row][col],
        print

def solveSudoku(grid) :
    A = []
    for i in range(len(grid)) :
        temp = []
        for j in range(len(grid[i])) :
            #print grid[i][0][j]
            temp.append(grid[i][j])
        A.append(temp[:])
    for i in range(len(grid)) :
        for j in range(len(grid)) :
            if A[i][j] == '.' :
                A[i][j] = 0
            else :
                A[i][j] = int(A[i][j])
    print A
    if solve(A) :
        for i in range(len(A)) :
            temp = ""
            for j in range(len(A)) :
                temp += str(A[i][j])
            A[i] = [temp]
        return  A
print(solveSudoku([ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]))

