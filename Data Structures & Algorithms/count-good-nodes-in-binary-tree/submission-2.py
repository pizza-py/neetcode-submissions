# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        number = 0
        def dfs(node, maximum):
            if node is None:
                return 
            else:
                if node.val >= maximum:
                    nonlocal number
                    number += 1
                dfs(node.left,max(maximum, node.val))
                dfs(node.right,max(maximum, node.val))
                return

        dfs(root, -101)
        return number
        