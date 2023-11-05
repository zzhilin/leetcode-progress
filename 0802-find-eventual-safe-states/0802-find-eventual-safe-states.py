class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # get indegree
        indegree = {node: 0 for node in range(len(graph))}
        for i in range(len(graph)):
            for nei in graph[i]:
                indegree[i] += 1
                
        q = deque()
        # get adj list
        reverse_g = defaultdict(list)
        for i in range(len(graph)):
            for node in graph[i]:
                reverse_g[node].append(i)
        
        
        
        # q for bfs, add all nodes with indegree = 0
        for i in range(len(graph)):
            if indegree[i] == 0:
                q.append(i)
        
        # track safe nodes
        safe = [False] * len(graph)
        
        # pop, mark as safe, 
        while q:
            node = q.popleft()
            safe[node] = True
            for nei in reverse_g[node]:
                # - indeg nei by 1
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        res = []
        for i in range(len(graph)):
            if safe[i]:
                res.append(i)
                
        return res
        
        
        