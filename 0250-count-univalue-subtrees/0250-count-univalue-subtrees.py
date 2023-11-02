# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.count = 0
        def dfs(node) -> bool:
            # checking if current subtree is uni-value
            
            if not node:
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                # if both childreen exist and have same value as node
                if node.left and node.left.val != node.val:
                    return False
                elif node.right and node.right.val != node.val:
                    return False
                else:
                    self.count += 1
                    return True
            # one or more children is not univalue
            return False
        dfs(root)
        return self.count
            