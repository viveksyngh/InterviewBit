#Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#Try to solve it in linear time/space.
#Example :
#Input : [1, 10, 5]
#Output : 5


# @param A : tuple of integers
# @return an integer
import math
def maximumGap(self, A):
    if len(A) < 2:
        return 0
    elif max(A) == min(A) :
        return 0
    bucket = {}
    N = len(A)
    Max = max(A)
    Min = min(A)
    for a in A :
        temp = math.floor((a - Min) * ( N - 1) /(Max - Min))
        if bucket.get(temp, []) == [] :
            bucket[temp] = []
        bucket[temp].append(a)
    res = 0
    prev = max(bucket[min(bucket.keys())])
    Keys = sorted(bucket.keys())
    for i  in range(1, len(Keys)) :
        res = max(res, min(bucket[Keys[i]]) - prev )
        prev = max(bucket[Keys[i]])
    return res
