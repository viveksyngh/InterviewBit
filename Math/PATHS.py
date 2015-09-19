__author__ = 'Vivek'
import math
#A robot is located at the top-left corner(Start) of an A x B grid
#The robot can only move either down or right at any point in time.
#The robot is trying to reach the bottom-right(Finish) corner of the grid
#How many possible unique paths are there ?

def nCr(self, n, r) :
        f = math.factorial
        return f(n)/f(r)/f(n -r)

def uniquePaths(self, A, B):
        return self.nCr(A+B-2, B -1)

#Input : A = 2, B = 2
#Output : 2
#2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
#              OR  : (0, 0) -> (1, 0) -> (1, 1)
