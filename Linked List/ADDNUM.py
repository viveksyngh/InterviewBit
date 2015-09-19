__author__ = 'Vivek'
#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        num1, num2 = A, B
        res = None
        carry = 0
        if A == None :
            return B
        elif B == None :
            return A
        while num1 != None and num2 != None :
            temp = num1.val + num2.val + carry
            newnode = ListNode(0)
            newnode.next = None
            if temp >= 10 :
                newnode.val = temp - 10
                carry = 1
            else :
                newnode.val = temp
                carry = 0
            if res == None :
                res = newnode
                cur = res
            else :
                cur.next = newnode
                cur = cur.next
            num1 = num1.next
            num2 = num2.next
        while num1 != None :
            newnode = ListNode(0)
            newnode.next = None
            temp = num1.val + carry
            if temp >= 10:
                newnode.val = temp - 10
                carry = 1
            else :
                newnode.val = temp
                carry = 0
            cur.next = newnode
            cur = cur.next
            num1 = num1.next

        while num2 != None :
            newnode = ListNode(0)
            newnode.next = None
            temp = num2.val + carry
            if temp >= 10:
                newnode.val = temp - 10
                carry = 1
            else :
                newnode.val = temp
                carry = 0
            cur.next = newnode
            cur = cur.next
            num2 = num2.next
        if carry == 1:
            newnode = ListNode(0)
            newnode.next = None
            newnode.val = carry
            cur.next = newnode
            cur = cur.next
        return res









