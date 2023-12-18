class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

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
