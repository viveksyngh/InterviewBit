__author__ = 'Vivek'

#Reverse a linked list from position m to n. Do it in-place and in one-pass.
#For example:
#Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#return 1->4->3->2->5->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if A == None :
            return A
        elif n - m + 1 == 1 :
            return A
        temp = A
        prev = None
        count = 1
        while count < m :
            prev = temp
            temp = temp.next
            count += 1
        present = temp
        past = None
        future = temp.next
        first = temp
        while count <= n and present != None :
            temp = temp.next
            count += 1
            future = present.next
            present.next = past
            past = present
            present = future
        first.next = present
        #if future != None :
        #   future.next = temp.next
        if prev != None :
            prev.next = past
        else :
            A = past
        return A

