__author__ = 'Vivek'

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# @param A : string
# @return an integer
def isValid(self, A):
        Open = "({["
        Close = ")}]"
        stack = []
        for char in A :
            if char in "({[" :
               stack.append(char)
            else :
                if len(stack) == 0 :
                    return 0
                else :
                    top = stack[len(stack) - 1]
                    if Open.index(top) == Close.index(char) :
                        stack.pop()
                    else :
                        return 0
        if len(stack) == 0 :
            return 1
        else :
            return 0
