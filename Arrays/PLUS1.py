def plusOne(A):
    """
    :param A: List containing digits of a non - negative number
    :return: List containing digits after addition of 1
    """
    length = len(A)
    number = 0
    i = length - 1
    while A[i] + 1 > 9 and i >= 0:
        A[i] = 0
        i = i - 1
    if i < 0 :
        i = i + 1
        A.insert(0, 0)
    A[i] = A[i] + 1
    number = 0
    res = []
    for i in range(len(A)) :
        number += A[i]
        if number != 0 :
            res.append(A[i])
    return res
print(plusOne([0, 1, 2, 3])) # Will Return [1, 2, 4]
print(plusOne([9, 9, 9, 9])) # Will Return [1, 0, 0, 0]
print(plusOne([0, 0, 0])) # Will Return [1]

