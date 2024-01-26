class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 is root node, trigger dfs
        # number of root node is number of islands
        # mark visited
        m,n = len(grid),len(grid[0])
        num_islands = 0
        
        def is_valid(i,j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] != '2' and grid[i][j] != '0'
        
        def dfs(grid,i,j):
            if not is_valid(i,j):
                return
            grid[i][j] = '2'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid,i,j)
                    
        return num_islands
                    
        