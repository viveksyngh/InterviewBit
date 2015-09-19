__author__ = 'Vivek'

#Implementation of (x^n)%d

def pow(self, x, n, d):
    """

    :param x: integer
    :param n: integer
    :param d: integer
    :return: (x^n)%d
    """
    res = 1
    sq = x
    if n == 0 and x == 0:
        return 0
    if n == 1 :
        return x%d
    while n != 0 :
        if n%2 == 1 :
            res = res * sq
        sq = (sq * sq)%d
        n = n/2
        if res > d :
            res = res%d
    return res

print(pow(71045970, 41535484, 64735492))