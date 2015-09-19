__author__ = 'Vivek'
def nextPermutation(A):
    """
    :param: List of integer
    :return : numerically next greater permutation of integers
    """
    i = -1
    last = False
    for k in range(len(A)-1) :
        if A[k] < A[k+1] :
            i = k
    if i == -1 :
        last = True
    j = -1
    if not last :
        for k in range(len(A)) :
            if k > i and A[k] > A[i] :
                j = k
        A[i], A[j] = A[j], A[i]
        temp = A[i+1:]
        temp.reverse()
        temp1 = A[:i+1]
        temp1.extend(temp)
        return temp1
    if last :
        A.reverse()
        return A

print(nextPermutation([1,4,3,2])) # will return [2, 1, 3, 4]
print(nextPermutation([1,2,3,4])) # Will return [1, 2, 4, 3]
