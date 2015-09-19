__author__ = 'Vivek'

def isPrime(A):
    """
    :param: An integer
    :return: Returns integer True if it's prime otherwise false

    """
    if A == 1:
        return False
    for i in range(2, int(A ** 0.5) + 1) :
        if A%i == 0 :
            return False
    return True

print(isPrime(1)) #Returns False
print(isPrime(2)) #Returns True
print(isPrime(5)) #Returns True
