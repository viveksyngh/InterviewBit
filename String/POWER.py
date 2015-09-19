__author__ = 'Vivek'
#Find if Given number is power of 2 or not.
#More specifically, find if given number can be expressed as 2^k where k >= 1.
def power(A):
        temp = int(A)
        A = int(A)
        Sum = 0
        while A != 0 :
            Sum += A%2
            A = A/2
        if Sum == 1 and temp != 1 :
            return 1
        else :
            return 0
