__author__ = 'Vivek'
#Reverse bits of an 32 bit unsigned integer
#Example
#  3
#  00000000000000000000000000000011
#  11000000000000000000000000000000
#return 3221225472
def reverse(A):
        # @param A : unsigned integer
        # @return an unsigned integer
        if A > 2**32-1 :
            return
        binaryString = ""
        while A != 0 :
            binaryString += str(A%2)
            A = A/2
        binaryString += '0' * (32 - len(binaryString))
        return int(binaryString, 2)
