__author__ = 'Vivek'
#Reverse a linked list. Do it in-place and in one-pass.
#For example:
#Given 1->2->3->4->5->NULL,
#return 5->4->3->2->1->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        present = A
        past = None
        future = A.next
        while present != None :
            future = present.next
            present.next = past
            past = present
            present = future
        return past