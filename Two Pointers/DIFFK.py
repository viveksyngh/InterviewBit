__author__ = 'Vivek'

#Given an array ‘A’ of sorted integers and another non negative integer k,
#find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
#----------------------------------------------------------------------------

# @param A : list of integers
# @param B : integer
# @return an integer
def diffPossible(self, A, B):
    j = 1
    for i in range(len(A)) :
        while j < len(A) :
            if i != j and A[j] - A[i] == B :
                return 1
            if A[j] - A[i] > B :
                break
            j += 1
    return 0
