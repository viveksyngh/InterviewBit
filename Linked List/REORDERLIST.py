__author__ = 'Vivek'
#Given a singly linked list
#    L: L0 → L1 → … → Ln-1 → Ln,

#reorder it to:

#    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
#You must do this in-place without altering the nodes’ values.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if A.next == None :
            return A
        pre = A
        cur = A.next
        while cur != None :
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        A.next = None
        return pre
    def reorderList(self, A):
        if A.next == None or A.next.next == None :
            return A
        slow = A
        fast = A
        while fast != None and fast.next != None and fast.next.next != None :
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        #print second.val
        second = self.reverseList(second)
        #print second.next.val
        cur1 = A
        cur2 = second
        while cur2 != None :
            temp1 = cur1.next
            temp2 = cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1 = temp1
            cur2 = temp2
        return A



