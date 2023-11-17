class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check if the board is a valid shape (done 9x9)
        Determine if the numbers in the cells create a valid board
        """
        # to check if row/col/subsquare is valid, and not compare every number one by one, save allnumbers we've seen in hash table
        row_cnt, col_cnt = 9, 9
        rows = [{} for _ in range(row_cnt)]
        cols = [{} for _ in range(col_cnt)]
        
        for i in range(row_cnt):
            d = rows[i]
            for j in range(col_cnt):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur not in d:
                    d[cur] = 1
                else:
                    return False
        for i in range(col_cnt):
            for j in range(row_cnt):
                cur = board[j][i]
                if cur == '.':
                    continue
                d = cols[i]
                if cur not in d:
                    d[cur] = 1
                else:
                    return False
        # check subsquares
        subsquares = [[{} for _ in range(3)] for _ in range(3)]
        for i in range(row_cnt):
            for j in range(col_cnt):
                cur = board[i][j]
                if cur == '.':
                    continue
                r, c = (i//3, j//3)
                subsquares[r][c][cur] = (subsquares[r][c].get(cur) or 0) + 1
                if subsquares[r][c][cur] > 1:
                    return False
        return True
                
                
        
        