__author__ = 'Vivek'

#Given a string S, find the longest palindromic substring in S.

# @param A : string# @return a strings
def expand(self, string, c1, c2) :
        l = c1
        r = c2
        n = len(string)
        while l >= 0 and r <= n - 1 and string[l] == string[r] :
            l -= 1
            r += 1
        return string[l + 1 : r]
def longestPalindrome(self, A):
        n = len(A)
        if n == 0 :
            return ""
        longest = A[0:1]
        for i in range(0, n-1) :
            temp1 = self.expand(A, i , i)
            #print temp1
            if len(temp1) > len(longest) :
                longest = temp1
            temp2 = self.expand(A, i , i + 1)
            if len(temp2) > len(longest) :
                longest = temp2
            #print temp2
        return longest