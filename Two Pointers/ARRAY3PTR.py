__author__ = 'Vivek'
#You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
#Find i, j, k such that :
#max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
#Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

# @param A : tuple of integers
# @param B : tuple of integers
# @param C : tuple of integers
# @return an integer
def minimize(self, A, B, C):
    Min = None
    i, j, k = 0, 0, 0
    while i < len(A) and j < len(B) and k < len(C) :
        temp = max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])
        if Min == None or temp < Min :
            Min = temp
        if temp == 0 :
            break
        if min(A[i], B[j], C[k]) == A[i]:
            i += 1
        elif min(A[i], B[j], C[k]) == B[j] :
            j += 1
        else :
            k += 1
    return Min
