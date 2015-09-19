__author__ = 'Vivek'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#For example,
#Given 1->2->3->3->4->4->5, return 1->2->5.
#Given 1->1->1->2->3, return 2->3.


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        current = A
        if current == None :
            return A
        prev = None
        repeat = False
        while current != None and current.next != None :

            if current.val == current.next.val :
                temp = current.next
                current.next = temp.next
                repeat = True
                del temp
            else :
                if repeat :
                    current.val = current.next.val
                    current.next = current.next.next
                    repeat = False
                else :
                    prev = current
                    current = current.next
        if repeat :
            if current == A:
                A = None
            else :
                prev.next = None
        return A