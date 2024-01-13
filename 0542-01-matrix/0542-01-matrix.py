class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # find distance between 1cell to closets0
        # starting bfs at each 1 for nearest 0
        
        # add all 1s to queue
        # update the distance in a copied matrix of mat during bfs
        
        m, n = len(mat), len(mat[0])
        matrix = [row[:] for row in mat]
        q = deque()
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    q.append((i,j))
                else:
                    matrix[i][j] = -1
                    
        
        print(matrix)
        depth = 1
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx,dy in directions:
                    r = i+dx
                    c=j+dy
                    if 0<=r<m and 0<=c<n and matrix[r][c] == -1:
                        q.append((r,c))
                        matrix[r][c] = depth
            depth += 1
        return matrix