__author__ = 'Vivek'

#Given a number N, verify if N is prime or not.
#Return 1 if N is prime, else return 0.

def isPrime(self, A):
        if A == 1:
            return 0
        for i in range(2, int(A ** 0.5) + 1) :
            if A%i == 0 :
                return 0
        return 1