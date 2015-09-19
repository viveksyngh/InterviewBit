__author__ = 'Vivek'

#Given a sorted array, remove the duplicates in place such that each element appear atmost twice and return the new length.
#Do not allocate extra space for another array, you must do this in place with constant memory.

def removeDuplicates(self, A):
        i = 1
        j = 0
        count = 1
        while i < len(A) :
            if A[i] == A[j] and count < 2:
                count += 1
                j += 1
                A[j] = A[i]
                i += 1
            elif A[i] == A[j] and count >= 2 :
                count += 1
                i += 1
            elif A[i] != A[j] :
                count = 1
                j += 1
                A[j] = A[i]
                i += 1
        return j+1

