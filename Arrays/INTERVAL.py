__author__ = 'Vivek'
#Definition for an interval.
#class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from operator import itemgetter
from operator import itemgetter
def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key = itemgetter(0))
    stack = []
    stack.append(intervals[0])
    for i in range(1, len(intervals)) :
        top = stack[len(stack) - 1]
        if top[1] < intervals[i][0]  :
            stack.append(intervals[i])
        elif top[1] < intervals[i][1] :
            top = stack.pop()
            top[1] = intervals[i][1]
            stack.append(top)
    return stack



print(insert([[1,3],[6,9]],[2,5])) # Will return [1, 5] , [6, 9]
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9])) # Will return [[1, 2], [3, 10], [12, 16]]