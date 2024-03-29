"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(node1, node2):
            if not node1 or not node2:
                return
            node1.next=node2
            # connect child nodes
            traverse(node1.left, node1.right)
            traverse(node2.left, node2.right)
            traverse(node1.right, node2.left)
            
            
        if not root:
            return None
        traverse(root.left, root.right)
        return root
        
        
            
            