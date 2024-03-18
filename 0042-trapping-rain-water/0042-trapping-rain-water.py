class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0] * n
        post = [0] * n
        
        l, r = 0, n - 1
        pre[0] = height[0]
        post[r] = height[r]
        
        for i in range(1, n):
            pre[i] = max(height[i], pre[i-1])
        for i in range(n-2, -1, -1):
            post[i] = max(height[i], post[i+1])
        
        max_water = 0
        for i in range(n):
            print(f"postfix {post[i]}, prefix {pre[i]}, height {height[i]}")
            max_water += min(post[i], pre[i]) - height[i]
            
        return max_water