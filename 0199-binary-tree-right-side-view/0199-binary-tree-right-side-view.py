# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order bfs
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            node, level = q.popleft()
            #found right node
            if len(res) == level:
                res.append(node.val)
            else:
                # update left -> right
                res[level] = node.val
            # go to next level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return res