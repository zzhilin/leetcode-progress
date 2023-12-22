class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        1 4 7
        2 5 8
        3 6 9
        """
        
        n = len(matrix)
        
        # transpose matrix
        for i in range(n):
            for j in range(i+1, n):
                # print(i,j)
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
                # print(matrix)
            matrix[i].reverse()
            