__author__ = 'Vivek'

#You are given an n x n 2D matrix representing an image.
#Rotate the image by 90 degrees (clockwise).
#You need to do this in place.
#Note that if you end up using an additional array, you will only receive partial score.

# @param A : list of list of integers
# @return the same list modified
def rotate(self, A):
        N = len(A)
        A = zip(*A)
        for i in range(N) :
            A[i] = list(A[i])
        for i in range(N//2) :
            for j in range(N):
                A[j][i], A[j][N-1-i] = A[j][N-1-i] , A[j][i]
        return A

