# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        total = 0
        res = 0
        def count_nodes(node) -> (int, int):
            nonlocal res
            if not node:
                return 0, 0
            
            left, cnt_left = count_nodes(node.left)
            right, cnt_right = count_nodes(node.right)
            total = left+right+node.val
            cnt = cnt_left+cnt_right+1
            avg = total // cnt
            if avg == node.val:
                res += 1
            return total, cnt
        count_nodes(root)
        return res