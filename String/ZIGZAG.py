__author__ = 'Vivek'
#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#P.......A........H.......N
#..A..P....L....S....I...I....G
#....Y.........I........R
#OR
#P   A   H   N
#A P L S I I G
#Y   I   R

#And then read line by line: PAHNAPLSIIGYIR

def convert(A, B):
        if B <= 1 :
            return A
        res = ""
        n = len(A)
        for i in range(B) :
            for j in range(i, n, 2*(B - 1)) :
                res += A[j]
                if i > 0 and i < B - 1 and j  + 2 * (B -1 - i) < n:
                    res += A[j + 2 * (B - 1 - i)]
        return res
