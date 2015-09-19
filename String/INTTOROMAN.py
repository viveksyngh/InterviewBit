__author__ = 'Vivek'
#Convert an integer into Roman Numerals
def intToRoman(A):
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res , i = "", 0
        if  A < 1 or A > 3999 :
            return res
        while A :
            res += (A//value[i])*numerals[i]
            A %= value[i]
            i += 1
        return res
