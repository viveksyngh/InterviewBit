__author__ = 'Vivek'
#Merge two sorted linked lists and return it as a new list.
#The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        curA, curB = A, B
        if A == None :
            return B
        elif B == None :
            return A
        if curA.val <= curB.val :
            C = curA
            curA = curA.next
        else :
            C = curB
            curB = curB.next
        curC = C
        while curA != None and curB != None :
            if curA.val <= curB.val :
                curC.next = curA
                curA = curA.next
                curC = curC.next
            else :
                curC.next = curB
                curB = curB.next
                curC = curC.next

        while curA != None :
            curC.next = curA
            curA = curA.next
            curC = curC.next

        while curB != None :
            curC.next = curB
            curB = curB.next
            curC = curC.next
        return C
