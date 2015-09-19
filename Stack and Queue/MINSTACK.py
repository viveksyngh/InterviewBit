__author__ = 'Vivek'

#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#push(x) – Push element x onto stack.
#pop() – Removes the element on top of the stack.
#top() – Get the top element.
#getMin() – Retrieve the minimum element in the stack.
#Note that all the operations have to be constant time operations.

class MinStack:

    def __init__(self) :
        self.items = [] #Stack element
        self.Min = [] #Min Element

    # @param x, an integer
    def push(self, x):
        if self.Min == [] or x <= self.Min[len(self.Min) - 1] :
            self.Min.append(x)
        self.items.append(x)

    # @return nothing
    def pop(self):
        if self.items == [] :
            return
        if self.items[len(self.items) -1] <= self.Min[len(self.Min) - 1] :
            self.Min.pop()
        self.items.pop()


    # @return an integer
    def top(self):
        if self.items == [] :
            return -1
        return self.items[len(self.items) - 1]

    # @return an integer
    def getMin(self):
        if self.Min == [] :
            return -1
        return self.Min[len(self.Min) - 1]
