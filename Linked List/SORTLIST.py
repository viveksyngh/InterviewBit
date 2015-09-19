__author__ = 'Vivek'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


    # @param A : head node of linked list
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
def split(self, start) :
        if start == None or start.next == None :
            first = start
            second = None
        else :
            slow = start
            fast = start
            while fast != None and fast.next != None :
                slow = slow.next
                fast = fast.next.next
            first = start
            second = slow.next
            slow.next = None
        return first, second

def sortList(self, A):
        if A == None or A.next == None :
            return A
        firstHalf = None
        secondHalf = None
        firstHalf, secondHalf = self.split(A)
        self.sortList(firstHalf)
        self.sortList(secondHalf)
        #self.mergeTwoLists(firstHalf, secondHalf)
        return  self.mergeTwoLists(firstHalf, secondHalf)

