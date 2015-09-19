__author__ = 'Vivek'

#Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#You should return the following matrix:
#[ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]

def generateMatrix(self, A):
        result = [[0] * A for _ in range(A)]
        count = 1
        T = 0
        B = len(result) - 1
        L = 0
        R = len(result[0]) -1
        dir = 0
        while T <= B and L <= R :
            if dir == 0 :
                for i in range(L, R+1) :
                    result[T][i] = count
                    count += 1
                T = T + 1
                dir = 1
            elif dir == 1 :
                for i in range(T, B + 1) :
                    result[i][R] = count
                    count += 1
                R = R - 1
                dir = 2
            elif dir == 2 :
                for i in range(R , L - 1 , -1) :
                    result[B][i] = count
                    count += 1
                B = B -1
                dir = 3
            elif dir == 3 :
                for i in range(B, T - 1, -1) :
                    result[i][L] = count
                    count += 1
                L = L + 1
                dir = 0
        return result

