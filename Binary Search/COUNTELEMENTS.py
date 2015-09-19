__author__ = 'Vivek'

def binarySearch(A, B, flagSearchFirst) :
    """
    Modified version of Binary Search to find first or last index of an element when it is repeated
    :param A: List of sorted integers
    :param B: integer to be searched
    :param flagSearchFirst: Whether to search for first or last index of integer B in array
    :return: index (if  nott found then -1)
    """
    start = 0
    end = len(A) - 1
    result = -1
    while start <= end :
        mid = (start + end )//2
        if A[mid] == B :
            result = mid
            if flagSearchFirst :
                end = mid - 1
            else :
                start = mid + 1
        elif B < A[mid] :
            end = mid - 1
        elif B > A[mid] :
            start = mid + 1
    return result

def findCount(A, B):

    firstIndex = binarySearch(A, B, True)
    if firstIndex == -1 :
        return 0
    else :
        lastIndex = binarySearch(A, B, False)

    return lastIndex - firstIndex + 1

