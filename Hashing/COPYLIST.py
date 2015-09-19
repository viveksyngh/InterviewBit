__author__ = 'Vivek'

#A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

#Return a deep copy of the list.

class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None


def copyRandomList(self, head):
        node_map = {}
        newHead = RandomListNode(head.label)
        node_map[head] = newHead
        p = head
        q = newHead
        p = p.next
        while p != None :
            temp = RandomListNode(p.label)
            node_map[p] = temp
            q.next = temp
            q = temp
            p = p.next
        p = head
        q = newHead
        while p != None :
            if p.random != None :
                q.random = node_map[p.random]
            else :
                q.random = None
            p = p.next
            q = q.next
        return newHead
