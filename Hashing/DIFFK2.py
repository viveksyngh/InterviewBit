__author__ = 'Vivek'

#Given an array A of integers and another non negative integer k,
#find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

def diffPossible(A, B):
        diff_dict = {}
        for i in range(len(A)) :
            if diff_dict.get(A[i], None ) != None :
                return 1
            else :
                diff_dict[A[i] + B] = A[i]
                diff_dict[A[i] - B] = A[i]
        return 0

print diffPossible([34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ], 97)
print diffPossible([2, 5, 3], 2)