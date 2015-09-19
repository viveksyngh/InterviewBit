__author__ = 'Vivek'
#Search for a target element in rotated array , if element present then return index otherwise -1
def binSearch(A, B) :
        """
        Binary Search Algorithm
        """
        low = 0
        high = len(A) - 1
        result = -1
        while low <= high :
            mid = (low + high)/2
            if A[mid] == B :
                return mid
            elif B > A[mid] :
                low = mid + 1
            else :
                high = mid - 1
        return -1

def findMin(A):
        """
        Find the index of minimum element in a rotated array
        """
        low = 0
        high = len(A) - 1
        N = len(A)
        while low <= high :
            mid = (low + high)/2
            next = (mid + 1)%N
            prev = (mid + N - 1)%N
            if A[low] < A[high] :
                return low
            elif A[mid] <= A[next] and A[mid] <= A[prev] :
                return mid
            elif A[mid] <= A[high] :
                high = mid - 1
            elif A[mid] >= A[low] :
                low = mid + 1

def search(A, B) :
        minIndex = findMin(A)
        if minIndex == 0 or minIndex == len(A) - 1 :
            return binSearch(A, B)
        else :
            res1 = binSearch(A[:minIndex], B)
            res2 = binSearch(A[minIndex:], B)
            if res1 == -1 and res2 == -1 :
                return -1
            if res1 == -1 :
                return res2 + minIndex
            elif res2 == -1 :
                return res1

