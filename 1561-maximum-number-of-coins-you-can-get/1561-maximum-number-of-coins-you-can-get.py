class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        1 2 3 4 5 6 7 8 9
        1 8 9
        2 6 7
        3 4 5
        
        1 2 2 4 7 8
        """
        
        piles.sort()
        res = 0

        alice = len(piles)-1
        for i in range(len(piles)//3):
            # print(i)
            # print(piles[alice-1])
            res += piles[alice-1]
            alice -= 2
        return res