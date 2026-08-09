# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        s = [(root, root.val)]
        a = 0
        
        while s:
            node, m = s.pop()
            
            if node.val >= m:
                a += 1
                m = node.val
            
            if node.left:
                s.append((node.left, m))
            if node.right:
                s.append((node.right, m))
        
        return a
        