__author__ = 'Vivek'

# @param n : integer
# @param k : integer
# @return a list of list of integers
def combineutil(self, A, res, data, start, end, index, r ) :
        if index == r :
           res.append(data[:])
           return res
        i = start
        while i <= end and end - i + 1 >= r - index :
            data[index] = A[i]
            self.combineutil(A, res, data, i + 1, end, index + 1, r)
            i += 1
def combine(self, n, k):
        A = range(1, n+1)
        res = []
        data = [0] * k
        self.combineutil(A, res, data, 0, n - 1, 0 , k)
        return res
