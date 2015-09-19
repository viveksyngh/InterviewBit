__author__ = 'Vivek'

#Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#Valid operators are +, -, *, /. Each operand may be an integer or another expression.

def evalRPN(A):
        stack = []
        for char in A :
            if char not in "+-*/" :
                stack.append(int(char))
            elif char in "+-*/" :
                op2 = stack.pop()
                op1 = stack.pop()
                if char == '+' :
                    stack.append(op1 + op2)
                elif char == '-' :
                    stack.append(op1 - op2)
                elif char == '*' :
                    stack.append(op1 * op2)
                else :
                    stack.append(op1/op2)
        return stack.pop()
