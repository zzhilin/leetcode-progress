# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        if not root.left and not root.right:
            return root.val
        
        # bfs q 
        # init max level = 0
        # root, level(0)
        # while q 
        # curr node, node level
        # update selfmaxlevel
        # if it's first node at the max level, update return value
        # add left and right child to queue
        
        q = deque([(root, 0)])
        depth = 0
        res = 0
        while q:
            node, level = q.popleft()
            if level > depth:
                res = node.val
                depth = level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return res
        