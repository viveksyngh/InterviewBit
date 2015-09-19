__author__ = 'Vivek'

#Given a number N >= 0, find its representation in binary.

def findDigitsInBinary(A):
        res = ""
        if A == 0 :
            return 0
        while A != 0 :
            res = str(A%2) + res
            A = A//2
        return res
