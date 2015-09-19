__author__ = 'Vivek'
#Find starting and ending index of an element in sorted list of elements
def binarySearch(A, B, searchFirst) :
    """
    Modified version of binary search
    :param: Sorted List of integers, target element, boolean value (True for first index, False for last index)
    :return: List of first index and last index, if target element not found returns [-1, -1]
    """
    low = 0
    high = len(A) - 1
    result = -1
    while low <= high :
        mid = (high + low)/2
        if A[mid] == B :
            result = mid
            if searchFirst :
                high = mid - 1
            else :
                low = mid + 1
        elif B < A[mid] :
            high = mid - 1
        else :
            low = mid + 1
    return result
def searchRange(A, B):
        start = binarySearch(A, B, True)
        end = binarySearch(A, B, False)
        return [start, end]
