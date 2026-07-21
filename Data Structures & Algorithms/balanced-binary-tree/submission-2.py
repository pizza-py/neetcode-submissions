# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        if root == None:
            return 0
        else:
            return 1 + max(self.height(root.left),self.height(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            print(root.val)
            res1 = self.isBalanced(root.left)
            res2 = self.isBalanced(root.right)
            res3 = self.height(root.left)-self.height(root.right) in {-1,0,1}
            return res1 and res2 and res3
        
        