# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        c1 = head
        while c1 != None:
            if c1 not in visited:
                visited.add(c1)
                c1 = c1.next
            else:
                return True
        return False