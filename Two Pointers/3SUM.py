__author__ = 'Vivek'

#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
#Return the sum of the three integers.
#You may assume that each input would have exactly one solution.

def threeSumClosest(self, A, B):
        A.sort()
        Min = 2 ** 31 - 1
        result = 0
        for i in range(0, len(A) - 2) :
            l = i + 1
            r = len(A) - 1
            while l <  r :
                Sum = A[i] + A[l] + A[r]
                diff = abs(Sum - B )
                if diff == 0 :
                    return B
                if diff <  Min :
                    Min = diff
                    result = Sum
                if Sum < B :
                    l += 1
                else :
                    r -= 1
        return result
