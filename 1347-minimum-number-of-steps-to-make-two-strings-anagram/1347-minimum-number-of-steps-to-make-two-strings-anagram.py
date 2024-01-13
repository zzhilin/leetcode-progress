class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count, t_count = Counter(s), Counter(t)
        if s_count == t_count:
            return 0
        '''
        a: 1; b: 2
        a: 2; b: 1
        
        c - 1
        p - 1
        r - 1
        a - 1
        i - 1
        '''
        print(s_count,t_count)
        res = 0
        letter_s = list(s_count.keys())
        for letter, cnt in t_count.items():
            if letter not in letter_s:
                res += cnt
            else:
                if cnt > s_count[letter]:
                    res = res + (abs(s_count[letter] - cnt))
        return res