class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        0,0 0,1 0,2 0,3 0,4
        1,0 1,1 1,2
        2,0 2,1 2,2
        3,0 3,1 3,2
        """
        # on diagnol sum of x,y is constant
        res = []
        diagonals = {}
        
        for x in range(len(nums)):
            for y in range(len(nums[x])):
                if x+y not in diagonals:
                    diagonals[x+y] = []
                diagonals[x+y].append(nums[x][y])
        for k in sorted(diagonals.keys()):
            # print(diagonals[k])
            res.extend(diagonals[k][::-1])
        return res