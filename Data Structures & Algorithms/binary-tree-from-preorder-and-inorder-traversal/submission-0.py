# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == []:
            return None
        root = preorder.pop(0)
        rootIndex = inorder.index(root)
        left = inorder[:rootIndex]
        right = inorder[rootIndex+1:]

        node = TreeNode(root, self.buildTree(preorder[:len(left)],left), self.buildTree(preorder[len(left):],right))

        return node



        