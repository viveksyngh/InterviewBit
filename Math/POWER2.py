__author__ = 'Vivek'

#Given a positive integer which fits in a 32 bit signed integer,
#find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

def isPower(self, A):
        if A == 1 :
            return True
        elif A <= 3:
            return False
        for i in range(2, 33) :
            temp = self.newtonRaphson(i, A)
            if temp == int(temp) :
                return True
        return False

def newtonRaphson(self, k, n):
        n = float(n)
        u, s = n, n+1
        while u < s:
            s = u
            t = (k-1) * s + n / pow(s, k-1)
            u = t / k
        return s
