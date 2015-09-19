__author__ = 'Vivek'

#Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
#find the area of largest rectangle in the histogram.

def largestRectangleArea(self, A):
        stack = []
        i = 0
        maxarea = 0
        if len(A) == 1 :
            return A[0]
        while i < len(A) :
            if stack == [] or A[stack[len(stack) - 1]] <= A[i] :
                stack.append(i)
                i += 1
            else :
                top = stack.pop()
                if stack == [] :
                    base = i
                else :
                    base = (i - stack[len(stack) - 1] - 1)
                area = A[top] * base
                maxarea = max(area, maxarea)
        while stack != [] :
            top = stack.pop()
            if stack == [] :
                base = i
            else :
                base = (i - stack[len(stack) - 1] - 1)
            area = A[top] * base
            maxarea = max(area, maxarea)
        return maxarea
