# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(start, end, memo):
            res = [] # all nodes root
            if start > end:
                res.append(None)
                return res
            if (start,end) in memo:
                return memo[(start,end)]
            
            for i in range(start, end+1):
                left = build(start, i-1, memo)
                right = build(i+1, end, memo)
                
                for l in left:
                    for r in right:
                        root = TreeNode(i, l, r)
                        res.append(root)
                
            memo[(start,end)] = res
            return res
                
        
        memo = {}
        build(1, n, memo)
        return memo[(1,n)]