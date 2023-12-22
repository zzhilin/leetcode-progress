class Solution:
    def maxScore(self, s: str) -> int:
        l_score, r_score = 0, 0
        res = 0
        n = len(s)
        mid = n//2
        l,r = 0, n-1
        
        """
        0 5
        1 4
        2 3
        
        tests:
        00 - both strs has to be non empty
        """
        
        while l < n-1:
            l_score = s[:l+1].count('0')
            r_score = s[n-r:].count('1')
            # print(s[:l+1], l_score)
            # print(s[n-r:], r_score)
            # print()
            sc = l_score+r_score
            res = max(res, sc)
            l += 1
            r -= 1
        return res