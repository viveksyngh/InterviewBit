__author__ = 'Vivek'

#Write a program to find the node at which the intersection of two singly linked lists begins.

#For example, the following two linked lists:

#A:          a1 → a2
#                   ↘
#                     c1 → c2 → c3
#                   ↗
#B:     b1 → b2 → b3

#begin to intersect at node c1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        len1, len2 = 0, 0
        temp1, temp2 = A, B
        while temp1 != None :
            temp1 = temp1.next
            len1 += 1
        while temp2 != None :
            temp2 = temp2.next
            len2 += 1
        d = abs(len1 - len2)
        count = 0
        temp1 = A
        temp2 = B
        if len1 > len2 :
            while count < d:
                temp1 = temp1.next
                count += 1
        else :
            while count < d :
                temp2 = temp2.next
                count += 1
        while temp1 and temp2 and temp1 != temp2 :
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1
