__author__ = 'Vivek'

#Given an integer n, return the number of trailing zeroes in n!.

def trailingZeroes(self, A):
        numOfZero = 0
        i = 1
        while 5**i <= A :
            numOfZero += A//(5 ** i)
            i = i + 1
        return numOfZero