class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # find consecutive ones in each column
        n = len(matrix[0]) # cols
        m= len(matrix)
        prev_row = [0] * n
        res = 0

        for row in range(m):
            curr_row = matrix[row][:]
            for col in range(n):
                if curr_row[col] != 0:
                    curr_row[col] += prev_row[col]
            sorted_row = sorted(curr_row, reverse=True)
            for i in range(len(sorted_row)):
                res = max(res, sorted_row[i] * (i+1))
            prev_row = curr_row
        # sort in non decreasing order

        return res