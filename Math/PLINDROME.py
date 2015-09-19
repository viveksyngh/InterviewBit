__author__ = 'Vivek'
#Determine whether an integer is a palindrome. Do this without extra space.
#A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
#Negative numbers are not palindromic.

def isPalindrome(self, A):
        num = 0
        if A < 0 :
            return False
        temp = A
        while temp != 0 :
            num = num*10 + (temp%10)
            temp = temp/10
        return num == abs(A)