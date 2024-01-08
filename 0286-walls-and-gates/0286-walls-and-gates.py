class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        wall = -1
        gate = 0
        INF = 2147483647
        
        # start bfs with all gates in queue
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == gate:
                    q.append((i,j))
                    
        while q:
            # search for next empty
            i,j = q.popleft()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = i+dx, j+dy
                if 0 <= nx < m and 0 <= ny < n:
                    if rooms[nx][ny] == INF:
                        rooms[nx][ny] = rooms[i][j] + 1
                        q.append((nx,ny))
                        
        return rooms