__author__ = 'Vivek'

# @param A : list of integers
# @return a list of list of integers
def permuteUtil(self, res, A, l , r) :
        if l == r :
            res.append(A[:])
        else :
            for i in range(l, r+1) :
                A[l], A[i] = A[i], A[l]
                self.permuteUtil(res, A, l + 1, r)
                A[i], A[l] = A[l], A[i]

def permute(self, A):
        l = 0
        r = len(A) -1
        res = []
        self.permuteUtil(res, A, l , r)
        return res
