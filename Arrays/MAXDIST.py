__author__ = 'Vivek'
#Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
#If there is no solution possible, return -1.

from operator import itemgetter
# @param A : tuple of integers
# @return an integer
def maximumGap(self, A):
    Max = 0
    L = []
    for i in range(len(A)) :
        L.append([A[i], i])
    L.sort(key = itemgetter(0))
    Max = -1
    for i in range(len(L) - 1, -1, -1) :
        Max = max(Max, L[i][1])
        L[i][0] = Max
    Max = 0
    for i in range(len(L)) :
        Max = max(Max, L[i][0]- L[i][1])
    return Max