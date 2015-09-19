__author__ = 'Vivek'
#Given an array and a value, remove all the instances of that value in the array.
#if array A is [4, 1, 1, 2, 1, 3]
#and value elem is 1,
#then new length is 3, and A is now [4, 2, 3]
def removeElement(A, B):
        i = 1
        j = 0
        if A[0] == B :
            j = -1
        while i < len(A) :
            if A[i] == B :
                i += 1
            else :
                j += 1
                A[j] = A[i]
                i += 1
        return j + 1
