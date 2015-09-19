__author__ = 'Vivek'
#Given a collection of intervals, merge all overlapping intervals.
#Given [1,3],[2,6],[8,10],[15,18]
#return [1,6],[8,10],[15,18].

# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

def merge(self, intervals):
    intervals.sort(key = lambda x : x.start)
    stack = []
    stack.append(intervals[0])
    for i in range(1, len(intervals)) :
        top = stack[len(stack) - 1]
        if top.end < intervals[i].start :
            stack.append(intervals[i])
        elif top.end < intervals[i].end :
            top = stack.pop()
            top.end = intervals[i].end
            stack.append(top)
    return stack

