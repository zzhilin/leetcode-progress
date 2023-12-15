class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_len = 0
        for i in range(len(s)):
            if s[i].isalpha():
                total_len += 1
            else:
                total_len *= int(s[i])
        # total_len = total_len // int(s[-1])
        for i in range(len(s)-1,-1,-1):
            k %= total_len
            curr = s[i]
            if k == 0 and curr.isalpha():
                return curr
            if curr.isalpha():
                total_len -= 1
            else:
                total_len //= int(curr)
                
            