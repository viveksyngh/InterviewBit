__author__ = 'Vivek'
#Given two numbers represented as strings, return multiplication of the numbers as a string.
# DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
def multiply(A, B):
        res = "0" * (len(A) + len(B))
        if A == '0' or B == '0' :
            return '0'
        elif A == '1' :
            return B
        elif B == '1' :
            return A
        count = 0
        for i in range(len(A)-1, -1, -1) :
            if len(res)-count == 0 :
                temp = int(A[i]) * int(B)
            else :
                temp = int(res[:len(res)-count]) + int(A[i]) * int(B)
            res = str(temp) + res[len(res)-count:]
            count += 1
        return res
