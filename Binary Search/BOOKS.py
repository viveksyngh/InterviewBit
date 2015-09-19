__author__ = 'Vivek'
def books( A, B):
        N = len(A)
        M = []
        if  N < B :
            return -1
        elif B == 1:
            return sum(A)
        for i in range(N+1) :
            M.append([0]*(N + 1))
        Cum = [0]*(N+1)
        for i in range(1, N + 1) :
            Cum[i] = Cum[i-1] + A[i-1]
        for i in range(1, N + 1) :
            M[i][1] = Cum[i]
        for i in range(1, B + 1) :
            M[1][i] = A[0]
        for i in range(2, B + 1) :
            for j in range(2, N + 1) :
                Max = 2 ** 31 - 1
                for p in range(1, j + 1) :
                    Max = min(Max, max(M[p][i-1], Cum[j] - Cum[p]))
                M[j][i] = Max
        #print M
        #print Cum
        return M[N][B]