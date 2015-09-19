__author__ = 'Vivek'

#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
#Find all unique triplets in the array which gives the sum of zero.

def threeSum(self, A):
        A.sort()
        result = set()
        for i in range(len(A) - 2) :
            l = i + 1
            r = len(A) - 1
            while l < r :
                Sum = A[i] + A[l] + A[r]
                if Sum == 0 :
                    result.add((A[i], A[l], A[r]))
                    l += 1
                    r -= 1
                elif Sum < 0 :
                    l += 1
                else :
                    r -= 1
        List = []
        for res in result :
            List.append(list(res))
        return List
