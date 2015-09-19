__author__ = 'Vivek'
#You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
#Find the position of zeros which when flipped will produce maximum continuous series of 1s.
#For this problem, return the indices of maximum continuous series of 1s in order.

# @param A : list of integers
# @param B : integer
# @return a list of integers
def maxone(self, A, B):
    l, r = 0, 0
    nZero = 0
    width = -1
    start = None
    end = None
    while r < len(A) :
        if nZero <= B :
            if A[r] == 0 :
                nZero += 1
            r += 1


        if nZero > B :
            if A[l] == 0 :
                nZero -= 1
            l += 1

        if r - l + 1 > width :
            width = r - l + 1
            start = l
            end = r
    res = []
    for i in range(start, end) :
        res.append(i)
    return res
