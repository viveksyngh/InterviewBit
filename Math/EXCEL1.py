__author__ = 'Vivek'

#Given a column title as appears in an Excel sheet, return its corresponding column number.

def titleToNumber(self, A):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = 0
        for i in range(len(A)) :
            num += (alphabet.index(A[i]) + 1) *  (26 ** (len(A) - i - 1) )
        return num
#A -> 1
#B -> 2
#C -> 3
#...
#Z -> 26
#AA -> 27
#AB -> 28
