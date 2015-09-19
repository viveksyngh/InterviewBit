__author__ = 'Vivek'

#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#For example:
#Given the array [-2,1,-3,4,-1,2,1,-5,4],
#the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#For this problem, return the maximum sum.

def maxSubArray(self, A):
        maxSumSoFar = 0
        currentMaxSum = 0
        for i in range(0, len(A)) :
            currentMaxSum += A[i]
            if currentMaxSum < 0 :
                currentMaxSum = 0
            if maxSumSoFar < currentMaxSum :
                maxSumSoFar = currentMaxSum
        if maxSumSoFar == 0 and max(A) >= 0 :
            return 0
        elif maxSumSoFar == 0 and max(A) < 0 :
            return max(A)
        else :
            return maxSumSoFar
