__author__ = 'Vivek'

#Write a function that takes an unsigned integer and returns the number of 1 bits it has.

def numSetBits(self, A):
        count = 0
        while A :
            A = A & (A - 1)
            count += 1
        return count
