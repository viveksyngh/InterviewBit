__author__ = 'Vivek'

#Given numRows, generate the first numRows of Pascal’s triangle.
#Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

def generate(self, A):
        triangle = []
        for rownum in range(A) :
            nextValue = 1
            row = [nextValue]
            for i in range(rownum) :
                nextValue = nextValue * (rownum - i) * 1 / (i + 1)
                row.append(nextValue)
            triangle.append(row)
        return triangle