__author__ = 'Vivek'

#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#Try solving it using constant additional space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        slow = A
        fast = A
        while slow and fast :
            slow = slow.next
            fast = fast.next
            if fast != None :
                fast = fast.next
            if slow == fast :
                break;
        if fast == None :
            return fast
        slow = A
        count = 0
        while slow != fast :
            slow = slow.next
            count += 1
        slow = A
        fast = A
        while count > 0 :
            fast = fast.next
            count -= 1
        while slow != fast :
            slow = slow.next
            fast = fast.next
        return fast


