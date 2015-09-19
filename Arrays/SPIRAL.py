__author__ = 'Vivek'

#Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

def spiralOrder(A):
        result = []
        T = 0
        B = len(A) - 1
        L = 0
        R = len(A[0]) -1
        dir = 0
        while T <= B and L <= R :
            if dir == 0 :
                for i in range(L, R+1) :
                    result.append(A[T][i])
                T = T + 1
                dir = 1
            elif dir == 1 :
                for i in range(T, B + 1) :
                    result.append(A[i][R])
                R = R - 1
                dir = 2
            elif dir == 2 :
                for i in range(R , L - 1 , -1) :
                    result.append(A[B][i])
                B = B -1
                dir = 3
            elif dir == 3 :
                for i in range(B, T - 1, -1) :
                    result.append(A[i][L])
                L = L + 1
                dir = 0
        return result
A = ((1,2,3),(4, 5, 6))
print(spiralOrder(A)) #will print [1, 2, 3, 6, 5, 4]
