class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        check no cycles and is connected
        dfs or bfs - bfs
        time: V+E
        space: (V+E)
        """
        visited = set()
        q = deque([0]) #cnt = 0
        visited_nodes = 0
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        while q:
            node = q.popleft()
            visited_nodes += 1
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
        if visited_nodes != n:
            return False
        return True
        