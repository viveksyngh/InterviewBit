__author__ = 'Vivek'
#Find Single integer from list of integers
def singleNumber(A):
    # @param A : tuple of integers
    # @return an integer
    res = A[0]
    for i in range(1, len(A)) :
        res = res ^ A[i]
    return res
