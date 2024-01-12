class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        size=len(s)//2
        cnt_a, cnt_b = 0,0
        for i in range(size):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                cnt_a += 1
        for i in range(size, len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                cnt_b += 1
                
        return cnt_a == cnt_b