__author__ = 'Vivek'
#This function returns all the factors of an integer in sorted order
def allFactors(A):
    """
    :param: A positive integer
    :return: All the factors of the integer in sorted order.
    """
    res = []
    firstHalf = []
    secondHalf = []
    for i in range(1, int(A ** 0.5) + 1) :
        if A%i == 0 :
            firstHalf.append(i)
            if i != A ** 0.5 :
                secondHalf.insert(0, A/i)
    firstHalf.extend(secondHalf)
    return firstHalf
print(allFactors(36))

