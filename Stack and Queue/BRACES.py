__author__ = 'Vivek'

#Write a program to validate if the input string has redundant braces?
#E.g.
#((a+b)) has redundant braces so answer will be 1
#(a + (a + b)) doesn't have have any redundant braces so answer will be 0

def braces(A):
        braces = 0
        for char in A :
            if char == '(' :
                braces += 1
            elif char in "*/+-" :
                braces -= 1
            if braces < 0 :
                braces = 0
        if braces == 0 :
            return 0
        else :
            return 1
