__author__ = 'Vivek'

#Given a linked list, remove the nth node from the end of list and return its head.
#For example,
#Given linked list: 1->2->3->4->5, and n = 2.
#After removing the second node from the end, the linked list becomes 1->2->3->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        temp = A
        prev = None
        count = 1
        while count < B and temp != None:
            temp = temp.next
            count += 1
        Node = A
        prev = None
        if temp == None :
            A = A.next
            return A
        while temp.next != None :
            prev = Node
            Node = Node.next
            temp = temp.next
        if prev == None :
            A = Node.next
        else :
            prev.next = Node.next
        del Node
        return A