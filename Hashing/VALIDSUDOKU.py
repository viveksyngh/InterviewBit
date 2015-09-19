__author__ = 'Vivek'

#Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
#The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.

def isValidSudoku(A) :
    row_dict = {}
    col_dict = {}
    cell_dict = {}
    N= len(A)
    box_size = int(N ** 0.5)
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if A[i][j] != '.' :
                if row_dict.get(i, []) == [] :
                    row_dict[i] = []
                    row_dict[i].append(A[i][j])
                elif A[i][j] in row_dict[i] :
                    return 0
                else :
                    row_dict[i].append(A[i][j])

                if col_dict.get(j, []) == [] :
                    col_dict[j] = []
                    col_dict[j].append(A[i][j])
                elif A[i][j] in col_dict[j] :
                    return 0
                else :
                    col_dict[j].append(A[i][j])

                #cell = (i/box_size) * box_size + (((i * N + j)%N)/box_size)
                cell = (i/box_size) * box_size + (j/box_size)
                #print cell_dict
                if cell_dict.get(cell, []) == [] :
                    cell_dict[cell] = []
                    cell_dict[cell].append(A[i][j])
                elif A[i][j] in cell_dict[cell] :
                    return 0
                else :
                    cell_dict[cell].append(A[i][j])
    #print row_dict
    #print col_dict
    #print cell_dict
    return 1

#print isValidSudoku(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"])
print isValidSudoku(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ])