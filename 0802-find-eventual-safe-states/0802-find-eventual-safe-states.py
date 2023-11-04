class Solution:
    def is_safe(self, node, graph, visited,safe_nodes):
        if visited[node] == 1:
            return True
        if visited[node] == -1:
            return False
        
        visited[node] = -1
        # print(node,visited)
        # check neighbor safe or not
        for nei in graph[node]:
            if not self.is_safe(nei, graph, visited,safe_nodes):
                return False
        visited[node] = 1
        return True
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # failed 60
        
        # dfs
        visited = [0]*len(graph)
        safe_nodes = [] # res
        for i in range(len(graph)):
            if self.is_safe(i, graph, visited,safe_nodes):
                safe_nodes.append(i)
        return safe_nodes