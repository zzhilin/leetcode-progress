# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_list = defaultdict(list)
        # convert tree to undirected graph
        # recursive function build graph that takes root and parent potentially, initiated at None
        # traverse the tree and populate graph
        # initialize adjacency list
        # if there a parent, add an edge between node and parent
        # recursively build the graph on children
        def build_graph(node, parent=None):
            if not node:
                return
            
            if parent:
                adj_list[parent.val].append(node.val)
                adj_list[node.val].append(parent.val)
                
            
            build_graph(node.left,node)
            build_graph(node.right,node)
            # return adj_list
        
        build_graph(root)
        # print(graph)
        # bfs
        # initialize q with start
        q = collections.deque()
        q.append((start,0)) # minutes
        # track minutes
        minutes = 0

        visited = set()
        visited.add(start)
        
        while q:
            node,minutes = q.popleft()
            
            for nei in adj_list[node]:
                if nei not in visited:
                    q.append((nei,minutes+1))
                    
                    visited.add(nei)
                    
        return minutes