class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,visited,grid):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] != '1':
                return False
            if (i,j) in visited:
                return False
            visited.add((i,j))
            dfs(i+1,j,visited,grid)
            dfs(i-1,j,visited,grid)
            dfs(i,j+1,visited,grid)
            dfs(i,j-1,visited,grid)
            return True
            
        visited = set()
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j,visited,grid):
                    cnt += 1
        return cnt