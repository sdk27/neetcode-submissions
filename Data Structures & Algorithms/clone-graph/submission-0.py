"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        copies = {}

        def dfs(original):
            if original in copies:
                return copies[original]

            clone = Node(original.val)
            copies[original] = clone

            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        if node is None:
            return None

        return dfs(node)
        