__author__ = 'Vivek'

#Sort a linked list using insertion sort.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A == None or A.next == None :
            return A
        res = ListNode(A.val)
        temp = A.next
        while temp != None :
            temp1 = res
            prev = None
            while temp1 != None and temp1.val <= temp.val :
                prev = temp1
                temp1 = temp1.next
            if prev == None :
                Newnode = ListNode(temp.val)
                Newnode.next = temp1
                res = Newnode
            else :
                Newnode = ListNode(temp.val)
                prev.next = Newnode
                Newnode.next = temp1
            temp = temp.next
        return res





