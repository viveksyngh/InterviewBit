__author__ = 'Vivek'
#Given n non-negative integers a1, a2, ..., an,
#where each represents a point at coordinate (i, ai).
#'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.

def maxArea(self, A):
        maxarea = 0
        l = 0
        r = len(A) - 1
        while l < r :
            base = r - l
            height = min(A[l], A[r])
            area = base * height
            maxarea = max(area, maxarea)
            if A[l] < A[r] :
                l += 1
            else :
                r -= 1
        return maxarea

