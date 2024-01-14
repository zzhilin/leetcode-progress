# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursive dfs
        # iscurr node > val
        # yes go left no go right
        # takes parent and curr node
        if not root:
            return TreeNode(val)
        
        def dfs(parent, node):
            # curr node is None, correct position
            if not node:
                child= TreeNode(val)
                if val < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                return
            if val > node.val:
                dfs(node, node.right)
            else:
                dfs(node, node.left)
        dfs(None, root)
        return root