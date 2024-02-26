# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(node):
            if not node:
                return
            # flat left and right subtrees
            left = flat(node.left)
            right = flat(node.right)
            
            # empty left and connect to right
            node.left = None
            node.right = left
            
            # move to end of right(curr) and connect original right
            p = node
            while p.right:
                p = p.right
            p.right = right
            
            return node
        flat(root)