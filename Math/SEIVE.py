__author__ = 'Vivek'
#Implementation of Sieve of eratosthenes , It returns an array containing all prime numbers less than A ( Including A)
def sieve(A):
    """
    :param: An integer A
    :return: An array of prime number less than equal to A
    """
    L = [1] * (A + 1)
    L[0] = 0
    L[1] = 0
    for i in range(2, int(A**0.5) + 1) :
        if L[i] == 1 :
            j = 2
            while i * j <= A :
                L[i * j] = 0
                j = j + 1

    res = []
    for i in range(len(L)) :
        if L[i] == 1:
            res.append(i)
    return res

