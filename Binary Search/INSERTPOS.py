__author__ = 'Vivek'
#Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.
def searchInsert(A, B):
    """
    :param: A List of integers , B integer to be inserted
    :return: return index if B is already present in A , otherwise index at which B will be inserted
    """
    low = 0
    high = len(A) - 1
    while low <= high :
        mid = (low + high)/2
        if A[mid] == B :
            return mid
        if mid + 1 != len(A) and A[mid] < B < A[mid+1] :
            return mid + 1
        elif mid == len(A) - 1  and A[mid] < B :
            return mid + 1
        elif mid != 0 and A[mid - 1] < B < A[mid] :
            return mid
        elif mid == 0 and A[mid] > B :
            return mid
        if B < A[mid] :
            high = mid - 1
        elif B > A[mid] :
            low = mid + 1
