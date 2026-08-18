# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None:
            return None

        root = TreeNode(preorder[0])
        s = [root]
        i = 0

        for x in preorder[1:]:
            node = s[-1]

            if node.val != inorder[i]:
                node.left = TreeNode(x)
                s.append(node.left)
            else:
                while s and s[-1].val == inorder[i]:
                    node = s.pop()
                    i += 1

                node.right = TreeNode(x)
                s.append(node.right)

        return root
        
        