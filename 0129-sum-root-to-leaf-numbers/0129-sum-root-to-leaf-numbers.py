# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def getSum(node, curr):
            if not node:
                return
            curr.append(str(node.val))
            if node.left == None and node.right == None:
                num = int(''.join(curr))
                res.append(num)
            else:
                if node.left:
                    getSum(node.left, curr)
                if node.right:
                    getSum(node.right, curr)
            curr.pop()
        getSum(root, [])
        return sum(res)
                
            