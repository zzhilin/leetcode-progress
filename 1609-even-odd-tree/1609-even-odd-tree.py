# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0:
            return False
        q = collections.deque()
        q.append(root)
        level = True
        while q:
            size = len(q)
            curr = float('-inf') if level else float('inf')

            
            for i in range(size):
                node = q.popleft()
                
                if level:
                    if node.val <= curr or node.val % 2 == 0:
                        return False
                else:
                    if node.val >= curr or node.val % 2 != 0:
                        return False
                curr = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level = not level
            
        return True
                
        