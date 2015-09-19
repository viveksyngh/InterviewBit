__author__ = 'Vivek'

#Divide two integers without using multiplication, division and mod operator.
#Return the floor of the result of the division.

def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0
        p = abs(dividend)
        q = abs(divisor)
        if divisor == 0 or (divisor == 1 and dividend >= INT_MAX) :
            return INT_MAX
        if dividend <= INT_MIN and divisor == -1 :
            return INT_MAX
        if abs(divisor) == 1 :
            return dividend * divisor
        while p >= q :
            c = 0
            while p > (q << c) :
                c += 1
            res += 1 << (c -1)
            p -= q << (c - 1)

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) :
            return res
        else :
            return -res
