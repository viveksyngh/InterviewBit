__author__ = 'Vivek'
#Given an array of integers, every element appears thrice except for one which occurs once.
#Find that element which does not appear thrice.
def singleNumber(A):
    # @param A : tuple of integers
    # @return an integer
    ones, twos = 0, 0
    for i in range(0, len(A)) :
        ones, twos = (ones ^ A[i]) & ~twos , (ones & A[i]) | (twos & ~A[i])
        print ones, twos
    return ones
print(singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))