class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        greedy
        sort greed factors
        iterate through g, for each element compare to size
        '''
        g.sort()
        s.sort()
        res = 0
        cookie = len(s)

        n = len(g)
        cookie_i = 0
        while cookie_i < len(s) and res < n:
            if s[cookie_i] >= g[res]:
                res += 1
            cookie_i += 1
        return res
                