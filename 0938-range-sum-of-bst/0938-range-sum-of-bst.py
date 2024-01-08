# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(curr):
            if not curr:
                return 0
            total = 0
            if curr.val >= low and curr.val <= high:
                total += curr.val
            if curr.val > low:
                total += dfs(curr.left)
            if curr.val < high:
                total += dfs(curr.right)
            return total
            
        res = dfs(root)
        
        return res