# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = []
        prev = None
        
        while s or root:
            while root:
                s.append(root)
                root = root.left
            
            root = s.pop()
            
            if prev is not None and root.val <= prev:
                return False
            
            prev = root.val
            root = root.right
        
        return True

        