__author__ = 'Vivek'
# @param A : tuple of integers
# @return an integer
def trap(self, A):
        n = len(A)
        if n <= 2:
            return 0
        left = [0]* n
        right = [0] * n
        Max = A[0]
        left[0] = A[0]
        for i in range(1, n) :
            if A[i] < Max :
                left[i] = Max

            else :
                left[i] = A[i]
                Max = A[i]
        Max = A[n-1]
        right[n-1] = Max
        for i in range(n -2, -1, -1) :
            if A[i] < Max :
                right[i] = Max
            else :
                right[i] = A[i]
                Max = A[i]
        water = 0
        for i in range(n) :
            water +=  min( left[i], right[i]) - A[i]
        return water
