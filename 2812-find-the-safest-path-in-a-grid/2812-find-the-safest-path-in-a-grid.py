class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        visited = [[0 for _ in range(n)] for _ in range(n)]
        distance = [[0 for _ in range(n)] for _ in range(n)]
        depth = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        # multisource bfs start at 1
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j))
        while q:
            level = []
            for i,j in q:
                if not visited[i][j]:
                    visited[i][j] = 1
                    distance[i][j] = depth
                    for dx,dy in directions:
                        r = i+dx
                        c = j+dy
                        if 0 <= r < n and 0 <= c < n:
                            level.append((r,c))
            q = level
            depth += 1
        visited = [[0 for _ in range(n)] for _ in range(n)]
        
        # dij
        pq = []
        heapq.heappush(pq,(-distance[0][0],0,0))
        while pq:
            sf, i,j = heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j] = 1
            if i == n-1 and j == n-1:
                return -sf
            for dx,dy in directions:
                r = i+dx
                c=j+dy
                if 0 <= r < n and 0 <= c < n:
                    heappush(pq,(-min(-sf, distance[r][c]), r, c))
        return -1
                    