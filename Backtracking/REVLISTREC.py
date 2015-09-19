__author__ = 'Vivek'

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    head = ListNode(0)
    def revUtil(self,A) :
        if A.next == None :
            self.head.next = A
            return
        else :
            self.reverseList(A.next)
            temp = A.next
            temp.next = A
            A.next = None

    def reverseList(self, A):
        self.revUtil(A)
        return self.head.next



