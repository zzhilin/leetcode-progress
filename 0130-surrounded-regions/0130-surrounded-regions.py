class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        # markall O that are on the border or adjacent to a 'O' cannot be flipped as 'E'
        def bfs(i,j):
            
            q = collections.deque([(i,j)])
            
            
            while len(q) > 0:
                i,j = q.popleft()
                if board[i][j] != 'O':
                    continue
                board[i][j] = 'E'
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        q.append((nx,ny))
                        # board[nx][ny] = 'E'
                    
                    
                
        # start bfs from border 'O' to find all escaped ones
        for i in range(m):
            bfs(i, 0)
            bfs(i, n-1)
        for j in range(n):
            bfs(0, j)
            bfs(m-1, j)
            
        # mark flippable cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'