# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.p = float("-inf")
        self.tree = []
        def populate(root):
            if not root:
                return
            
            populate(root.left)
            self.tree.append(root.val)
            populate(root.right)
        populate(root)
        self.root = root

    def hasNext(self) -> bool:
        if self.p < len(self.tree)-1:
            return True
        return False

    def next(self) -> int:
        if self.p == float("-inf"):
            self.p = 0
        else:
            if self.p < len(self.tree):
                self.p += 1
        return self.tree[self.p]
        

    def hasPrev(self) -> bool:
        if self.p > 0:
            return True
        return False

    def prev(self) -> int:
        if self.p < len(self.tree) and self.p > 0:
            self.p -= 1
        return self.tree[self.p]
                


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()