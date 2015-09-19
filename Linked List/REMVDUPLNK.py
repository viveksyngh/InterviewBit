__author__ = 'Vivek'
#Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        current = A
        if current == None :
            return A
        while current != None and current.next != None :
            if current.val == current.next.val :
                temp = current.next
                current.next = temp.next
                del temp
            else :
                current = current.next
        return A
