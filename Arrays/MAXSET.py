__author__ = 'Vivek'

#Find out the maximum sub-array of non negative numbers from an array.
#The sub-array should be continuous. That is, a sub-array created by choosing the second and
# fourth element and skipping the third element is invalid.
#Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
# Sub-array A is greater than sub-array B if sum(A) > sum(B).

def maxset(self, A):
        maxSum = 0
        curretMaxSum = 0
        maxStart = 0
        maxEnd = 0
        currentStart = 0
        for i in range(len(A)) :
            if A[i] >= 0 :
                curretMaxSum += A[i]
                if curretMaxSum  > maxSum :
                    maxSum = curretMaxSum
                    maxStart = currentStart
                    maxEnd = i+1
                elif curretMaxSum == maxSum :
                    if (i - currentStart + 1) >  (maxEnd - maxStart + 1) :
                        maxStart = currentStart
                        maxEnd = i + 1
            if A[i] < 0 :
                curretMaxSum = 0
                currentStart = i + 1
        return A[maxStart : maxEnd]
