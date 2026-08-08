# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        r = []
        s = [(root, 0)]
    
        while s:
            node, depth = s.pop()
        
            if node:
                if depth == len(r):
                    r.append(node.val)
            
                s.append((node.left, depth + 1))
                s.append((node.right, depth + 1))
    
        return r
        