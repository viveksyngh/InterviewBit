__author__ = 'Vivek'
#Given a linked list, swap every two adjacent nodes and return its head.
#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        temp = A
        while temp != None and temp.next != None :
            c = temp.val
            temp.val = temp.next.val
            temp.next.val = c
            temp = temp.next.next
        return A
