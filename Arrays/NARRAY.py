def repeatedNumber(A):
    """

    :param A: A tupple of integer
    :return: Return a list [duplicate element , missing element]
    """
    n = len(A)
    dup = 0
    for i in range(len(A)) :
        if A[abs(A[i]) - 1]  > 0 :
            A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]
        elif A[abs(A[i]) - 1] < 0 :
            dup = abs(A[i])
    sum1 = 0
    for j in range(len(A)) :
        sum1 += abs(A[j])
    missing = (n * (n + 1))/2 - sum1 + dup
    return [dup, missing]


repeatedNumber([3, 1, 2, 5, 8, 6, 7, 10, 8, 9]) # will Return [8, 4]
repeatedNumber([3, 1, 2, 5, 3]) # Will return [3, 4]



