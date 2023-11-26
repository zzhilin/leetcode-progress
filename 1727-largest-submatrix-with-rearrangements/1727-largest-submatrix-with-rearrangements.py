class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # find consecutive ones in each column
        n = len(matrix[0]) # cols
        m= len(matrix)
        res = 0

        for i in range(n):
            consecutive_ones = 0
            for row in range(m):
                if matrix[row][i] == 0:
                    consecutive_ones = 0
                    continue
                consecutive_ones += matrix[row][i]
                matrix[row][i] = consecutive_ones
        # sort in non decreasing order
        for row in matrix:
            row.sort(reverse=True)
            for i in range(len(row)):
                area = row[i] *(i+1)
                res = max(res, area)
        
        return res