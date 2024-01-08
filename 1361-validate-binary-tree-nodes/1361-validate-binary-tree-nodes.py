class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        has_parent = [False] * n
        
        
        # find root
        root = -1
        children = set(leftChild) | set(rightChild)
        for i in range(n):
            if i not in children:
                root = i
        
        # noroot
        if root == -1:
            return False
        
        # dfs for cycles
        visited = set()
        visited.add(root)
        
        def dfs(node):
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in visited:
                        return False
                    visited.add(child)
                    if not dfs(child):
                        return False
            return True
                    
                    
                    
        
        return dfs(root) and len(visited) == n