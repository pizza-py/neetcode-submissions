# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        res = ListNode()
        cur = res
        while (ptr1 != None) and (ptr2 != None):
            if (ptr1.val <= ptr2.val):
                cur.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
                cur = cur.next
            else:
                cur.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
                cur = cur.next
        
        while (ptr1 != None):
            cur.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
            cur = cur.next
        while (ptr2 != None):
            cur.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
            cur = cur.next

        return res.next