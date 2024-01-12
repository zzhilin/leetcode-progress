class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs find duplicated edges
        self.dup_edge = []
        # build graph
        graph=defaultdict(list)
        
        def dfs(source, target, visited):
            if source not in visited:
                visited.add(source)
                if source == target:
                    return True
                
                return any(dfs(nei,target,visited) for nei in graph[source])
                
        for i,j in edges:
            visited = set()
            
            if i in graph and j in graph and dfs(i,j,visited):
                return i,j
            graph[i].append(j)
            graph[j].append(i)
