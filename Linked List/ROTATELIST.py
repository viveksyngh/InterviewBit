__author__ = 'Vivek'
#Given a list, rotate the list to the right by k places, where k is non-negative.
#For example:
#Given 1->2->3->4->5->NULL and k = 2,
#return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        cur = A
        prev = None
        length = 1
        while cur.next != None :
            prev = cur
            cur = cur.next
            length = length + 1
        end = cur
        count = 0
        cur = A
        B = B%length
        if B == 0 :
            return A
        while count < length - B - 1:
            cur = cur.next
            count += 1
        end.next = A
        A = cur.next
        cur.next = None
        return A




