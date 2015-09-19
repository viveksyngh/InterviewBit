__author__ = 'Vivek'
#Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
def removeDuplicates(A):
        j = 0
        i = 1
        while i < len(A) :
            if A[i] == A[j] :
                i += 1
            else :
                j += 1
                A[j] = A[i]
                i += 1
        return j + 1