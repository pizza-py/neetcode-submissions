# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        n1 = []
        n2 = []
        while node1 != None and node2 != None:
            n1.append(node1.val)
            n2.append(node2.val)
            node1,node2 = node1.next,node2.next
        while node1 != None:
            n1.append(node1.val)
            node1 = node1.next
        while node2 != None:
            n2.append(node2.val)
            node2 = node2.next
        n1 = int("".join(map(str, n1[::-1])))
        n2 = int("".join(map(str, n2[::-1])))
        sumList = list(str(n1+n2))[::-1]
        head = ListNode(sumList[0])
        cur = head
        for i in range(1, len(sumList)):
            temp = ListNode(sumList[i])
            cur.next = temp
            cur = temp
        return head
        