class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """
        in 3x3 grid, minimum path to color all grids
        tracking distance moving vertically / horizontally a stone to target location (0)
        result: a grid of [[1,1,1],[1,1,1],[1,1,1]]
        find all permutations of pos with more than 1 stones, match with pos of 0 stones
        """
        res = float('inf')
        out = [] # indices of position > than 1 stones
        start_pos = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    start_pos.append([i,j])
                elif grid[i][j] > 1:
                    for _ in range(grid[i][j] - 1):
                        out.append([i,j])
        print(out)
        m = len(out)
        # permutation
        def permute(start):
            nonlocal res
            if start == m:
                cur = 0
                for i in range(m):
                    cur += abs(out[i][0] - start_pos[i][0]) + abs(out[i][1] - start_pos[i][1])
                res = min(res, cur)
                return
            # selec t
            for i in range(start,m):
                out[start], out[i] = out[i], out[start]
                permute(start+1)
                out[start], out[i] = out[i], out[start]
        permute(0)
        # return res
                    
        return res