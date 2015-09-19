__author__ = 'Vivek'

#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#Example:
#"A man, a plan, a canal: Panama" is a palindrome.
#"race a car" is not a palindrome.
#Return 0 / 1 ( 0 for false, 1 for true ) for this problem

import string
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        punctuation = string.punctuation
        newstring = ""
        for char in A.lower() :
            if char in punctuation or char == ' ' :
                continue
            newstring += char
        low = 0
        high = len(newstring)-1
        while low < high :
            if newstring[low] == newstring[high] :
                low += 1
                high -= 1
            else :
                return 0
        return 1

