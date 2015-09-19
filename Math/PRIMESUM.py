__author__ = 'Vivek'
def sieve(A):
    """
    :param: An integer A
    :return: An array of prime number less than equal to A
    """
    L = [True] * (A + 1)
    L[0] = False
    L[1] = False
    for i in range(2, int(A**0.5) + 1) :
        if L[i] :
            j = 2
            while i * j <= A :
                L[i * j] = False
                j = j + 1
    return L
def primesum(A) :
    L = sieve(A)
    res = []
    for i in range(len(L)) :
        if L[i]  and L[A-i] :
            temp = [i, A - i]
            if len(res) == 0 :
                res = temp[:]
            elif  (res[0] <= temp[0] and res[1] < temp[1]) :
                res = temp[:]
    return  res

print(primesum(14))

