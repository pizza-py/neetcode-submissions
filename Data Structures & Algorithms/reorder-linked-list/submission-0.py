# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        node = head
        n = 0
        while node:
            nodes.append(node)
            n+=1
            node = node.next
        ptr1 = 0
        ptr2 = n-1
        while ptr1 < ptr2:
            nodes[ptr1].next = nodes[ptr2]
            nodes[ptr2].next = nodes[ptr1+1]
            ptr1 += 1
            ptr2 -= 1
        nodes[ptr1].next = None
        
        
        
        