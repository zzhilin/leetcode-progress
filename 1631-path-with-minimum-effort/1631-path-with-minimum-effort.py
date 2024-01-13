class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        input: 2d arr, each cell is height
        start at 0,0
        end at m-1,n-1
        effort is largest diff in height between two cell next to each other
        return min effort (find max in one path, min in all paths)
        
        constraints
        - height is always positive?
        
        test
        - heights= [[1]] return 0
        - single row [[1,2,4]] return 2 only one path
        - same height [[1,1,1],[1,1,1]] return 0
        
        compare each cell height
        
        '''
        m,n = len(heights),len(heights[0])
        q = [(0,0,0)]
        q.append((0,0,0))
        effort = [[float("inf") for _ in range(n)] for _ in range(m)]
        effort[0][0]=0
        visited = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while q:
            
            diff,i,j = heapq.heappop(q)

            visited[i][j] = 1
            for dx,dy in directions:
                r,c = i+dx,j+dy
                if 0<=r<m and 0<=c<n and not visited[r][c]:
                    curr_diff = abs(heights[r][c] - heights[i][j])
                    max_diff = max(curr_diff, effort[i][j])
                    if effort[r][c] > max_diff:
                        effort[r][c] = max_diff
                        heapq.heappush(q, (max_diff,r,c))
        return effort[-1][-1]
                    
        return 0