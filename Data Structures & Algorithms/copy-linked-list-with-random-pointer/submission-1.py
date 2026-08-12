"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToCopy = {None:None}

        if head == None:
            return


        cur = head
        res = Node(cur.val)
        cur = cur.next
        prev = res
        nodeToCopy[head] = prev
        while cur:
            copy = Node(cur.val)
            if prev:
                prev.next = copy
            nodeToCopy[cur] = copy

            cur = cur.next
            prev = prev.next
        
        curOriginal = head
        curCopy = res

        while curCopy:
            curCopy.random = nodeToCopy[curOriginal.random]
            curCopy = curCopy.next
            curOriginal = curOriginal.next
        
        return res
        