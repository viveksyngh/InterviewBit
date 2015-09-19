__author__ = 'Vivek'

#Reverse digits of an integer.

def reverse(self, A):
        rev = 0
        flag = False
        if A < 0 :
            flag = True
            A = abs(A)
        while A != 0 :
            rev = rev * 10 + (A%10)
            A = A/10
        if rev > 2**31 :
            return 0
        if flag :
            return -rev
        else :
            return rev
