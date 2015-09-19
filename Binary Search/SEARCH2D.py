__author__ = "Vivek"
#Write an efficient algorithm that searches for a value in an m x n matrix.

# @param A : list of list of integers
# @param B : integer
# @return an integer

def binarySearch(A, B) :
        start = 0
        end = len(A) - 1
        while start <= end :
            mid = (start + end )//2
            if A[mid] == B :
                return 1
            elif B < A[mid] :
                end = mid - 1
            elif B > A[mid] :
                start = mid + 1
        return 0
def searchMatrix(self, A, B):
        result = 0
        for i in range(len(A)) :
            result = self.binarySearch(A[i], B)
            if result == 1 :
                return 1
        return result
