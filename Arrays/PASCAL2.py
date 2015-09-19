__author__ = 'Vivek'

#Given an index k, return the kth row of the Pascal’s triangle.
#Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

def getRow(self, A):
        nextValue = 1
        row = [nextValue]
        for i in range(A) :
            nextValue = nextValue * (A - i) * 1 / (i + 1)
            row.append(nextValue)
        return row
