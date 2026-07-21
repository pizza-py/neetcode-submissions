# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        queue = [[root,0]]
        while queue:
            cur = queue.pop(0)
            if cur[0] is None:
                pass
            else:
                if cur[1] in res:
                    res[cur[1]].append(cur[0].val)
                else:
                    res[cur[1]] = [cur[0].val]

                queue.append([cur[0].left, cur[1]+1])
                queue.append([cur[0].right, cur[1]+1])
        return list(res.values())
        