__author__ = 'Vivek'
#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.
#For example,
#Given 1->4->3->2->5->2 and x = 3,
#return 1->2->2->4->3->5.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        head1 = ListNode(0)
        head2 = ListNode(0)
        p = A
        p1 = head1
        p2 = head2
        while p != None :
            if p.val < B :
                p1.next = ListNode(p.val)
                p1 = p1.next
                p = p.next
            else :
                p2.next = ListNode(p.val)
                p2 = p2.next
                p = p.next
        p1.next = head2.next
        return head1.next



