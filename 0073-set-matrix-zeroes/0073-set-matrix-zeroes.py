class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row and col is 0 indicators
        m = len(matrix) # row
        n = len(matrix[0]) # col
        
        row = [False for _ in range(m)]
        col = [False for _ in range(n)]
        
        # if we found any element which is 0 in that row for the ‘ROW’ vector and column for the 'COL' vector, change to True
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(m):
            for j in range(n):
                if (row[i] or col[j]):
                    matrix[i][j] = 0
                    