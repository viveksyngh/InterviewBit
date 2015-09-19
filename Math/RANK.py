__author__ = 'Vivek'
# @param A : String
# @return an integer

#Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated.
def fact (self, n ) :
        if n <= 1 :
            return 1
        else :
            return n * self.fact(n-1)
def findRank(self, A):
        res = 1
        for i in range(0, len(A)-1) :
            rank = 0
            for j in range(i+1, len(A)) :
                if A[i] > A[j] :
                    rank += 1
            res = (res + rank * self.fact(len(A) - i - 1 ))%1000003
        return res
