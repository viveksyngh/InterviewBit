__author__ = 'Vivek'
#Returns smallest missing posistive integer in a list of integers
def divideArray(A) :
    """
    :param: List of integers
    :return: List having only positive integers
    """
    j = 0
    for i in range(len(A)) :
        if A[i] <= 0 :
            A[j], A[i] = A[i], A[j]
            j = j + 1
    return A[j:]

def firstMissingPositive(A):
    """
    :param: List of integers
    :return: Smallest positive missing integer
    """
    A = divideArray(A)
    for i in range(len(A)) :
        if abs(A[i]) - 1 < len(A) and A[abs(A[i]) - 1] > 0:
            A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]
    for i in range(len(A)) :
        if A[i] > 0 :
            return i+1
    return len(A) + 1

print(firstMissingPositive([3,4,-1,1])) # Will Return 2
print(firstMissingPositive([1,2,0])) # Will Return 3
print(firstMissingPositive([-8, -7, -6])) # Will Return 1
