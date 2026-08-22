# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prev = None
        cur = head
        count = 1
        while count < left and cur:
            prev = cur
            cur = cur.next
            count += 1
        
        newHead = cur

        while count < right and cur:
            temp = cur.next.next
            cur.next.next = newHead
            newHead = cur.next
            cur.next = temp
            count += 1
        
        if prev:
            prev.next = newHead
            return head
        else:
            return newHead

        
        