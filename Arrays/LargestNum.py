__author__ = 'Vivek'
def comp(X, Y) :
    """
    :param: X, Y two integers
    :return : -1, 0 or 1
    """
    XY = str(X) + str(Y)
    YX = str(Y) + str(X)
    if XY < YX :
        return -1
    if XY == YX :
        return 0
    if XY > YX :
        return  1

def largestNumber(A) :
    """
    :param: tuple of non negative integers
    :return: Largest number that can be formed using integers
    """
    A.sort(cmp=comp, reverse=True)
    if max(A) == 0 :
        return 0
    return ''.join(str(i) for i in A)
print(largestNumber([3, 30, 34, 5, 9])) #Will Return 9534330
print(largestNumber([0, 0, 0, 0, 0])) #Will return 0
