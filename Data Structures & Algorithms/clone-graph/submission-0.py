"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def cloneNode(myNode):
            if myNode.val not in visited:
                newNode = Node(myNode.val)
                visited[myNode.val] = newNode
                for adj in myNode.neighbors:
                    newNode.neighbors.append(cloneNode(adj))
                return newNode
            else:
                return visited[myNode.val]
        
        if not node:
            return None
        return cloneNode(node)


            
        