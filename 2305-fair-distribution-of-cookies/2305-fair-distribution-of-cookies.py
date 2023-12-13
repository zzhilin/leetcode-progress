class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
    
        def assign(cookie_cnt, child_no_cookie):
            if len(cookies)-cookie_cnt < child_no_cookie:
                return float('inf')
            if cookie_cnt == len(cookies):
                return max(res)
            ans = float('inf')
            for i in range(k):
                if res[i] == 0:
                    child_no_cookie -= 1
                res[i] += cookies[cookie_cnt]
                ans=min(ans,assign(cookie_cnt+1,child_no_cookie))
                res[i] -= cookies[cookie_cnt]
                if res[i] == 0:
                    child_no_cookie += 1
            return ans
            
        res = [0] * k

        return assign(0,k)
        