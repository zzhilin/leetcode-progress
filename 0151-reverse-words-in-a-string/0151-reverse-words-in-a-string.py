class Solution:
    def reverseWords(self, s: str) -> str:
        # 时间复杂度：O(n)
        # 空间复杂度：O(N)
        # 耗时：Pass 15 + 5
        # 思路 1 ：python string is immutable, so we will convert s to a list, reverse it, then reverse each single word
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
                
        
        s = list(s.strip())
        def trim(s):
            l, r = 0, len(s)-1
            res = []
            while l<=r:
                if s[l] != ' ':
                    res.append(s[l])
                elif res[-1] != ' ':
                    # print(res)
                    res.append(s[l])
                l += 1
            return res
        s=trim(s)
        n = len(s)
        reverse(0, n-1)
        i = 0 # start of word
        
        # e,u,l,b,' ',s,i
        # reverse word in s    
        while i < n:
            # print(s)
            if s[i] != ' ':
                r = i # end of word
                # find end of word
                while r < n and s[r] != ' ':
                    r += 1
                reverse(i, r-1)
                i = r
            else:
                i += 1
                
        # remove trailing space
        
                
        return ''.join(s).strip()
                    
            
        