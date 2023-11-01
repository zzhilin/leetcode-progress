# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
        length of longest consecutive increasing subsequence path
        """
        if not root.left and not root.right:
            return 1
        res = []
        def longest_len(node, parent, length):
            if not node:
                return
            if parent and node.val == parent.val + 1:
                length += 1
            else:
                length = 1
            res.append(length)
            longest_len(node.left, node, length)
            longest_len(node.right, node, length)
        longest_len(root, None, 0)
        return max(res)
        