class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def bfs(i,j):
            q = collections.deque([(i,j)])
            board[i][j] = '#'
            while q:
                row, col = q.popleft()
                # check 4 directions
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny = row+dx, col+dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        q.append((nx,ny))
                        board[nx][ny] = '#'
        
        # check escaping Os
        # as these Os are not flippable, we need to find all connected Os using bfs
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O':
                        bfs(i,j)
                    
        
        # mark flippable cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'