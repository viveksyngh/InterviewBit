__author__ = 'Vivek'

#Given a positive integer, return its corresponding column title as appear in an Excel sheet.

def convertToTitle(A):
        aplhabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        column = ""
        while A > 0 :
            temp = A%26
            #print temp, A
            if temp == 0 :
                temp = 26
                A = A - 1
            #print aplhabet[temp-1]
            column = aplhabet[temp-1] + column
            A = A/26
        return column
#1 -> A
#2 -> B
#3 -> C
#...
#26 -> Z
#27 -> AA
#28 -> AB
