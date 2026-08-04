# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        cur = head
        temp = None
        count = 0

        while count < length - n:
            count += 1
            temp = cur
            cur = cur.next
        
        if not temp:
            return cur.next

        temp.next = cur.next
        return head

        