__author__ = 'Vivek'

#The gray code is a binary numeral system where two successive values differ in only one bit.
#Given a non-negative integer n representing the total number of bits in the code,
# print the sequence of gray code. A gray code sequence must begin with 0.
#For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

class Solution:
    # @param A : integer
    # @return a list of integers
    res = ["0", "1"]
    def grayCodeUtil(self, k , n) :
        #global res
        if k == n :
            return self.res
        else :
            L1 = self.res[:]
            L2 = L1[:]
            L2.reverse()
            for i in range(len(L1)) :
                L1[i] = "0" + L1[i]
            for i in range(len(L2)) :
                L2[i] = "1" + L2[i]
            self.res = L1 + L2
        #print res
            self.grayCodeUtil(k+1, n)
    def grayCode(self, A):
        #global res
        self.grayCodeUtil(1, A)
        return self.res

sol = Solution()
print sol.grayCode(3)

