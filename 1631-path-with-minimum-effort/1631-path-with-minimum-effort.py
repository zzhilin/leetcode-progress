class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        modified dijkstra to find lower weight path
        use heap that takes diff, diff matrix to track effort
        """
        m,n = len(heights),len(heights[0])
        pq = [(0,0,0)]
        effort = [[float("inf") for _ in range(n)] for _ in range(m)]
        effort[0][0] = 0
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        while pq:
            diff,i,j = heappop(pq)
            visited[i][j] = 1
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                r,c = i+dx,j+dy
                # validation
                if 0<=r<m and 0<=c<n and not visited[r][c]:
                    curr_diff = abs(heights[r][c] - heights[i][j])
                    max_diff = max(curr_diff, effort[i][j])
                    if max_diff < effort[r][c]:
                        effort[r][c] = max_diff
                        heapq.heappush(pq, (max_diff,r,c))
        return effort[-1][-1]
                    