# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root, "+"]
        lastSeen = None
        res = []
        while len(queue) > 1:
            cur = queue.pop(0)
            if cur == "+":
                res.append(lastSeen.val)
                queue.append("+")
            elif cur is None:
                pass
            else:
                lastSeen = cur
                queue.append(cur.left)
                queue.append(cur.right)
        
        return res



        