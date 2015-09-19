__author__ = 'Vivek'

#Given a string S, reverse the string using stack.

# @param A : string
# @return a strings
def reverseString(self, A):
        stack = []
        for char in A :
            stack.append(char)
        res = ""
        temp = stack[:]
        for i in range(len(stack)) :
            res += temp.pop()
        return res
