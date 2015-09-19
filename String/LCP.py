__author__ = 'Vivek'
#LCP LONGEST COMMON PREFIX
def longestCommonPrefix(A):
        """
        Find the longest common prefix in an array of string
        :param: Array of strings
        :return: prefix string
        """
        prevLCP = A[0]
        for i in range(1, len(A)):
            curLCP = ""
            j = 0
            while (j < len(A[i]) and  j < len(prevLCP)) and prevLCP[j] == A[i][j] :
                curLCP += A[i][j]
                j = j + 1
            prevLCP = curLCP
        return prevLCP
print(longestCommonPrefix("aaa", "aaaaaaabbbb", "aaaaaabbbbb")) # Will Return "aaa"


